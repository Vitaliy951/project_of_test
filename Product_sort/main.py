from src.category import Category
from src.product import Product, ZeroQuantityError


def main():
    try:
        # Тест добавления товара с нулевым количеством
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ZeroQuantityError as e:
        print(f"Ошибка: {str(e)}")
    else:
        print("Товар успешно добавлен")
    finally:
        print("Обработка добавления товара завершена\n")

    # Создание нормальных товаров
    products = [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5),
        Product("iPhone 15", "512GB, Space Gray", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]

    # Создание категорий
    smartphones = Category("Смартфоны", "Мобильные устройства", products)
    empty_category = Category("Пустая", "Категория без товаров")

    # Тестирование средней цены
    print(f"Средняя цена смартфонов: {smartphones.middle_price()} руб.")
    print(f"Средняя цена пустой категории: {empty_category.middle_price()} руб.")


if __name__ == '__main__':
    main()
