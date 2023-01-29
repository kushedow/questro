import eventlet

import logging

from src.models.game_session import GameSession
from src.models.player import Player
from src.models.question import Question

from src.service import QuestroMainService as service

# Выносим в отдельный файл создание сокета,
# чтобы иметь возможность разделить контроллер на несколько

from src.create_socket import sio, app

# Активируем логгер для сокета
socket_logger = logging.getLogger("socket")


def update_game_by_player_id(sid):
    """
    Отправляем информацию об игре всем ее участникам
    :param sid: sid пользователя
    """
    player: Player = service.get_player_by_sid(sid)
    game: GameSession = player.get_game()

    # TODO ограничить информацию по игровой сессии
    # player_ids = [player.sid for player in game.players_as_list]

    sio.emit("client/game_updated", data=game.dict())


# >>
# << client/welcome

@sio.event
def connect(sid, environ):
    socket_logger.info(f"CONNECTED {sid}")

    player: Player = service.create_player(sid)
    player_as_dict = player.dict()
    # отправляем сообщение что все нормально
    sio.emit("client/welcome", to=sid, data=player_as_dict)


# >> server/create_game
# << client/game_created

@sio.on('server/create_game')
def socket_start_game(sid, data):

    socket_logger.info(f"START GAME {sid}")

    # Создаем игровую сессию с указанной темой
    game: GameSession = service.create_game(
        player_sid=sid,
        cat=data.get("cat", "default")
    )

    # Отправляем информацию об игре создателю
    game_as_dict = game.dict()
    sio.emit("client/game_updated", to=sid, data=game_as_dict)


# >> server/join_game
# << client/game_updated

@sio.on('server/join_game')
def socket_join(sid, data):
    socket_logger.info(f"JOIN GAME {sid}")

    code = data['code']
    game = service.join_game_by_code(sid, code)

    if game is None:
        socket_exception(sid, "No game was found")
        return

    # sio.emit("client/game_updated", to=sid, data=game.dict())

    update_game_by_player_id(sid)


# >> server/record_answer
# << client/answer_recorded

# @sio.on('server/record_answer')
# def socket_answer(sid, data):
#
#     pk = int(data['pk'])
#     player = service.record_answer(sid, pk)
#     result = player.dict()
#
#     sio.emit("client/answer_recorded", to=sid, data=result)
#
#     # Теперь подберем вопрос для следующего пользователя
#
#     game = player.game
#     next_player = game.get_next_player(player)
#     question = service.get_next_question(game, player)
#
#     result: Question = question.dict()
#     sio.emit("client/answer_recorded", to=next_player.sid, data=result)


# >> server/get_questions
# << client/get_questions
@sio.on('server/get_questions')
def socket_get_questions(sid, data):
    socket_logger.info(f"GET QUESTION {sid} {data}")

    player: Player = service.get_player_by_sid(sid)

    game: GameSession = player.game
    if not game:
        socket_exception(sid, "no game selected")
        return

    questions: list[Question] = service.get_three_questions(game, player)

    sio.emit("client/get_questions", to=sid, data=[que.dict() for que in questions])


# >> server/pick_question
# << client/receive_question
@sio.on('server/pick_question')
def socket_get_question(sid, data):

    socket_logger.info(f"PICK QUESTION {sid}")

    player: Player = service.get_player_by_sid(sid)
    question_pk: int = data.get("pk")

    game: GameSession = player.game

    if not game: socket_exception(sid, "no game selected"); return
    if not question_pk: socket_exception(sid, "no question_pk selected"); return

    question:Question = service.get_question_by_pk(question_pk)

    next_player: Player = service.get_next_player(game, player)

    if not next_player: socket_exception(sid, "no next player found"); return

    next_player_sid: str = next_player.sid

    # print("sending question", question_pk, "from", player.sid, "to", next_player_sid)

    sio.emit("client/receive_question", to=next_player_sid, data=question.dict())


# >> server/get_categories
# >> client/get_categories
@sio.on("server/get_categories")
def socket_get_categories(sid, data):
    """ Возвращает список категорий """
    socket_logger.info(f"GET CATEGORIES {sid}")
    categories = service.get_categories()
    sio.emit("client/get_categories", to=sid, data=categories)


@sio.event
def disconnect(sid):

    print(f"DISCONNECTED {sid}")
    socket_logger.info(f"DISCONNECTED {sid}")

    player = service.get_player_by_sid(sid)
    game = player.game

    if game:
        service.remove_player_from_game(player, game)

    socket_exception(sid, "Один из игроков отсоединился. Начните с начала", broadcast=True)


#   СЛУЖЕБНЫЕ ОБРАБОТЧИКИ


# >> server/snapshot
# << client/snapshot

@sio.on('server/snapshot')
def socket_snapshot(sid, data):
    snapshot = service.snapshot()
    sio.emit("client/snapshot", to=sid, data=snapshot)


# << client/exception
def socket_exception(sid: str, error: str, broadcast=False):
    """
    Отправляет ошибку пользователю с указанным id
    Или всем пользователям в игре, если broadcast = True
    """
    socket_logger.info(f"EXCEPTION     {error}    {sid}")

    if not broadcast:
        sio.emit("client/exception", to=sid, data={"error": error})

    else:
        player = service.get_player_by_sid(sid)
        game = player.game

        if game is not None:

            for player_to_inform in game.players:
                sio.emit("client/exception", to=player_to_inform, data={"error": error})


def main():
    eventlet.wsgi.server(
        eventlet.listen(('', 80)), app
    )


if __name__ == '__main__':
    main()
