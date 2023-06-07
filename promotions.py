from abc import ABC


class Promotions(ABC):
    def __init__(self, name):
        self.name = name

    def apply_promotions(self, product, quantity):
        pass


class PercentDiscount(Promotions):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotions(self, product, quantity):
        discount = (self.percent / 100) * product.price * quantity
        return product.price * quantity - discount


class SecondHalfPrice(Promotions):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotions(self, product, quantity):
        items_for_half_price = quantity // 2
        items_to_pay_full_price = quantity - items_for_half_price
        total_price = (items_to_pay_full_price * product.price) + (items_for_half_price * product.price / 2)
        return total_price


class ThirdOneFree(Promotions):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotions(self, product, quantity):
        free_items = quantity // 3
        full_price_items = quantity - free_items
        return full_price_items * product.price
