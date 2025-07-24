import pytest
from main import Product, Category


def test_product_initialization():
    product = Product("Test Product", "Test Description", 100, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100
    assert product.quantity == 10


def test_product_price_setter():
    product = Product("Test Product", "Test Description", 100, 10)
    product.price = 150
    assert product.price == 150

    product.price = -50  # Пытаемся установить отрицательную цену
    assert product.price == 150  # Цена не должна измениться


def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100, 10)
    product2 = Product("Product 2", "Description 2", 200, 5)
    category = Category("Test Category", "Test Description", [product1, product2])

    assert category.name == "Test Category"
    assert category.get_product_count() == 2


def test_add_product_to_category():
    product = Product("Product 1", "Description 1", 100, 10)
    category = Category("Test Category", "Test Description", [])
    category.add_product(product)

    assert category.get_product_count() == 1
    assert category.products == "Product 1, 100 руб. Остаток: 10 шт."


def test_new_product_class_method():
    product_data = {
        "name": "New Product",
        "description": "New Description",
        "price": 300,
        "quantity": 20
    }
    new_product = Product.new_product(product_data)

    assert new_product.name == "New Product"
    assert new_product.description == "New Description"
    assert new_product.price == 300
    assert new_product.quantity == 20
