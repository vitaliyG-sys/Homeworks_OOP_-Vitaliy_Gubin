import os
from typing import Generator

from src.category import Category
from src.read_files import get_json_file


class Product:
    """Представляет продукт из категории товаров."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует продукт из категории товаров.
        Args:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Стоимость товара.
        quantity (int): Количество товаров.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


def init_json_to_product() -> Generator[Product, str | int | float]:
    """Генератор для инициализации класса Product."""
    path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
    data = get_json_file(path)
    for item in data:
        category = Category(item.get("name"), item.get("description"), item.get("products"))
        for prod in category.products:
            product = Product(
                prod.get("name"),
                prod.get("description"),
                prod.get("price"),
                prod.get("quantity"),
            )
            yield product
