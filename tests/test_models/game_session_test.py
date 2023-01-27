import pytest

from models.game_session import GameSession
from models.question import Question


class TestGameSession:
    # вопросики для теста

    questions = [
        Question(pk=1, text="Первый вопрос", cat="default"),
        Question(pk=2, text="Второй вопрос", cat="default"),
        Question(pk=3, text="Третий вопрос", cat="icebreak"),
        Question(pk=4, text="Четвертый вопрос", cat="icebreak"),
        Question(pk=5, text="Пятый вопрос", cat="date"),
    ]

    @pytest.fixture
    def sample_game(self):
        """ Пустая игра для теста"""
        questions = self.questions
        game = GameSession(pk=1)
        game.add_questions(questions)
        return game

    # questions

    def test_remove_question(self, sample_game):
        len_before = len(sample_game.questions)
        sample_game.remove_question(1)
        len_after = len(sample_game.questions)
        assert len_before - 1 == len_after, "Метод должен уменьшать на единичку"

    def test_get_three_randoms_if_full(self, sample_game):
        """ Проверяем как работает получение случ вопросов"""
        result = sample_game.get_three_randoms()
        assert type(result) == list, "Ожидается получение списка"
        assert len(result) == 3, "Ожидается получение списка длиной 3"
        assert type(result[0]) == Question, "Ожидается что в списке будут Question"

    def test_get_three_randoms_if_empty(self):
        game = GameSession(1)
        assert game.get_three_randoms() is None, "Ожидается None для игры без вопросов"

    # players

    def test_get_players(self):
        # TODO
        pass

    def test_add_player(self):
        # TODO
        pass

    def test_remove_player(self):
        # TODO
        pass

    def test_get_next_player(self):
        # TODO
        pass

    # serialization

    def test_dict(self):
        # TODO
        pass
