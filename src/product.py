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
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        TypeValidator.validate_str(value, self.__class__.__qualname__)
        self.__name = value
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        TypeValidator.validate_integer(value,self.__class__.__qualname__)
        ValueValidator.validate_non_negative(value,self.__class__.__qualname__)
        self.__quantity = value
        
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        TypeValidator.validate_num(value,self.__class__.__qualname__)
        ValueValidator.validate_non_negative(value,self.__class__.__qualname__)
        self.__price = value
    
    def get_total_price(self):
        # returns total price of product based on quantity * price (per unit)
        return self.price * self.quantity