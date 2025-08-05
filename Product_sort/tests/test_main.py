import pytest
from src.product import Product, ZeroQuantityError
from src.category import Category


def test_product_creation():
    with pytest.raises(ZeroQuantityError):
        Product("Test", "Desc", 100, 0)


def test_category_average_price():
    products = [
        Product("Item1", "Desc1", 100, 1),
        Product("Item2", "Desc2", 200, 1)
    ]
    category = Category("Test", "Category", products)
    assert category.middle_price() == 150.0


def test_empty_category_average():
    category = Category("Empty", "Category")
    assert category.middle_price() == 0
