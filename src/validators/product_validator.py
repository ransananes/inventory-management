from src.product import Product

class ProductValidator:
    """
        Product Validator 
            - validate_product -> validate if instance is product
            - validate_existance_product -> check if product already exists
    """
    @staticmethod
    def validate_product(value: str, context: str=""):
        if not isinstance(value, Product):
            raise TypeError(f"{context} error: {value} must be a product.")
    
    @staticmethod 
    def validate_existance_product(product : Product, product_list : list):
        if product in product_list:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")  
        for _product in product_list:
            if product.name == _product.name:
                raise ValueError(f"Product '{product.name}' already exists in the inventory.") 

