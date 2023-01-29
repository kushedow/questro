import random
from dataclasses import dataclass

from models.question import Question


@dataclass
class GameSession:

    pk: int
    players: dict = None
    code: int = None  # код для подключения к игре

    questions: dict = None
    questions_cat: str = "default"

    def __post_init__(self):

        self.code = self._generate_code()
        self.players = {}
        self.questions = {}

    #   ДОПОЛНИТЕЛЬНЫЕ ПОЛЯ


    @property
    def players_as_list(self):
        return list(self.players.values())

    #   УПРАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯМИ

    def get_players(self):
        """ Возвращаем всех пользователей """
        return self.players

    def add_player(self, player):
        """ Добавляем пользователя в хранилище """
        sid = player.sid
        self.players[sid] = player

    def remove_player(self, player):
        """ Удаляем игрока, причем передаем самого игрока """
        sid = player.sid
        self.players.pop(sid)

    def get_next_player(self, player):
        """ Передаем пользователя, получаем следующего (технически предыдущего) """

        index = self.players_as_list.index(player)
        next_player = self.players_as_list[index-1]
        return next_player

    #   СЕРИАЛИЗАЦИЯ

    def dict(self):
        """ Возвращает сериализованную игру """
        result = {
            "pk": self.pk,
            "players": [player.dict() for player in list(self.players.values())],
            "code": self.code,
            "cat": self.questions_cat,
            "questions": [quest.dict() for quest in self.questions.values()]
        }

        return result

    # УПРАВЛЕНИЕ ВОПРОСАМИ

    # Поскольку мы уникализируем вопросы

    def add_questions(self, questions_to_add: list[Question]):
        """ Добавляет вопросы (из набора, например)"""
        self.questions = {quest.pk:quest for quest in questions_to_add}

    def set_category(self, cat_name):
        """ Устанавливаем категорию для игры"""
        self.questions_category = cat_name

    def remove_question(self, question_pk):
        if question_pk in self.questions:
            self.questions.pop(question_pk)

    def get_three_randoms(self) -> list[Question]:
        """ Возвращает три вопроса, если есть, если нет – None"""

        # Если вопросы закончились вернем None
        if len(self.questions) < 3:
            return []

        # Если вопросы есть - вернем три
        question_pks = random.sample([q for q in self.questions.keys()], k=3)
        result = [self.questions[pk] for pk in question_pks]
        return result

    # СЛУЖЕБНЫЕ МЕТОДЫ

    @staticmethod
    def _generate_code():
        """ Создает код, да так, чтобы коды были уникальными"""
        # TODO перенести в менеджер, чтобы хранить отдельно коды
        code = random.randint(1111, 9999)
        return code
