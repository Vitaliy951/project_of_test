from src.exceptions import ZeroQuantityError
import logging

logger = logging.getLogger(__name__)

class Product:
    def __init__(self, name, description, price, quantity):
        if not name.strip():
            raise ValueError("Название обязательно")
        if not description.strip():
            raise ValueError("Описание обязательно")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ZeroQuantityError("Количество должно быть целым положительным числом")

        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = quantity

    @classmethod
    def load_products(cls, file_path):
        products = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                categories_data = json.load(f)
                for category in categories_data:
                    for product_data in category.get('products', []):
                        try:
                            products.append(cls(
                                name=product_data['name'],
                                description=product_data['description'],
                                price=product_data['price'],
                                quantity=product_data['quantity']
                            ))
                        except (KeyError, ValueError, ZeroQuantityError) as e:
                            logger.error(f"Ошибка загрузки '{product_data.get('name', 'Без названия')}': {e}")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.critical(f"Фатальная ошибка файла: {e}")
        return products
