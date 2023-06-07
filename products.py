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
        self._name = name
        self._price = price
        self._quantity = quantity
        self.active = True
        self._promotion = None

    @property
    def quantity(self) -> float:
        """Returns quantity of the product."""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of the product."""
        self._quantity += quantity
        if self._quantity == 0:
            self.deactivate()

    @property
    def price(self):
        """The price of the product."""
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of the product.
        Raises:
            ValueError: If the price is negative."""
        try:
            if price < 0:
                raise ValueError
            self._price = price
        except ValueError:
            print("Error! Price cannot be negative")

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
        """Returns the promotion applied to the product, if any."""
        return self._promotion

    def set_promotion(self, promotion):
        """Sets the promotion for the product."""
        self._promotion = promotion

    def __str__(self) -> str:
        """Returns a string representation of the product."""
        if self._promotion is not None:
            promotion_info = f"Promotion: *** {self._promotion.name} ***"
        else:
            promotion_info = "*** No promotion ***"
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}\n  {promotion_info}"

    def buy(self, quantity) -> float:
        """Buys a specified quantity of the product.
        If there is any promotion then it is applied.
        Returns total price of the purchase.
        Raises ValueError: If the quantity is greater than the available quantity."""
        if quantity <= 0 or quantity > self._quantity:
            raise ValueError("Invalid quantity!")
        if self._promotion:
            return self._promotion.apply_promotions(self, quantity)
        else:
            total_price = quantity * self._price
            self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()
        return total_price

    def get_price(self):
        """Returns the price of the product."""
        return self._price

    def __lt__(self, other):
        """Comparison method for 'less than' operator.
            Return a boolean."""
        return self.get_price() < other.get_price()

    def __gt__(self, other):
        """Comparison method for 'greater than' operator.
            Return a boolean."""
        return self.get_price() > other.get_price()


class NonStockedProduct(Product):
    """Represents a non-stocked product, which has a quantity of 0 by default."""
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def __str__(self):
        """Returns a string representation of the non-stocked product."""
        if self._promotion is not None:
            promotion_info = f"Promotion: *** {self._promotion.name} ***"
        else:
            promotion_info = "*** No promotion ***"
        return f"{self._name}, Price: {self._price}, this is a non-stocked product.\n  {promotion_info}"

    def buy(self, quantity) -> float:
        """Buys a specified quantity of the non-stocked product.
            Returns total price of bought products."""
        if self._promotion:
            return self._promotion.apply_promotions(self, quantity)
        total_price = self._price * quantity
        return total_price


class LimitedProduct(Product):
    """Represents a limited quantity product, with a maximum quantity per order."""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def __str__(self):
        """Returns a string representation of the limited product."""
        if self._promotion is not None:
            promotion_info = f"Promotion: *** {self._promotion.name} ***"
        else:
            promotion_info = "*** No promotion ***"
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}, maximum quantity per order" \
               f" {self._maximum}.\n  {promotion_info}"
