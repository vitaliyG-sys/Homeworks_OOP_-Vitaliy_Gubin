from src.products.smartphone import Smartphone

def test_smartphone(smartphone_1: Smartphone):
    """1. Проверка инициализации класса Smartphone."""
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"
