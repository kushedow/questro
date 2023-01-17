import random
from dataclasses import dataclass


@dataclass
class GameSession:

    pk: int
    players: list = None #
    code: int = None # код для подключения к игре

    def __post_init__(self):

        self.code = self.generate_code()
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def dict(self, exclude=tuple()):

        result = {
            "pk": self.pk,
            "players": [player.dict() for player in self.players],
            "code": self.code
        }

        return result

    def get_next_player(self, player):
        """Передаем пользователя, получаем следующего"""
        index = self.players.index(player)
        next_player = self.players[index-1]
        return next_player

    def get_players(self):
        return self.players


    @staticmethod
    def generate_code():
        return random.randint(1111, 9999)
