class Category:
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1

    @property
    def product_count(self):
        return len(self.products)

    def middle_price(self):
        try:
            return round(sum(p.price for p in self.products) / len(self.products), 2)
        except ZeroDivisionError:
            return 0

    def __repr__(self):
        return f"Category(name={self.name}, product_count={self.product_count})"
