import os
from typing import Generator

import src
from src.product import Product
from src.read_files import get_json_file


class Category:
    """Представляет категорию товаров."""

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
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Метод для вывода общего количества товаров в категории и списка товаров в формате:
        Название категории, количество продуктов: Х шт."""
        quantity_of_all_goods = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {quantity_of_all_goods}"

    @property
    def products(self) -> str:
        """Геттер, который будет выводить список товаров в виде строк в формате:
        Название продукта, (Стоимость) руб. Остаток: (Количество) шт."""
        product_strings = []

        for product in self.__products:
            product_str = str(product)
            product_strings.append(product_str)
        return "\n".join(product_strings)

    @products.setter
    def products(self, products: list) -> None:
        """Сеттер для установки списка товаров. Обновляет счётчик продуктов."""
        Category.product_count = len(self.__products)
        self.__products = [products]

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию. Обновляет счётчик продуктов."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError


def init_json_to_category() -> Generator[Category, str | list]:
    """Генератор для инициализации класса Category из файла "products.json"."""
    path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
    data = get_json_file(path)
    for item in data:
        product = list(src.product.init_json_to_product(item.get("product")))
        yield Category(item.get("name"), item.get("description"), product)
