import json
import random
from models.question import Question


class QuestionManager:

    """Управляет вопросами – загружает, находит, фильтрует, отмечвет"""

    def __init__(self, source: str="JSON", path:str=None):

        self.questions = {}  # хранилище вопросов

        self.source = source  # какой тип источника вопросовиспользуется
        self.path = path  # путь к источнику с вопросами

        self.load_questions()

    def load_questions(self) -> None:
        """Загружает вопросы в поле вопросов, ничего не возвращает"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                questions_raw = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print("Ошибка загрузки файла какая-то")
            questions_raw = []

        self.questions = {quest["pk"]: Question(**quest) for quest in questions_raw}

    def get_random(self) -> Question:
        """Возвращает один случайный вопрос"""
        # TODO OPTIMIZE AND INCREASE SPEED HERE
        # получаем случайный набор
        question = random.choice(list(self.questions.values()))
        # выпиливаем его из доступного
        return question

    def get_by_pk(self, pk: int) -> Question:
        """Возвращет вопрос по его pk"""
        return self.questions.get(pk)






