import deprecation

from config.config import QUESTION_SOURCE, CATEGORIES_SOURCE
from managers.categories_manager import CategoriesManager
from managers.game_manager import GameManager
from managers.player_manager import PlayerManager
from managers.question_manager import QuestionManager
from models.game_session import GameSession
from models.player import Player
from models.question import Question


class QuestroMainService:
    # создаем все менеджеры
    player_manager = PlayerManager()
    categories_manager = CategoriesManager(path=CATEGORIES_SOURCE)
    question_manager = QuestionManager(path=QUESTION_SOURCE)

    game_manager = GameManager(question_manager=question_manager)

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
    def create_game(cls, player_sid: str, cat: str = "default") -> GameSession:
        """Стартует игру, возврашает игру"""
        player = cls.player_manager.get_player_by_pk(sid=player_sid)
        game = cls.game_manager.start_game(cat=cat)
        cls.game_manager.add_player_to_game(player, game)
        return game

    # Подключаем к игре по коду

    @classmethod
    def join_game_by_code(cls, player_sid, code) -> GameSession | None:
        """ Присоединяет игрока к игре по коду, возвращает игру"""

        player = cls.player_manager.get_player_by_pk(player_sid)

        game = cls.game_manager.get_by_code(code)

        if not game:
            return None

        game = cls.game_manager.add_player_to_game(player, game)


        if game:
            return game

    @classmethod
    def remove_player_from_game(cls, player, game):
        cls.game_manager.remove_player_from_game(player, game)
        # Играем

    #### Вопросы ####

    # @classmethod
    # def get_next_question(cls, game, player) -> Question:
    #     """ Дает игроку вопрос """
    #     # question: Question = cls.question_manager.get_random()
    #     question
    #     return question

    @classmethod
    def get_three_questions(cls, game, player) -> list[Question]:
        """ Возвращает три вопросика"""
        # questions: list[Question] = cls.question_manager.get_random_three()
        questions: list[Question] = game.get_three_randoms()
        return questions

    @classmethod
    def get_question_by_pk(cls, question_pk) -> Question | None:
        """Возвращаем вопрос по его номеру"""

        question = cls.question_manager.get_by_pk(question_pk)
        return question

    @classmethod
    def pop_question_from_game(cls, player: Player, question_pk: int) -> Question | None:
        """ Получает вопрос по номеру и удаляет его из игры"""

        # Пытаемся получить игру, ругаемся если не можем
        game: GameSession = player.game
        if not game:
            return None

        # Получаем и удираем вопрос
        question = cls.get_question_by_pk(question_pk)
        game.remove_question(question_pk)

        return question


    @classmethod
    @deprecation.deprecated()
    def record_answer(cls, sid, pk):

        question = cls.get_question_by_pk(pk)
        player: Player = cls.get_player_by_sid(sid)
        player.add_answer(question)

        return player

    ### Работаем с категориями

    @classmethod
    def get_categories(cls):
        all_categories = cls.categories_manager.get_all()
        return [cat.dict() for cat in all_categories]

    ### Заканчиваем играть

    @classmethod
    def finish_game(cls, game_pk):
        # TODO Дописать завершение игры
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

    @classmethod
    def get_next_player(cls, game: GameSession, player: Player):
        """Получает следующего игрока в игре"""

        next_player = game.get_next_player(player)

        return next_player
