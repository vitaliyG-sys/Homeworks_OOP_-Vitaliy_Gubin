import json
from unittest.mock import Mock, mock_open, patch

import pytest

from src.product import Product, init_json_to_product
from src.products.smartphone import Smartphone
from src.products.lawngrass import LawnGrass


def test_product_str(product_1: Product) -> None:
    """1. Функция для проверки работы магического метода __str__ класса Product."""
    assert str(product_1) == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'

def test_product_add(product_1: Product, product_2: Product) -> None:
    """2. Функция для проверки работы магического метода __add__ класса Product."""
    assert product_1 + product_2 == 1761000.0


def test_product_add_type_error(smartphone_1: Smartphone, lawngrass_1: LawnGrass)-> None:
    """1.1. Функция для проверки работы магического метода __str__ класса Product ошибка TypeError"""
    with pytest.raises(TypeError):
        smartphone_1 + lawngrass_1

def test_product(product_1: Product) -> None:
    """3. Функция для проверки работы класса Category."""
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_init_json_to_product(data_from_json: list[dict]) -> None:
    """4. Проверяет работу init_json_to_product."""
    products_json = json.dumps(data_from_json)
    with patch("builtins.open", mock_open(read_data=products_json)):
        with patch("json.load") as mock_get_json:
            mock_get_json.return_value = data_from_json

            generator = init_json_to_product()

            products = list(generator)

    # Собираем ожидаемые данные в список
    expected_products = []
    for category in data_from_json:
        for prod in category["products"]:
            expected_products.append(prod)

    # Поэлементная проверка каждого атрибута
    for product, expected in zip(products, expected_products):
        assert product.name == expected["name"]
        assert product.description == expected["description"]
        assert product.price == expected["price"]
        assert product.quantity == expected["quantity"]

    generator_from_data = init_json_to_product(data_from_json)
    products_from_data = list(generator_from_data)

    # Проверка результатов для ветки else
    assert len(products_from_data) == len(expected_products)


def test_product_verify_price_zero_price() -> None:
    """5. Проверка нулевой цены."""
    result = Product.verify_price(0.0)
    assert result is None


def test_product_verify_price_negative_price() -> None:
    """6. Проверка отрицательной цены."""
    result = Product.verify_price(-100.0)
    assert result is None


def test_product_verify_price_positive_without_old_price() -> None:
    """7. Положительная цена без старой цены."""
    new_price = 1000.0
    result = Product.verify_price(new_price)
    assert result == new_price


#
def test_product_verify_price_increase_price() -> None:
    """8. Повышение цены (новая цена больше старой)."""
    old_price = 1000.0
    new_price = 1500.0
    result = Product.verify_price(new_price, old_price)
    assert result == new_price


@patch("builtins.input", return_value="y")
def test_product_verify_price_decrease_price_confirm(mock_input: Mock) -> None:
    """9. Понижение цены, пользователь подтверждает изменение."""
    old_price = 1500.0
    new_price = 1000.0
    result = Product.verify_price(new_price, old_price)
    assert result == new_price
    mock_input.assert_called_once_with("Подтвердить изменение? y/n")


@patch("builtins.input", return_value="n")
def test_product_verify_price_decrease_price_cancel(mock_input: Mock) -> None:
    """10. Понижение цены, пользователь отменяет изменение."""
    old_price = 1500.0
    new_price = 1000.0
    result = Product.verify_price(new_price, old_price)
    assert result == old_price
    mock_input.assert_called_once_with("Подтвердить изменение? y/n")


@patch("builtins.input", side_effect=["invalid", "y"])
def test_product_verify_price_decrease_price_invalid_then_confirm(mock_input: Mock) -> None:
    """11. Понижение цены с некорректным вводом, затем подтверждение."""
    old_price = 1500.0
    new_price = 1000.0
    result = Product.verify_price(new_price, old_price)
    assert result == new_price
    assert mock_input.call_count == 2


@patch("builtins.input", side_effect=["invalid", "n"])
def test_product_verify_price_decrease_price_invalid_then_cancel(mock_input: Mock) -> None:
    """12. Понижение цены с некорректным вводом, затем отмена."""
    old_price = 1500.0
    new_price = 1000.0
    result = Product.verify_price(new_price, old_price)
    assert result == old_price
    assert mock_input.call_count == 2


