import products


class Store:
    """A class representing a store that manages products."""

    def __init__(self, products):
        """Initialize the Store with a list of products."""
        self._products = products

    def add_product(self, product):
        """Add a product to the store."""
        self._products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        """Get the total quantity of products in the store."""
        total_units = 0
        for product in self._products:
            total_units += product.quantity
        return total_units

    def get_all_products(self) -> list:
        """Get a list of all active products in the store."""
        active_products = []
        for product in self._products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """Place an order for products in the store.
        Args:
            shopping_list (list): List of tuples containing a Product and the desired quantity.
        Returns:
            float: Total price of the order.
        Raises:
            ValueError if entered quantity is above of what is left in stock"""
        total_price = 0.0
        error = False
        for product, quantity in shopping_list:
            try:
                if isinstance(product, products.LimitedProduct) and 0 < quantity > 1:
                    print("This is a limited product, maximum one per order!")
                    error = True
                if not error:
                    total_price += product.buy(quantity)
            except ValueError:
                print("Not enough quantity in shop!")
        return total_price

    def __contains__(self, product):
        """Check if a product exists in the store."""
        return product in self._products
