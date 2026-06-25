import gc
import os
from typing import Generator

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
        self.__price = price
        self.quantity = quantity


    def __str__(self) -> str:
        """ Метод для вывода информации о продукте в формате:
            Название продукта, ХХ руб. Остаток: ХХ шт."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """ Метод возвращает общую стоимость складываемых продуктов. """
        return self.quantity * self.__price + other.quantity * other.__price

    @property
    def price(self) -> float:
        """Геттер атрибута price."""
        return self.__price

    @staticmethod
    def verify_price(new_price: float, old_price: float | None = None) -> float | None:
        """Метод проверяет устанавливаемую цену:
        Если цена нулевая или отрицательная выводит предупреждение и возвращает None.
        Если имеется установленная сумма и устанавливаемая сумма меньше,
          выводит запрос подтверждения изменения цены "y/n"."""
        # Проверяем установку нулевой или отрицательной цены.
        if new_price <= 0:
            print("“Цена не должна быть нулевая или отрицательная”")
            return None
        # Предупреждение о понижении цены.
        elif old_price and old_price > new_price:
            while True:
                print("Устанавливаемая цена ниже установленной")
                confirm = input("Подтвердить изменение? y/n").lower()
                if confirm == "y":
                    return new_price
                elif confirm == "n":
                    return old_price
                else:
                    print("Введено неправильное значение должно быть 'y' или 'n'. ")
        else:
            return new_price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер атрибута price."""
        v_price = None
        if self.__price:
            old_price = self.__price
            v_price = self.verify_price(price, old_price)
        if not v_price:
            pass
        else:
            self.__price = v_price

    @staticmethod
    def verify_products(data: dict) -> dict:
        """Метод проверяет наличие товара в существующих классах.
        При положительном результате устанавливает максимальную цену и складывает количества."""
        for obj in gc.get_objects():
            if isinstance(obj, Product):
                if obj.name == data["name"]:
                    data["price"] = max(obj.price, data["price"])
                    data["quantity"] += obj.quantity
        return data

    @classmethod
    def new_product(cls, data: dict) -> Product:
        """Класс-метод, принимает на вход словарь с товаром:
        {"name": Название (str),
          "description": Описание (str),
          "price": Стоимость (float),
          "quantity": Количество (int)}
         Создает и возвращает объект класса Product."""
        v_data = cls.verify_products(data)
        return cls(v_data["name"], v_data["description"], v_data["price"], v_data["quantity"])


def init_json_to_product(json_data: list | None = None) -> Generator[Product, str | int | float]:
    """Генератор для инициализации класса Product из файла .json."""
    if not json_data:
        path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
        data = get_json_file(path)
    else:
        data = json_data

    for product_type in data:
        for product in product_type["products"]:
            result = Product(
                product.get("name"), product.get("description"), product.get("price"), product.get("quantity")
            )
            yield result
