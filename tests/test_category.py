from unittest.mock import Mock

import pytest

from src.category import Category, init_json_to_category
from src.product import Product


def test_category_str(category_1: Category) -> None:
    """1. Функция для проверки работы магического метода __str__ класса Category."""
    assert str(category_1) == 'Смартфоны, количество продуктов: 27'


def test_category(category_1: Category) -> None:
    """2. Проверяет работу класса Category."""
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Описание смартфонов"
    assert category_1.category_count == 2


def test_products_setter(category_1: Category, product_1: list[Product], data_from_json: list) -> None:
    """3. Тест сеттера "products" класса Category"""
    category_1.products = product_1
    assert category_1.products == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(category_1: Category, product_1: list[Product], data_from_json: list) -> None:
    """4. Тест метода "add_product" класса Category"""
    new_product = Product("test_name", "test_description", 100, 3)
    category_1.add_product(new_product)
    assert category_1.products == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                   'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                   'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'
                                   'test_name, 100 руб. Остаток: 3 шт.')


def test_add_product_type_error(category_1: Category) -> None:
    """4.1. Тест метода "add_product" класса Category ошибка TypeError"""
    with pytest.raises(TypeError):
        category_1.add_product("invalid_type")


def test_init_json_to_category(mock_get_json: Mock, category_1: Category, data_from_json: list[dict]) -> None:
    """5. Проверяет работу init_json_to_category."""

    # Вызываем тестируемую функцию
    generator = init_json_to_category()
    categories = list(generator)

    # Проверка количества категорий
    assert len(categories) == len(data_from_json)

    # Проверка первой категории
    assert categories[0].name == category_1.name
    assert categories[0].description == category_1.description
