from src.product import Product

class ProductValidator:
    """
        Type Validator => validate data type
    """
    @staticmethod
    def validate_product(value, context=""):
        if not isinstance(value, Product):
            raise TypeError(f"{context} error: {value} must be a product.")
        

