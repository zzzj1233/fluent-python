from operator import contains, itemgetter, attrgetter

"""
    operator模块定义了一些常用的操作函数
        1. add
        2. iadd
        3. mul
        4. div ...
        
        5. itemgetter   -  xxx[index]
        6. contains     -  x in xx
        7. attrgetter   -  x.key
"""

countrys = [
    ["Tokyo", "JP"],
    ["New-Yock", "USA"],
    ["Beijin", "ZH"]
]

index_0_item = itemgetter(0)

for country in countrys:
    """
    - itemgetter
        1. Tokyo
        2. New-Yock
        3. Beijin
    """
    print(index_0_item(country))

print("-" * 50)

"""
    - contains
        True
"""
print(contains(countrys, ["Tokyo", "JP"]))

print("-" * 50)