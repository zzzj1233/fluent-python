from collections import defaultdict

"""
    在操作字典时,如果访问一个不存在的key
    
    1. dict[key]    ->  Raise KeyError
    2. dict.get(key) -> None
    3. dict.get(key,defaultValue) -> defaultValue
    4. 使用defaultDict
"""

"""
    第一个参数:
        ()->Any
        如果没有找到对应的key,则调用这个函数的返回值作为这个key的值
        这个方法仅仅在__setitem__时会被调用
        也就是说仅仅在dict[ket]被调用,dict.get(key)时不会被调用
"""

dic = defaultdict(lambda: "NoThing")

# NoThing
print(dic["name"])

# None
print(dic.get("name2"))

# defaultValue
print(dic.get("name3", "defaultValue"))