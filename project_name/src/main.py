class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены с двумя подчеркиваниями
        self.quantity = quantity

    @property
    def price(self):
        return self.__price  # Геттер для приватной цены

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:  # Если новая цена меньше старой
                confirm = input("Вы уверены, что хотите понизить цену? (y/n): ")
                if confirm.lower() == 'y':
                    self.__price = new_price
                else:
                    print("Цена не изменена.")
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data):
        """Создание нового продукта из словаря"""
        return cls(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])

class Category:
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products  # Приватный атрибут для списка продуктов
        Category.category_count += 1

    @classmethod
    def get_category_count(cls):
        return cls.category_count

    def get_product_count(self):
        return len(self._products)

    def add_product(self, product):
        self._products.append(product)  # Добавление продукта в список
        Product.category_count += 1  # Увеличение счетчика продуктов

    @property
    def products(self):
        """Геттер для получения списка продуктов в нужном формате"""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]
        )

if __name__ == "__main__":
    """Создание продуктов"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    """Создание категории"""
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    """Создание второй категории"""
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    """Вывод информации о категориях и продуктах"""
    print(f"Общее количество категорий: {Category.get_category_count()}")
    print(f"Количество продуктов в категории 1: {category1.get_product_count()}")
    print(f"Количество продуктов в категории 2: {category2.get_product_count()}")

    """Вывод списка продуктов в категории 1"""
    print(category1.products)

    """Добавление нового продукта в категорию 1"""
    new_product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(new_product)

    """Вывод обновленного списка продуктов в категории 1"""
    print(category1.products)
    print(f"Количество продуктов в категории 1 после добавления: {category1.get_product_count()}")

    """Создание нового продукта через класс-метод"""
    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    new_product_instance = Product.new_product(new_product_data)

    """Вывод информации о новом продукте"""
    print(new_product_instance.name)
    print(new_product_instance.description)
    print(new_product_instance.price)
    print(new_product_instance.quantity)

    """Изменение цены нового продукта"""
    new_product_instance.price = 800
    print(new_product_instance.price)

    """Попытка установить отрицательную цену"""
    new_product_instance.price = -100
    print(new_product_instance.price)

    """Установка цены в ноль"""
    new_product_instance.price = 0
    print(new_product_instance.price)
