"""
    使用类实现策略模式
"""
from abc import abstractclassmethod
from collections import namedtuple

Customer = namedtuple("Customer", ["name", "link_phone"])


class CartItem:
    def __init__(self, product_name, quantity: int, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:
    def __init__(self, customer, cart_items, promotion=None):
        self.customer = customer
        self.cart = list(cart_items)
        self.promotion = promotion
        self.__total = sum([cart_item.total() for cart_item in self.cart])

    def total(self):
        return self.__total

    def discount(self):
        if not self.promotion:
            return 0
        return self.promotion.discount(self)


