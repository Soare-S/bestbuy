class Product:
    """Initializes a new instance of the Product class.
    Args:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product.
        active (bool): by default set True
    Raises NameError: If the name is empty, or the quantity or price is negative."""
    def __init__(self, name, price, quantity):
        if len(name) == 0 or quantity < 0 or price < 0:
            raise NameError("Invalid value")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Returns quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity of the product."""
        self.quantity += quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Checks if the product is active, return boolean."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Buys a specified quantity of the product.
        Returns total price of the purchase.
        Raises ValueError: If the quantity is greater than the available quantity."""
        if self.quantity == 0 or quantity > self.quantity:
            raise ValueError("Invalid quantity!")
        total_price = quantity * self.price
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price
