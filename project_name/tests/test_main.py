import os
import pytest
from project_name.src.main import Product, Category, CategoryIterator

"""Создание директории для тестов, если она отсутствует"""
test_results_dir = 'test_results'
os.makedirs(test_results_dir, exist_ok=True)


"""Функция для записи результатов тестов в файл"""
def write_test_results(results):
    with open(os.path.join(test_results_dir, 'results.txt'), 'w') as f:
        f.write(results)


"""Запуск тестов и запись результатов"""
if __name__ == '__main__':
    # Запуск pytest и получение результатов
    result = pytest.main(['--tb=short', '-q', '--disable-warnings'])

    """Получение текста результатов"""
    if result == 0:
        results_text = "Все тесты прошли успешно!\n"
    else:
        results_text = f"Некоторые тесты не прошли. Код ошибки: {result}\n"

    """Запись результатов в файл"""
    write_test_results(results_text)


def test_product_str():
    product = Product("Test Product", "Test Description", 100, 10)
    assert str(product) == "Test Product, 100 руб. Остаток: 10 шт."


def test_category_str():
    product1 = Product("Product 1", "Desc 1", 100, 5)
    product2 = Product("Product 2", "Desc 2", 200, 10)
    category = Category("Test Category", "Test Desc", [product1, product2])
    assert str(category) == "Test Category, количество продуктов: 15 шт."


def test_product_add():
    product1 = Product("Product 1", "Desc 1", 100, 5)
    product2 = Product("Product 2", "Desc 2", 200, 10)
    assert product1 + product2 == 2500  # 100*5 + 200*10


def test_category_iterator():
    product1 = Product("Product 1", "Desc 1", 100, 5)
    product2 = Product("Product 2", "Desc 2", 200, 10)
    category = Category("Test Category", "Test Desc", [product1, product2])
    iterator = CategoryIterator(category)

    products = [product for product in iterator]
    assert len(products) == 2
    assert str(products[0]) == str(product1)
    assert str(products[1]) == str(product2)


"""Запуск тестов"""
if __name__ == '__main__':
    # Запуск pytest и получение результатов
    result = pytest.main(['--tb=short', '-q', '--disable-warnings'])

    """Получение текста результатов"""
    if result == 0:
        results_text = "Все тесты прошли успешно!\n"
    else:
        results_text = f"Некоторые тесты не прошли. Код ошибки: {result}\n"

    """Запись результатов в файл"""
    write_test_results(results_text)
