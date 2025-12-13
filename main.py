from products import Product
from store import Store


def list_products(store: Store):
    """Print all active products."""
    for product in store.get_all_products():
        product.show()


def show_total_quantity(store: Store):
    """Print the total quantity of all items in the store."""
    print(store.get_total_quantity())


def make_order(store: Store):
    """
    Allow the user to select a product and place an order.
    Handles input errors and prints result.
    """
    products = store.get_all_products()

    if not products:
        print("No active products available.")
        return

    print("\nAvailable products:")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.name} (Quantity: {product.quantity}, Price: {product.price}€)")

    try:
        choice = int(input("Select product number: "))
        product = products[choice - 1]

        quantity = int(input("Enter quantity: "))

        total = store.order([(product, quantity)])
        print(f"Order successful! Total price: {total}€")

    except (ValueError, IndexError):
        print("Invalid selection.")
    except Exception as e:
        print(f"Order failed: {e}")


def start(store: Store):
    """Main UI menu loop."""
    while True:
        print("\nStore Menu\n----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


def main():
    """Initialize inventory and start UI."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
