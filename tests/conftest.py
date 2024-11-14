# conftest.py
import pytest
import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.product import Product

# Products Fixtures => Apple, Melon
@pytest.fixture
def Apple():
    product = Product("Apple", 10, 1.90)
    return product

@pytest.fixture
def Melon():
    product = Product("Melon", 21, 10.35)
    return product