def test_product_verify_price_same_price() -> None:
    """13. Цена не изменилась."""
    price = 1000.0
    result = Product.verify_price(price, price)
    assert result == price


def test_price_setter_with_valid_new_price(product_1: Product) -> None:
    """14. Тест установки корректной новой цены."""
    initial_price = product_1.price
    new_price = 200000.0
    product_1.price = new_price
    assert product_1.price == new_price
    assert product_1.price != initial_price


def test_price_setter_with_zero_price(product_1: Product) -> None:
    """15. Тест установки нулевой цены."""
    product_1.price = 0.0
    assert product_1.price == 180000.0


def test_price_setter_with_negative_price(product_1: Product) -> None:
    """16. Тест установки отрицательной цены (должна быть отклонена)."""
    initial_price = product_1.price
    negative_price = -5000.0
    product_1.price = negative_price
    # Цена не должна измениться
    assert product_1.price == initial_price


def test_price_getter_returns_correct_value(product_1: Product) -> None:
    """17. Тест геттера цены — возвращает корректное значение."""
    expected_price = 180000.0
    assert product_1.price == expected_price


def test_price_setter_calls_verify_price(product_1: Product, mocker: Mock) -> None:
    """18. Тест, что сеттер вызывает метод verify_price."""
    mock_verify = mocker.patch.object(product_1, "verify_price")
    new_price = 150000.0
    product_1.price = new_price
    mock_verify.assert_called_once()


def test_price_setter_no_change_when_verify_returns_none(product_1: Product, mocker: Mock) -> None:
    """19. Цена не меняется, если verify_price возвращает None."""
    mocker.patch.object(product_1, "verify_price", return_value=None)
    initial_price = product_1.price
    product_1.price = 99999.0
    assert product_1.price == initial_price


def test_verify_products_no_existing_products() -> None:
    """20. Нет существующих продуктов с таким именем — данные не меняются."""
    test_data = {"name": "Cмартфон", "description": "Описание", "price": 50000.0, "quantity": 10}
    result = Product.verify_products(test_data)
    assert result == test_data


def test_verify_products_existing_product_same_name() -> None:
    """21. Есть продукт с таким же именем — цена берётся максимальная, количество суммируется."""
    # Создаём существующий продукт
    _ = Product("Смартфон X", "Старый смартфон", 45000.0, 5)

    test_data = {
        "name": "Смартфон X",
        "description": "Новый описание",
        "price": 50000.0,  # Больше существующей цены
        "quantity": 3,
    }

    result = Product.verify_products(test_data)

    assert result["price"] == 50000.0  # Максимальная цена
    assert result["quantity"] == 8  # 5 + 3
    assert result["description"] == "Новый описание"  # Описание не меняется


def test_verify_products_existing_product_lower_price() -> None:
    """22. Существующий продукт с более высокой ценой — берётся существующая цена."""
    _ = Product("Смартфон Y", "Старый", 60000.0, 2)

    test_data = {
        "name": "Смартфон Y",
        "description": "Новое описание",
        "price": 55000.0,  # Меньше существующей цены
        "quantity": 4,
    }

    result = Product.verify_products(test_data)

    assert result["price"] == 60000.0  # Берётся максимальная цена (существующая)
    assert result["quantity"] == 6  # 2 + 4


def test_new_product_creates_correct_instance(new_product_data: dict) -> None:
    """23. new_product создаёт корректный экземпляр Product."""
    product = Product.new_product(new_product_data)
    assert isinstance(product, Product)
    assert product.name == new_product_data["name"]
    assert product.description == new_product_data["description"]


def test_new_product_with_no_existing_products(new_product_data: dict) -> None:
    """24. new_product без существующих продуктов — создаёт продукт с исходными данными."""
    # Удаляем все существующие продукты из gc, если они есть
    import gc

    for obj in gc.get_objects():
        if isinstance(obj, Product):
            del obj
    gc.collect()

    product = Product.new_product(new_product_data)
    assert product.price == new_product_data["price"]
    assert product.quantity == new_product_data["quantity"]

def test_add_product_with_zero_quantity() -> None:
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

