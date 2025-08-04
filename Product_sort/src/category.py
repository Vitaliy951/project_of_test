# src/category.py

class Category:
    category_count = 0  # Счетчик категорий

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1  # Увеличиваем счетчик при создании новой категории

    @property
    def product_count(self):
        return len(self.products)

    def __repr__(self):
        return f"Category(name={self.name}, product_count={self.product_count})"
