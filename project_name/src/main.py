class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        raise StopIteration


# Пример использования
if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))
    print(category1.products)

    print(product1 + product2)  # Общая стоимость для product1 и product2
    print(product1 + product3)  # Общая стоимость для product1 и product3
    print(product2 + product3)  # Общая стоимость для product2 и product3

    # Использование итератора
    for product in CategoryIterator(category1):
        print(product)
