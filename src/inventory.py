from src.validators.product_validator import ProductValidator


class Inventory:
    """
    Handles inventory management system
        products (list) => A list of products in inventory
    """
    def __init__(self):
        self.__products = []
    
    @property
    def products(self):
        return self.__products
    
    def add_product(self, product):
        ProductValidator.validate_product(product)
        
        
