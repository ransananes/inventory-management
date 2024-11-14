import pytest
import sys 
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.inventory import Inventory

@pytest.fixture(scope="module")
def simple_inventory():
    inventory = Inventory()
    return inventory

# testing if inventory is empty
def test_inventory_initialization():
    inventory = Inventory()
    assert not inventory.products 

# testing if after adding the product exists
def test_add_and_get_product(simple_inventory, Apple):
    simple_inventory.add_product(Apple)
    assert simple_inventory.get_product(Apple.name) == Apple
    
# testing removing a product from inventory
def test_remove_product(simple_inventory, Apple):
    simple_inventory.remove_product(Apple.name)
    with pytest.raises(ValueError):
        simple_inventory.get_product(Apple.name)

# testing removing a product non-existant
def test_remove_nonexistent_product(simple_inventory):
    with pytest.raises(ValueError):
        simple_inventory.remove_product("Mallawah")

# testing inventory full
def test_total_value(simple_inventory,Apple,Melon):
    simple_inventory.add_product(Apple)
    simple_inventory.add_product(Melon)
    assert simple_inventory.total_inventory_value() == (Apple.price * Apple.quantity) + (Melon.price * Melon.quantity)
    

    