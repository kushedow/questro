from models.game_session import GameSession
from models.player import Player


class GameManager:

    """ Управляет игровыми сессиями (играми) – создает, стартует, удаляет."""

    def __init__(self):
        # тут мы храним все активные игры, ключ – это pk
        self.active_games: dict[int:GameSession] = {}
        self.max_pk = 1

    def start_game(self) -> GameSession:
        """Стартует игру и возвращает ее"""

        game: GameSession = GameSession(self.max_pk)
        self.active_games[self.max_pk] = game

        # Пишем в общий список и инкрементируем pk
        self.max_pk += 1
        return game

    def terminate_by_pk(self, pk: int):
        """ Убиваем игру по ключу """
        game = self.active_games.pop(pk)
        game.status = "finished"

    def get_by_pk(self, pk: int) -> GameSession:
        """ Возвращаем игру по первичному ключу """
        return self.active_games.get(pk)

    def get_by_code(self, code: int) -> GameSession | None:
        """ Возвращаем игру по ее коду """
        print(code)
        for game in self.active_games.values():
            if game.code == code:
                return game

    ### Работаем с игроками ###

    def add_player_to_game(self, player: Player, game: GameSession) -> GameSession | None:
        """ Добаыляет игрока в игру"""
        if not player or not game:
            return None

        game.add_player(player)
        player.game = game

        return game

    def remove_player_from_game(self, player: Player, game: GameSession):
        """ Отвязывает игру от пользователя, а пользователя от игры"""
        game.remove_player(player)
        player.game = None
