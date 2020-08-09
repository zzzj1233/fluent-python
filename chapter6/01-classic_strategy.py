"""
    使用类实现策略模式
"""
from collections import namedtuple

Customer = namedtuple("Customer", ["name", "integral"])


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


class IntegralPromo:
    def discount(self, order):
        if order.customer.integral > 1000:
            return order.total() * 0.05
        return 0


class BulkItemPromo:
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity > 20:
                discount = discount + order.total() * 0.01
        return discount


class LargeOrderPromo:
    def discount(self, order):
        discount = 0
        if len(order.cart) > 10:
            discount = order.total() * 0.07
        return discount
