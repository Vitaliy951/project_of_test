class Product:
    """Базовый класс для всех продуктов."""

    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Невозможно сложить продукты разных типов")
        return self.price + other.price


class Smartphone(Product):
    """Класс для смартфонов, наследующий от Product."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы, наследующий от Product."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для категорий продуктов."""

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Добавляемый объект должен быть продуктом или его наследником")
        self.products.append(product)


if __name__ == '__main__':
    # Создание экземпляров смартфонов
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    # Вывод информации о смартфонах
    for smartphone in [smartphone1, smartphone2, smartphone3]:
        print(f"Смартфон: {smartphone.name}, Описание: {smartphone.description}, "
              f"Цена: {smartphone.price}, Количество: {smartphone.quantity}, "
              f"Эффективность: {smartphone.efficiency}, Модель: {smartphone.model}, "
              f"Память: {smartphone.memory}, Цвет: {smartphone.color}")

    # Создание экземпляров газонной травы
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    # Вывод информации о газонной траве
    for grass in [grass1, grass2]:
        print(f"Трава: {grass.name}, Описание: {grass.description}, "
              f"Цена: {grass.price}, Количество: {grass.quantity}, "
              f"Страна: {grass.country}, Срок прорастания: {grass.germination_period}, "
              f"Цвет: {grass.color}")

    # Сложение смартфонов
    smartphone_sum = smartphone1 + smartphone2
    print(f"Сумма цен смартфонов: {smartphone_sum}")

    # Сложение травы
    grass_sum = grass1 + grass2
    print(f"Сумма цен травы: {grass_sum}")

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")

    # Создание категорий
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)
    print(f"Продукты в категории смартфонов: {[product.name for product in category_smartphones.products]}")

    print(f"Общее количество продуктов: {Product.product_count}")

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
