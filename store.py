from products import Product

class Store:
    """
    Represents a store containing multiple Product objects.
    Provides methods to manage products and process customer orders.
    """

    def __init__(self, products: list[Product]):
        """
        Initialize the store with a list of Product objects.

        :param products: list of Product instances to add to the store
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Add a new product to the store.

        :param product: Product instance to be added
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the store.

        :param product: Product instance to be removed
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.

        :return: Total number of items (int)
        """
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self) -> list[Product]:
        """
        Return all active products in the store.

        :return: List of Product objects that are active
        """
        active_products = []
        for product in self.products:
            if product.active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Process an order consisting of multiple products.
        Each item in shopping_list is a tuple: (Product, quantity).

        - Calls product.buy(quantity) for each tuple.
        - Accumulates and returns the total price.
        - buy() handles validation and exceptions.

        :param shopping_list: list of (Product, quantity) tuples
        :return: Total price of the entire order (float)
        """
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()
