import json
import os

import pytest

from src.managers.categories_manager import CategoriesManager

path = os.path.join("..", "mocks", "categories.json")
categories_correct_keys = {"pk", "code", "title"}

class TestCategoriesManager:

    @pytest.fixture
    def manager(self):
        """ Фикстура для экземпляра класса менеджера """
        instance = CategoriesManager(path=path)
        return instance

    def test_get_all(self, manager):
        """ Проверяем загрузку всех категорий """
        result = manager.get_all()
        assert type(result) == list

        the_keys = set(result[0].dict().keys())
        assert categories_correct_keys.issubset(the_keys)


