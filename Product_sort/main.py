import json
import os

from src.product import Product


def main():
    try:
        # Загрузка продуктов
        products = Product.load_products(os.path.join('data', 'products.json'))

        # Фильтрация смартфонов
        smartphones = [p for p in products if 'смартфон' in p.description.lower()]

        if smartphones:
            avg_price = sum(p.price for p in smartphones) / len(smartphones)
            print(f"Средняя цена смартфонов: {avg_price:.2f} руб.")
        else:
            print("Смартфоны не найдены")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()