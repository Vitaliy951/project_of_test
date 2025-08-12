import pytest
import json
from unittest.mock import patch
from main import main

class TestMain:
    def test_main_execution(self, tmp_path, capsys):
        data_dir = tmp_path / "data"
        data_dir.mkdir()
        products_file = data_dir / "products.json"

        # Исправленная структура данных
        test_data = [{
            "name": "Смартфоны",
            "description": "Тестовые смартфоны",
            "products": [{
                "name": "Xiaomi",
                "description": "Смартфон",
                "price": 25000,
                "quantity": 5
            }]
        }]

        with open(products_file, 'w') as f:
            json.dump(test_data, f)

        with patch('src.product.Product.load_products') as mock_loader:
            mock_loader.return_value = [
                type('', (), {'description': 'смартфон', 'price': 25000})()
            ]
            main()

        captured = capsys.readouterr()
        assert "Средняя цена смартфонов: 25000.00 руб." in captured.out