import json
# from src.product import Product
# from src.exceptions import ZeroQuantityError

class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    @property
    def middle_price(self):
        if not self.products:
            return 0
        return round(sum(p.price for p in self.products) / len(self.products), 2)

    @classmethod
    def load_categories(cls, file_path='data/categories.json'):
        try:
            with open(file_path, 'r') as f:
                return [cls(**category) for category in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []