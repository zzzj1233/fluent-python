promos = []

"""
    使用装饰器完善策略模式
"""


def promo(fun):
    promos.append(fun)
    return fun


@promo
def integral_promo(order):
    if order.customer.integral > 1000:
        return order.total() * 0.05
    return 0


@promo
def bulk_item_promo(order):
    if order.customer.integral > 1000:
        return order.total() * 0.05
    return 0


@promo
def large_order_promo(order):
    if order.customer.integral > 1000:
        return order.total() * 0.05
    return 0


def best_promo(order):
    return max(p(order) for p in promos)
