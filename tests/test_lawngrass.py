from src.products.lawngrass import LawnGrass

def test_lawngrass(lawngrass_1: LawnGrass):
    """1. Проверка инициализации класса LawnGrass."""
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"
