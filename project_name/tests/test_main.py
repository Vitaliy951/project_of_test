import pytest
from unittest.mock import patch
from main import Product, Category

class TestProduct:
    @pytest.fixture
    def product(self):
        return Product("Test Product", "Test Description", 100.0, 10)

    def test_initial_attributes(self, product):
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 100.0
        assert product.quantity == 10

    def test_price_setter_valid(self, product):
        product.price = 120.0
        assert product.price == 120.0

    def test_price_setter_lower(self, product):
        with patch('builtins.input', side_effect=['y']):
            product.price = 80.0
        assert product.price == 80.0

    def test_price_setter_not_lower(self, product):
        with patch('builtins.input', side_effect=['n']):
            product.price = 80.0
        assert product.price == 100.0

    def test_price_setter_invalid(self, product):
        with patch('builtins.print') as mock_print:
            product.price = -50.0
            mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная")

        with patch('builtins.print') as mock_print:
            product.price = 0.0
            mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная")

class TestCategory:
    @pytest.fixture
    def category(self):
        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 3)
        return Category("Test Category", "Test Description", [product1, product2])

    def test_initial_attributes(self, category):
        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert category.get_product_count() == 2

    def test_add_product(self, category):
        new_product = Product("Product 3", "Description 3", 150.0, 4)
        category.add_product(new_product)
        assert category.get_product_count() == 3

    def test_products_property(self, category):
        expected_output = (
            "Product 1, 100.0 руб. Остаток: 5 шт.\n"
            "Product 2, 200.0 руб. Остаток: 3 шт."
        )
        assert category.products == expected_output
