import os
from typing import TYPE_CHECKING, Generator

import src
from src.read_files import get_json_file

if TYPE_CHECKING:
    from src.product import Product


class Category:
    """Представляет категорию товаров."""

    name: str
    description: str
    products: list[Product]

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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    @property
    def products(self) -> list:
        """Геттер, который будет выводить список товаров в виде строк в формате:
        Название продукта, (Стоимость) руб. Остаток: (Количество) шт."""
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity}")
        return result

    @products.setter
    def products(self, products: list) -> None:
        """Сеттер для установки списка товаров. Обновляет счётчик продуктов."""
        Category.product_count = 0
        Category.product_count += len(products)
        self.__products = [products]

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию. Обновляет счётчик продуктов."""
        self.__products.append(product)
        Category.product_count = 0
        Category.product_count += len(self.__products)




def init_json_to_category() -> Generator[Category, str | list]:
    """Генератор для инициализации класса Category из файла "products.json"."""
    path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
    data = get_json_file(path)
    for item in data:
        product = list(src.product.init_json_to_product(item.get("product")))
        yield Category(item.get("name"), item.get("description"), product)
