import json
from unittest.mock import mock_open, patch

from src.product import Product, init_json_to_product


def test_product(product_1: Product) -> None:
    """1. Функция для проверки работы класса Category."""
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_init_json_to_product(data_from_json: list[dict]) -> None:
    """2. Проверяет работу init_json_to_product."""
    products_json = json.dumps(data_from_json)
    with patch("builtins.open", mock_open(read_data=products_json)):
        with patch("json.load") as mock_get_json:
            mock_get_json.return_value = data_from_json

            generator = init_json_to_product()

            products = list(generator)

    # Собираем ожидаемые данные в список
    expected_products = []
    for category in data_from_json:
        for prod in category["products"]:
            expected_products.append(prod)

    # Поэлементная проверка каждого атрибута
    for product, expected in zip(products, expected_products):
        assert product.name == expected["name"]
        assert product.description == expected["description"]
        assert product.price == expected["price"]
        assert product.quantity == expected["quantity"]
