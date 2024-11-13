from src.product import Product

class ProductValidator:
    """
        Product Validator => validate if instance is product
    """
    @staticmethod
    def validate_product(value: str, context: str=""):
        if not isinstance(value, Product):
            raise TypeError(f"{context} error: {value} must be a product.")
    
    @staticmethod 
    def validate_existance_product(product : Product, product_list : list):
        if product in product_list:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")    

