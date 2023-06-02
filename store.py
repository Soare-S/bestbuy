class Store:
    """A class representing a store that manages products."""
    def __init__(self, products):
        """Initialize the Store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Get the total quantity of products in the store."""
        total_units = 0
        for product in self.products:
            total_units += product.quantity
        return total_units

    def get_all_products(self) -> list:
        """Get a list of all active products in the store."""
        active_products = []
        for product in self.products:
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
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError:
                print("Not enough quantity in shop!")
        return total_price