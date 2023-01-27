import json
import logging

from models.category import Category

storage_logger = logging.getLogger("storage")


class CategoriesManager:

    def __init__(self, path: str = None):

        if path is None:
            raise ValueError
        self.path = path
        self._categories = []
        self._load()

    def _load(self):
        """ Загружает категории в поле вопросов, ничего не возвращает"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data_raw = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:

            storage_logger.error(f"Ошибка загрузки файла {self.path}")
            print(f"Ошибка загрузки файла {self.path}")

        self._categories = [Category(**cat_data) for cat_data in data_raw]

    def get_all(self):
        """ Все категории """
        return self._categories


