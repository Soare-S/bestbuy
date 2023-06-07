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
        self.promotion = None

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

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def show(self) -> str:
        """Returns a string representation of the product."""
        if self.promotion is not None:
            promotion_info = f"Promotion: *** {self.promotion.name} ***"
        else:
            promotion_info = "*** No promotion ***"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}\n  {promotion_info}"

    def buy(self, quantity) -> float:
        """Buys a specified quantity of the product.
        Returns total price of the purchase.
        Raises ValueError: If the quantity is greater than the available quantity."""
        if quantity <= 0 or quantity > self.quantity:
            raise ValueError("Invalid quantity!")
        if self.promotion:
            return self.promotion.apply_promotions(self, quantity)
        else:
            total_price = quantity * self.price
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        if self.promotion is not None:
            promotion_info = f"Promotion: *** {self.promotion.name} ***"
        else:
            promotion_info = "*** No promotion ***"
        return f"{self.name}, Price: {self.price}, this is a non-stocked product.\n  {promotion_info}"

    def buy(self, quantity) -> float:
        if self.promotion:
            return self.promotion.apply_promotions(self, quantity)
        total_price = self.price * quantity
        return total_price


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        if self.promotion is not None:
            promotion_info = f"Promotion: *** {self.promotion.name} ***"
        else:
            promotion_info = "*** No promotion ***"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, maximum quantity per order" \
               f" {self.maximum}.\n  {promotion_info}"
