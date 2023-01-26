from models.player import Player


class PlayerManager:
    """Управляет активнымиигроками – создает, возвращает, удаляет """

    def __init__(self):
        self.players: dict[str:Player] = {}

    def create_player(self, sid: str, **player_data: any) -> Player:
        """Создает игрока sid и по переданной в произвольном формате игре"""
        player_data["sid"] = sid
        player = Player(**player_data)
        self.players[sid] = player

        return player

    def get_players(self) -> list[Player]:
        """
        Возвращает всех игроков
        :return:
        """
        return list(self.players.values())

    def remove_player(self, sid):
        self.players.pop(sid)

    def get_player_by_pk(self, sid: str) -> Player:
        """ Возвращает игрока по переданному sid"""
        return self.players.get(sid)
