import eventlet

from managers.game_manager import GameSession
from managers.player_manager import Player
from models.question import Question

from service import QuestroMainService as service

# Выносим в отдельный файл создание сокета,
# чтобы иметь возможность разделить контроллер на несколько

from create_socket import sio, app


def update_game_by_player_id(sid):
    """
    Отправляем информацию об игре всем ее участникам
    :param sid: sid пользователя
    """
    player: Player = service.get_player_by_sid(sid)
    game: GameSession = player.get_game()

    player_ids = [player.sid for player in game.get_players()]

    sio.emit("client/game_updated",  data=game.dict())


# << client/exception
def socket_exception(sid:str, error:str):
    """
    Отправляет ошибку пользователю с указанным id
    """
    sio.emit("client/exception", to=sid, data={"error": error})

# >>
# << client/welcome

@sio.event
def connect(sid, environ):
    player: Player = service.create_player(sid)
    player_as_dict = player.dict()
    # отправляем сообщение что все нормально
    sio.emit("client/welcome", to=sid, data=player_as_dict)


# >> server/create_game
# << client/game_created

@sio.on('server/create_game')
def socket_start_game(sid, data):

    game: GameSession = service.create_game(player_sid=sid)
    game_as_dict = game.dict()
    sio.emit("client/game_updated", to=sid, data=game_as_dict)


# >> server/snapshot
# << client/snapshot

@sio.on('server/snapshot')
def socket_snapshot(sid, data):
    snapshot = service.snapshot()
    sio.emit("client/snapshot", to=sid, data=snapshot)


# >> server/join_game
# << client/client/game_updated

@sio.on('server/join_game')
def socket_join(sid, data):

    code = data['code']
    game = service.join_game_by_code(sid, code)

    if game is None:
        socket_exception(sid, "No game was found")
        return

    sio.emit("client/game_updated", to=sid, data=game.dict())

    update_game_by_player_id(sid)


# >> server/record_answer
# << client/answer_recorded

@sio.on('server/record_answer')
def socket_answer(sid, data):

    pk = int(data['pk'])
    player = service.record_answer(sid, pk)
    result = player.dict()

    sio.emit("client/answer_recorded", to=sid, data=result)

    # Теперь подберем вопрос для следующего пользователя

    game = player.game
    next_player = game.get_next_player(player)
    question = service.get_next_question(game, player)

    result: Question = question.dict()
    sio.emit("client/answer_recorded", to=next_player.sid, data=result)


@sio.event
def disconnect(sid):
    print("disconnected", sid)
    player = service.get_player_by_sid(sid)
    game = player.game
    if game:
        service.remove_player_from_game(player, game)


if __name__ == '__main__':
    eventlet.wsgi.server(
        eventlet.listen(('', 5001)), app
    )
