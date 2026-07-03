import gc
from typing import Generator
from unittest.mock import patch

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


@pytest.fixture(autouse=True)
def cleanup_gc() -> None:
    """Фикстура для очистки gc перед каждым тестом."""
    gc.collect()


@pytest.fixture
def new_product_data() -> dict:
    """Фикстура с данными для нового продукта."""
    return {
        "name": "Samsung Galaxy C23 Ultra",  # То же имя, что у существующего
        "description": "Обновлённое описание",
        "price": 190000.0,  # Выше существующей цены
        "quantity": 3,
    }


@pytest.fixture
def mock_get_json(data_from_json: list[dict]) -> Generator:
    with patch("src.category.get_json_file") as mock:
        mock.return_value = data_from_json
        yield mock


@pytest.fixture
def category_1(data_from_json: list[dict]) -> Category:
    # Преобразуем словари продуктов в объекты Product
    products = [Product(p["name"], p["description"], p["price"], p["quantity"]) for p in data_from_json[0]["products"]]
    return Category(data_from_json[0]["name"], data_from_json[0]["description"], products)


@pytest.fixture
def product_1(data_from_json: list[dict]) -> Product:
    product_from_list = data_from_json[0]["products"][0]
    return Product(
        product_from_list["name"],
        product_from_list["description"],
        product_from_list["price"],
        product_from_list["quantity"],
    )

@pytest.fixture
def product_2(data_from_json: list[dict]) -> Product:
    product_from_list = data_from_json[1]["products"][0]
    return Product(
        product_from_list["name"],
        product_from_list["description"],
        product_from_list["price"],
        product_from_list["quantity"],
    )

@pytest.fixture
def product_samsung() -> Product:
    """Фикстура для товара Samsung."""
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет",
        price=180000.0,
        quantity=5
    )

@pytest.fixture
def product_iphone() -> Product:
    """Фикстура для товара Iphone."""
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )

@pytest.fixture
def product_xiaomi() -> Product:
    """Фикстура для товара Xiaomi."""
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )

@pytest.fixture
def category_with_products(product_samsung, product_iphone, product_xiaomi) -> Category:
    """
    Создает категорию, содержащую список объектов Product.
    Геттер .products автоматически превратит их в строку вида:
    "Samsung Galaxy C23 Ultra\nIphone 15\nXiaomi Redmi Note 11"
    """
    products_list = [product_samsung, product_iphone, product_xiaomi]
    return Category(
        name="Смартфоны",
        description="Лучшие смартфоны",
        products=products_list
    )