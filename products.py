class Product:
    """
    Represents a product in the store.
    Each product has a name, price, quantity, and active status.
    Provides methods for purchasing, updating quantity, and displaying information.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new Product instance.

        :param name: Name of the product (string)
        :param price: Price per unit (float), must be >= 0
        :param quantity: Number of available units (int), must be >= 0
        :raises Exception: If name is empty or price/quantity is negative
        """
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid product parameters")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Get the current available quantity of the product.

        :return: Quantity in stock (int)
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Update the product's quantity.

        If the quantity becomes 0, the product is automatically deactivated.

        :param quantity: New quantity (int)
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check whether the product is active.

        :return: True if active, False otherwise
        """
        return self.active

    def activate(self):
        """
        Mark the product as active.
        """
        self.active = True

    def deactivate(self):
        """
        Mark the product as inactive.
        """
        self.active = False

    def show(self):
        """
        Print all relevant product information in a readable format.
        """
        print(f"{self.name} | Price: {self.price}€ | Quantity: {self.quantity} | Active: {self.active}")

    def buy(self, quantity: int) -> float:
        """
        Purchase a given quantity of the product.

        - Validates that quantity is positive
        - Ensures the product is active
        - Ensures stock is sufficient
        - Reduces quantity accordingly
        - Deactivates the product if quantity reaches 0

        :param quantity: Number of units to buy (int)
        :return: Total price for the purchase (float)
        :raises Exception: For invalid quantity, inactive product, or insufficient stock
        """
        if quantity <= 0:
            raise Exception("Quantity must be positive")
        if not self.active:
            raise Exception("Cannot buy an inactive product")
        if quantity > self.quantity:
            raise Exception("Not enough stock available")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
