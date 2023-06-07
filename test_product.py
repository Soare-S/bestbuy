import pytest
from main import *


# Test that creating a normal product works.
def test_normal_product():
    products.Product("iPhone 14, Gold, 256GB", 1209.99, 40)


# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_empty_name():
    with pytest.raises(NameError):
        products.Product("", 130.87, 40)


def test_negative_price():
    with pytest.raises(NameError):
        products.Product("Negative Price", -130.87, 40)


def test_negative_quantity():
    with pytest.raises(NameError):
        products.Product("", 130.87, -40)


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_inactive_if_zero_quantity_left():
    keys = products.Product("Keyring", 15.00, 10)
    keys.buy(10)
    assert keys.active is False


# Test that product purchase modifies the quantity and returns the right output.
def test_correct_amount_in_stock():
    keys = products.Product("Keyring", 15.00, 10)
    keys.buy(5)
    assert products.Product.get_quantity(keys) == 5


# Test that buying a larger quantity than exists invokes exception.
def test_buying_more_than_stock():
    keys = products.Product("Keyring", 15.00, 10)
    with pytest.raises(ValueError):
        keys.buy(15)
