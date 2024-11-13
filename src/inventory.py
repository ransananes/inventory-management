from multiprocessing.sharedctypes import Value
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
        # Add product 
        ProductValidator.validate_product(product)
        ProductValidator.validate_existance_product(product,self.__products)
        self.__products.append(product)
    
    def remove_product(self, product_name: str):
        # Find product by name and remove it
        for product in self.__products:
            if product.name == product_name:
                self.__products.remove(product)
                print(f"Product '{product_name}' removed.")
                return True
        raise ValueError(f"Product '{product_name}' not found and can't be removed.")
        
    def get_product(self, product_name: str):
        # Find product by name and return it
        for product in self.__products:
            if product.name == product_name:
                return product
        raise ValueError(f"Product '{product_name}' not found.")
    
    def total_inventory_value(self):
        # Return sum of all the inventory value
        return sum(product.total_price() for product in self.__products)

        
        
