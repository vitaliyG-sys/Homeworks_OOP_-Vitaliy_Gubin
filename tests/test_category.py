from unittest.mock import Mock

from src.category import Category, init_json_to_category
from src.product import Product


def test_category(category_1: Category) -> None:
    """1. Проверяет работу класса Category."""
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Описание смартфонов"
    assert len(category_1.products) == 3
    assert category_1.category_count == 1
    assert category_1.product_count == 3


def test_products_setter(category_1: Category, product_1: list[Product], data_from_json: list) -> None:
    category_1.products = product_1
    assert category_1.products == ["Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5"]


def test_add_product(category_1: Category, product_1: list[Product], data_from_json: list) -> None:
    new_product = Product("test_name", "test_description", 100, 3)
    category_1.add_product(new_product)
    assert category_1.products[-1] == "test_name, 100 руб. Остаток: 3"


def test_init_json_to_category(mock_get_json: Mock, category_1: Category, data_from_json: list[dict]) -> None:
    """Проверяет работу init_json_to_category."""

    # Вызываем тестируемую функцию
    generator = init_json_to_category()
    categories = list(generator)

    # Проверка количества категорий
    assert len(categories) == len(data_from_json)

    # Проверка первой категории
    assert categories[0].name == category_1.name
    assert categories[0].description == category_1.description
    assert len(categories[0].products) == 4
