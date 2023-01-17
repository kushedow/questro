from managers.game_manager import GameManager, GameSession
from managers.player_manager import PlayerManager
from managers.question_manager import QuestionManager, Question

from config import QUESTION_SOURCE
from models.player import Player


class QuestroMainService:

    game_manager = GameManager()
    player_manager = PlayerManager()
    question_manager = QuestionManager(path=QUESTION_SOURCE)

    # Создаем пользователя при присоединении к игре

    @classmethod
    def create_player(cls, sid):
        return cls.player_manager.create_player(sid=sid)

    # Получаем пользователя

    @classmethod
    def get_player_by_sid(cls, sid):
        return cls.player_manager.get_player_by_pk(sid)

    # Создаем игру по запросу пользователя

    @classmethod
    def create_game(cls, player_sid: str) -> GameSession:
        """Стартует игру, возврашает игру"""
        player = cls.player_manager.get_player_by_pk(sid=player_sid)
        game = cls.game_manager.start_game()
        cls.game_manager.add_player_to_game(player, game)
        return game

    # Подключаем к игре по коду

    @classmethod
    def join_game_by_code(cls, player_sid, code) -> GameSession | None:
        """ Присоединяет игрока к игре по коду, возвращает игру"""

        player = cls.player_manager.get_player_by_pk(player_sid)
        print(player)

        game = cls.game_manager.get_by_code(code)
        print(game)

        if not game:
            return None

        game = cls.game_manager.add_player_to_game(player, game)
        print(game)

        if game:
            return game

    @classmethod
    def remove_player_from_game(cls, player, game):
        cls.game_manager.remove_player_from_game(player, game)
        # Играем

    #### Вопросы ####

    @classmethod
    def get_next_question(cls, game, player) -> Question:
        """ Дает игроку вопрос """
        question: Question = cls.question_manager.get_random()
        return question

    @classmethod
    def get_question_by_pk(cls, pk) -> Question:
        question = cls.question_manager.get_by_pk(pk)
        return question

    @classmethod
    def record_answer(cls, sid, pk):

        question = cls.get_question_by_pk(pk)
        player: Player = cls.get_player_by_sid(sid)
        player.add_answer(question)

        return player


    # Заканчиваем играть

    @classmethod
    def finish_game(cls, game_pk):
        """ Завершает игру"""
        pass

    @classmethod
    def snapshot(cls):
        """ Делает снэпшот всех активных объектов"""
        return {
            "active_games": repr(cls.game_manager.active_games),
            "active_players": repr(cls.player_manager.players),
            "questions": repr(cls.question_manager.questions),
        }


