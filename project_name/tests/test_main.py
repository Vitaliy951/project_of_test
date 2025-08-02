import pytest
from project_name.src.main import Product, Smartphone, LawnGrass, Category

def test_product_initialization():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100.0
    assert product.quantity == 10

def test_smartphone_initialization():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "Описание", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"

def test_lawn_grass_initialization():
    grass = LawnGrass("Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"

def test_product_count():
    initial_count = Product.product_count
    Product("Товар 1", "Описание 1", 100.0, 10)
    Product("Товар 2", "Описание 2", 200.0, 5)
    assert Product.product_count == initial_count + 2

def test_addition_same_type():
    smartphone1 = Smartphone("Samsung", "Описание", 1000.0, 1, 90.0, "Model A", 128, "Черный")
    smartphone2 = Smartphone("Iphone", "Описание", 1500.0, 1, 95.0, "Model B", 256, "Белый")
    assert smartphone1 + smartphone2 == 2500.0

def test_addition_different_type():
    smartphone = Smartphone("Samsung", "Описание", 1000.0, 1, 90.0, "Model A", 128, "Черный")
    grass = LawnGrass("Газонная трава", "Описание", 500.0, 10, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        _ = smartphone + grass

def test_add_product():
    category = Category("Смартфоны", "Описание категории")
    smartphone = Smartphone("Samsung", "Описание", 1000.0, 1, 90.0, "Model A", 128, "Черный")
    category.add_product(smartphone)
    assert len(category.products) == 1
    assert category.products[0] == smartphone

def test_add_invalid_product():
    category = Category("Смартфоны", "Описание категории")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")

if __name__ == "__main__":
    pytest.main()
