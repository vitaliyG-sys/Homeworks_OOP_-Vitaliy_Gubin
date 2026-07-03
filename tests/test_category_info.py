import pytest

from src.category_info import CategoryInfo


def test_category_info(category_with_products) -> None:
    info = CategoryInfo(category_with_products)
    iterator = iter(info)

    first = next(iterator)
    second = next(iterator)
    third = next(iterator)

    expected = category_with_products.products.split('\n')

    assert first == expected[0]
    assert second == expected[1]
    assert third == expected[2]

    with pytest.raises(StopIteration):
        next(iterator)

