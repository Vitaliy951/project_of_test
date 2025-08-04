class Product:
    """Класс для представления продукта."""

    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"
