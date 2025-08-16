class ZeroQuantityError(Exception):
    """Исключение при нулевом количестве товара"""
    def __init__(self, message="Количество товара не может быть нулевым"):
        super().__init__(message)