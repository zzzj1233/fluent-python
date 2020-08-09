from weakref import WeakValueDictionary

"""
    将对象作为弱引用添加到value
    
    如果对象被释放,那么对于的key,value,item都会消失
"""


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return "Cheese( {} )".format(self.kind)

    def __eq__(self, other):
        if other is None:
            return False

        if other == self.kind:
            return True


cheese_list = [Cheese(item) for item in ["奶油", "芝士", "水果", "谷物"]]

# [Cheese( 奶油 ), Cheese( 芝士 ), Cheese( 水果 ), Cheese( 谷物 )]
print(cheese_list)

# 创建对象
weak_dict = WeakValueDictionary()
for cheese in cheese_list:
    weak_dict[cheese.kind] = cheese

# {'奶油': Cheese( 奶油 ), '芝士': Cheese( 芝士 ), '水果': Cheese( 水果 ), '谷物': Cheese( 谷物 )}
"""
    4 -> 4
"""
print(dict(weak_dict.items()))

cheese_list.remove("水果")
cheese_list.remove("芝士")


# {'奶油': Cheese( 奶油 ), '谷物': Cheese( 谷物 )}
"""
    已经被删除了两个item
"""
print(dict(weak_dict.items()))