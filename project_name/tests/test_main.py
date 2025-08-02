import pytest
from project_name.src.main import Product, Smartphone, LawnGrass, Category

def reset_product_count():
    Product.product_count = 0


def test_product_creation():
    reset_product_count()  # Сброс счетчика перед тестом
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100.0
    assert product.quantity == 10


def test_smartphone_creation():
    reset_product_count()  # Сброс счетчика перед тестом
    smartphone = Smartphone("Samsung Galaxy", "Описание", 1000.0, 5, 95.5, "Galaxy", 128, "Синий")
    assert smartphone.name == "Samsung Galaxy"
    assert smartphone.efficiency == 95.5


def test_lawn_grass_creation():
    reset_product_count()  # Сброс счетчика перед тестом
    grass = LawnGrass("Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.country == "Россия"


def test_category_creation():
    reset_product_count()  # Сброс счетчика перед тестом
    product1 = Product("Товар1", "Описание1", 100.0, 10)
    product2 = Product("Товар2", "Описание2", 200.0, 5)
    category = Category("Категория", "Описание категории", [product1, product2])
    assert len(category.products) == 2


def test_add_product_to_category():
    reset_product_count()  # Сброс счетчика перед тестом
    category = Category("Категория", "Описание категории")
    product = Product("Товар", "Описание", 100.0, 10)
    category.add_product(product)
    assert len(category.products) == 1


def test_invalid_product_addition():
    reset_product_count()  # Сброс счетчика перед тестом
    category = Category("Категория", "Описание категории")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_product_addition_and_count():
    reset_product_count()  # Сброс счетчика перед тестом
    product1 = Product("Товар1", "Описание1", 100.0, 10)
    product2 = Product("Товар2", "Описание2", 200.0, 5)
    assert Product.product_count == 2
