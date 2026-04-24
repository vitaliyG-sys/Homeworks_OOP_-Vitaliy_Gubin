import os
from typing import Generator

from src.read_files import get_json_file


class Category:
    """Представляет категорию товаров."""

    name: str
    description: str
    products: list  # [Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Инициализирует категорию товаров.
        Args:
        name (str): Категория товара.
        description (str): Описание категории товаров.
        products (list[dict]): Список товаров. Содержит словари с названием товара, описанием, количеством и ценой.
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)


def init_json_to_category() -> Generator[Category, str | list]:
    """Генератор для инициализации класса Category."""
    path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
    data = get_json_file(path)
    for item in data:
        yield Category(item.get("name"), item.get("description"), item.get("products"))
