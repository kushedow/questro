import json
import os

import pytest

from models.question import Question
from src.managers.question_manager import QuestionManager

path = os.path.join("..", "mocks", "questions.json")
question_correct_keys = {"pk", "cat", "text", "used"}


def load_mock_questions(path):
    with open(path) as file:
        return json.load(file)


class TestQuestionsManager:

    @pytest.fixture
    def manager(self):
        """ Фикстура для экземпляра класса менеджера"""
        instance = QuestionManager(path=path)
        instance.load_questions()
        return instance

    def test_get_all(self, manager):
        """ Проверяем что вопросы загружаются нормально """

        questions = manager.get_all()
        questions_mock = load_mock_questions(path)

        assert type(questions) == list, f"Ожидается список вопросов"
        assert len(questions) == len(questions_mock), f"Ожидается что вернется {len()} вопросов"

        # проверяем, что требуемые ключи передаются, но допускаем расширение
        question_keys = set(questions[0].dict().keys())
        assert question_correct_keys.issubset(question_keys), f"Не совпадают ключи {question_correct_keys} vs {question_keys}"

    def test_get_by_pk(self, manager):
        """ Проверяем, что получение вопроса по ключу работает"""

        one_pk = 1
        single_question = manager.get_by_pk(one_pk)
        assert single_question.pk == one_pk, f"Ожидается, что вернется вопрос {one_pk}"

    @pytest.mark.parametrize("cat_name", ["default", "date", "icebreake"])
    def test_get_by_category(self, manager, cat_name):
        """ Проверяем загрузку по категориям"""

        questions_by_category = manager.get_by_category(cat_name)

        assert type(questions_by_category) == list
        assert type(questions_by_category[0]) == Question
        for quest in questions_by_category:
            assert quest.cat == cat_name





