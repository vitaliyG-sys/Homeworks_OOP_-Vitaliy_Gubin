import json
from unittest.mock import mock_open, patch

from src.category import Category, init_json_to_category


def test_category(category_1: Category) -> None:
    """1. Проверяет работу класса Category."""
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Описание смартфонов"
    assert len(category_1.products) == 3
    assert category_1.category_count == 1
    assert category_1.product_count == 3


def test_init_json_to_category(data_from_json: list[dict]) -> None:
    """Проверяет работу init_json_to_category."""
    products_json = json.dumps(data_from_json)
    with patch("builtins.open", mock_open(read_data=products_json)):
        with patch("json.load") as mock_get_json:
            mock_get_json.return_value = data_from_json

            generator = init_json_to_category()

            categories = list(generator)

            # Проверка первой категории
            category_1 = categories[0]
            assert category_1.name == "Смартфоны"
            assert category_1.description == "Описание смартфонов"
            assert len(category_1.products) == 3

            # Проверка второй категории
            category_2 = categories[1]
            assert category_2.name == "Телевизоры"
            assert category_2.description == "Описание телевизоров"
            assert len(category_2.products) == 1
