class PrintMixin:
    """ Класс-миксин для класса Product.
    Выводит в консоль информации какой класс и с какими параметрами был инициализирован."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
