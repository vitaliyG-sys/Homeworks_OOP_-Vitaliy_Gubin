import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def data_from_json() -> list[dict]:
    return [
        {
            "name": "Смартфоны",
            "description": "Описание смартфонов",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Описание телевизоров",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def category_1(data_from_json: list[dict]) -> Category:
    return Category(data_from_json[0]["name"], data_from_json[0]["description"], data_from_json[0]["products"])


@pytest.fixture
def product_1(data_from_json: list[dict]) -> Product:
    product_from_list = data_from_json[0]["products"][0]
    return Product(
        product_from_list["name"],
        product_from_list["description"],
        product_from_list["price"],
        product_from_list["quantity"],
    )
