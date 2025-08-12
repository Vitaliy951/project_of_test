import pytest
import json
from src.category import Category
from src.product import Product


class TestCategory:
    def test_add_product(self):
        category = Category("Электроника", "Техника")
        product = Product("Телефон", "Смартфон", 25000, 5)
        category.add_product(product)
        assert len(category.products) == 1

    def test_middle_price(self):
        category = Category("Электроника", "Техника")
        assert category.middle_price == 0

        category.add_product(Product("Товар1", "Описание", 100, 1))
        category.add_product(Product("Товар2", "Описание", 200, 1))
        assert category.middle_price == 150.0

    def test_load_categories(self, tmp_path):
        test_data = [{
            "name": "Категория",
            "description": "Описание"
        }]

        file = tmp_path / "categories.json"
        with open(file, 'w') as f:
            json.dump(test_data, f)

        categories = Category.load_categories(file)
        assert len(categories) == 1
        assert categories[0].name == "Категория"