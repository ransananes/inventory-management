from src.inventory import Inventory
from src.product import Product

def main():
    try:
        apple = Product("Apple", 10, 0.5)
        apple2 = Product("Banana", 20, 5.5)
        apple3 = Product("Orange", 70, 7)
        
        print(apple)
        im = Inventory()
        im.add_product(apple)
        im.add_product(apple2)
        im.add_product(apple3)
        print(im.total_inventory_value())
        # im.remove_product("Apple")

    except (TypeError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
