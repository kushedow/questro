import random
from dataclasses import dataclass


@dataclass
class GameSession:

    pk: int
    players: dict = None
    code: int = None  # код для подключения к игре
    questions: dict = None

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
            "code": self.code
        }

        return result

    # СЛУЖЕБНЫЕ МЕТОДЫ

    @staticmethod
    def _generate_code():
        return random.randint(1111, 9999)
