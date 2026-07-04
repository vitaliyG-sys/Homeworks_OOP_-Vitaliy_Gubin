from typing import Any

from src.category import Category


class CategoryInfo:
    """Представляет товары из категории."""

    category: Category
    _products: list
    _index: int

    def __init__(self, category: Category) -> None:
        self.category = category
        self._index = 0
        self._products = self.category.products.split("\n")

    def __iter__(self) -> CategoryInfo:
        self._index = 0
        return self

    def __next__(self) -> Any:
        if self._index < len(self._products):
            prod = self._products[self._index]
            self._index += 1
            return prod
        else:
            raise StopIteration
