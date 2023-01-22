import json
import logging
import random
from models.question import Question

storage_logger = logging.getLogger("storage")

class QuestionManager:
    """Управляет вопросами – загружает, находит, фильтрует, отмечвет"""

    def __init__(self, source: str = "JSON", path: str = None):

        self.questions = []  # хранилище вопросов

        self.source = source  # какой тип источника вопросовиспользуется
        self.path = path  # путь к источнику с вопросами

        self.load_questions()

    def load_questions(self) -> None:
        """Загружает вопросы в поле вопросов, ничего не возвращает"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                questions_raw = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:

            storage_logger.error(f"Ошибка загрузки файла {self.path}")
            print("Ошибка загрузки")
            questions_raw = []

        self.questions = [Question(**quest) for quest in questions_raw]

        storage_logger.error(f"STORAGE   Данные загружены")


    def get_random(self) -> Question:
        """Возвращает один случайный вопрос"""
        question = random.choice(self.questions)
        # выпиливаем его из доступного
        return question

    def get_random_three(self) -> list[Question]:
        """Возвращает три случайных вопроса"""
        sample_three: list = random.sample(self.questions, 3)
        return sample_three

    def get_by_pk(self, pk: int) -> Question:
        """Возвращает вопрос по первичному ключу"""
        for quest in self.questions:
            if quest.pk == pk:
                return quest
