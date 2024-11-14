import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.product import Product

# testing constructor initialzation
def test_product_constructor():
    product = Product("Agvania", 100, 1.25)
    assert product.name == "Agvania"
    assert product.quantity == 100
    assert product.price == 1.25
    assert product.total_price() == (product.price * product.quantity)

# testing invalid params types
@pytest.mark.parametrize("name, quantity, price, exception", [
    (123, 10, 1.0, TypeError),
    ("Apple", "50", 1.25, TypeError),
    ("Apple", 50, "1.25", TypeError),
    ("Apple", -50, 1.25, ValueError),
    ("Apple", 50, -1.25, ValueError)
])

def test_product_invalid_params(name, quantity, price, exception):
    with pytest.raises(exception):
        Product(name, quantity, price)


# testing total price calculation
def test_product_total_price(Apple):
    assert Apple.total_price() == Apple.price * Apple.quantity