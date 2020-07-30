from collections import namedtuple

"""
    1. 字符串,使用空格将属性分割
    2. 可迭代对象
"""
# namedtuple("Card", "name no id")

Card = namedtuple("Card", ["name", "no", "id", "range"])

"""
    3. 隐藏属性 _fields
        ('name', 'no', 'id')
"""
print(Card._fields)

"""
    4. 隐藏属性 _asdict(),方面我们查看对象属性
       {'name': '扑克牌', 'no': '0001', 'id': 1, 'range': [1, 2, 3, 4, 5, 6, 7, 8, 9]}
"""

print(Card("扑克牌", "0001", 1, range=list(range(1, 10)))._asdict())
