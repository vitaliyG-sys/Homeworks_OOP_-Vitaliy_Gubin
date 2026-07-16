from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.product import Product


class BaseProduct(ABC):
    """ Абстрактный класс для класса Product. """

    @abstractmethod
    def __str__(self) -> str:
        """Метод для вывода информации о продукте в формате:
        Название продукта, ХХ руб. Остаток: ХХ шт."""
        pass  # pragma: no cover

    @abstractmethod
    def __add__(self, other: Product) -> float:
        """Метод возвращает общую стоимость складываемых продуктов."""
        pass  # pragma: no cover

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер атрибута price."""
        pass  # pragma: no cover

    @staticmethod
    @abstractmethod
    def verify_price(new_price: float, old_price: float | None = None) -> float | None:
        """Метод проверяет устанавливаемую цену:
        Если цена нулевая или отрицательная выводит предупреждение и возвращает None.
        Если имеется установленная сумма и устанавливаемая сумма меньше,
          выводит запрос подтверждения изменения цены "y/n"."""
        pass  # pragma: no cover

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер атрибута price."""
        pass  # pragma: no cover

    @staticmethod
    @abstractmethod
    def verify_products(data: dict) -> dict:
        """Метод проверяет наличие товара в существующих классах.
        При положительном результате устанавливает максимальную цену и складывает количества."""
        pass  # pragma: no cover

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict) -> Product:
        """Класс-метод, принимает на вход словарь с товаром:
        {"name": Название (str),
          "description": Описание (str),
          "price": Стоимость (float),
          "quantity": Количество (int)}
         Создает и возвращает объект класса Product."""
        pass  # pragma: no cover
