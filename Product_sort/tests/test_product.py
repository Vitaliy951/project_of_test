import pytest
import json
# from pathlib import Path
from src.product import Product
from src.exceptions import ZeroQuantityError


class TestProduct:
    def test_creation_valid_product(self):
        product = Product("Телефон", "Смартфон", 25000, 5)
        assert product.price == 25000.0
        assert product.quantity == 5
        assert product.description == "Смартфон"

    def test_invalid_creation(self):
        with pytest.raises(ValueError):
            Product("", "Описание", 100, 1)

        with pytest.raises(ValueError):
            Product("Товар", "", 100, 1)

        with pytest.raises(ValueError):
            Product("Товар", "Описание", -100, 1)

        with pytest.raises(ZeroQuantityError):
            Product("Товар", "Описание", 100, 0)

    def test_price_setter(self):
        p = Product("Товар", "Описание", 100, 1)
        p.price = 150
        assert p.price == 150.0
        with pytest.raises(ValueError):
            p.price = -50

    def test_repr_format(self):
        product = Product("Ноутбук", "Игровой", 120000, 3)
        expected = "Product(name='Ноутбук', description='Игровой', price=120000.0, quantity=3)"
        assert repr(product) == expected

    def test_load_products(self, tmp_path):
        test_data = [{
            "name": "Электроника",
            "description": "Техника",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Android",  # исправлено: добавлено обязательное поле
                    "price": 25000,
                    "quantity": 5
                }
            ]
        }]

        file_path = tmp_path / "test_products.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False)

        products = Product.load_products(file_path)
        assert len(products) == 1
        assert products[0].name == "Смартфон"
        assert products[0].price == 25000.0

# Тест на дробное количество
def test_fractional_quantity():
    with pytest.raises(ZeroQuantityError):
        Product("Тест", "Описание", 100, 2.5)

# Тест на отсутствие описания в JSON
def test_missing_description_in_json(tmp_path):
    test_data = [{"products": [{"name": "Тест", "price": 100, "quantity": 1}]}]
    # Должен вызвать KeyError при загрузке
