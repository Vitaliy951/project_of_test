import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from product import Product
from category import Category

@pytest.fixture(autouse=True)
def reset_category_count():
    """Сбрасывает счетчик категорий перед каждым тестом."""
    Category.category_count = 0
    yield

@pytest.fixture
def products():
    """Создает тестовые продукты."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return product1, product2

def test_product_initialization(products):
    """Тестируем инициализацию продукта."""
    product1, _ = products
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

def test_product_repr(products):
    """Тестируем строковое представление продукта."""
    product1, _ = products
    assert repr(product1) == "Product(name=Samsung Galaxy S23 Ultra, price=180000.0)"

def test_product_price_update(products):
    """Тест обновления цены продукта."""
    product1, _ = products
    product1.price = 190000.0
    assert product1.price == 190000.0

@pytest.fixture
def category(products):
    """Создает тестовую категорию с продуктами."""
    return Category("Смартфоны", "Описание смартфонов", list(products))

def test_category_initialization(category):
    """Тестируем инициализацию категории."""
    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert len(category.products) == 2

def test_category_product_count(category):
    """Тестируем подсчет продуктов в категории."""
    assert category.product_count == 2

def test_category_count(category):
    """Тестируем общий счетчик категорий."""
    assert Category.category_count == 1

def test_category_repr(category):
    """Тестируем строковое представление категории."""
    assert repr(category) == "Category(name=Смартфоны, product_count=2)"
