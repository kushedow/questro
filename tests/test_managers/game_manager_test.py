import os

import pytest

from managers.question_manager import QuestionManager
from models.game_session import GameSession
from models.question import Question
from src.managers.game_manager import GameManager


class TestGameManager:

    pks_for_cat_default = {1, 2}
    pks_for_cat_date = {5}

    # вопросики

    questions = [
        Question(pk=1, text="Первый вопрос", cat="default"),
        Question(pk=2, text="Второй вопрос", cat="default"),
        Question(pk=3, text="Третий вопрос", cat="icebreak"),
        Question(pk=4, text="Четвертый вопрос", cat="icebreak"),
        Question(pk=5, text="Пятый вопрос", cat="date"),
    ]

    def test_start_game(self):

        """ Проверяем создание игры с подходящими вопросами"""

        question_manager = QuestionManager(path=os.path.join("..", "mocks", "questions.json"))
        game_manager = GameManager(question_manager=question_manager)

        # default

        game_default: GameSession = game_manager.start_game(cat="default")
        questions_ids: list = [key for key in game_default.questions.keys()]
        assert set(questions_ids) == self.pks_for_cat_default, "Неверный подбор вопросов по категории"

        # date

        game_date: GameSession = game_manager.start_game(cat="date")
        questions_ids: list = [key for key in game_date.questions.keys()]
        assert set(questions_ids) == self.pks_for_cat_date, "Неверный подбор вопросов по категории"


