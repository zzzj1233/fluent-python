fruits = ["Coconut", "Banana", "Pear", "Apple"]

"""
    sort(key,reverse=False)    : 改变集合元素位置,返回None
    sorted(key,reverse=False)  : 返回一个排好序的集合,不会修改原集合
    
    key :     排序的函数
    reverse : 是否反序
"""

# ['Apple', 'Banana', 'Coconut', 'Pear']
print(sorted(fruits))

# ['Pear', 'Coconut', 'Banana', 'Apple']
print(sorted(fruits, reverse=True))

# ['Pear', 'Apple', 'Banana', 'Coconut']
# 相当于 key = len
print(sorted(fruits, key=lambda fruit: len(fruit)))

# ['Coconut', 'Banana', 'Apple', 'Pear']
print(sorted(fruits, key=lambda fruit: -len(fruit)))
