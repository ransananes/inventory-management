from src.inventory import Inventory
from src.product import Product

def main():
    try:
        apple = Product("Apple", 10, 0.5)
        print(apple)
        im = Inventory()
        im.add_product(apple)
        im.add_product("test")


    except (TypeError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
