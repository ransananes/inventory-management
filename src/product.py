from .validators.type_validator import TypeValidator
from .validators.value_validator import ValueValidator

class Product:
    """
    Product 
    - name (str) => name of the product
    - quantity (int) => quantity of product in stock
    - price (float) => price per unit
    """
    def __init__(self, name, quantity, price):
        self.__set_name(name)
        self.__set_quantity(quantity)
        self.__set_price(price)

    @property
    def name(self):
        return self.__name
    
    def __set_name(self, value):
        TypeValidator.validate_str(value, self.__class__.__qualname__)
        self.__name = value
    
    @property
    def quantity(self):
        return self.__quantity
    
    def __set_quantity(self, value):
        TypeValidator.validate_integer(value,self.__class__.__qualname__)
        ValueValidator.validate_non_negative(value,self.__class__.__qualname__)
        self.__quantity = value
        
        
    @property
    def price(self):
        return self.__price
    
    def __set_price(self, value):
        TypeValidator.validate_num(value,self.__class__.__qualname__)
        ValueValidator.validate_non_negative(value,self.__class__.__qualname__)
        self.__price = value
    
    def get_total_price(self):
        # returns total price of product based on quantity * price (per unit)
        return self.price * self.quantity
    
    # tostring method
    def __str__(self):
        return f"Product => name={self.name}, quantity={self.quantity}, price={self.price:.2f}, total_price={self.get_total_price():.2f})"
