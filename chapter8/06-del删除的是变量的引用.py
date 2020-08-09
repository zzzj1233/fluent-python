import weakref

a = {1, 2, 3}
b = a


def dead():
    print("I'm die")


weakref.finalize(a, dead)

del a

# [1, 2, 3]
print(b)

# 如果不删除变量b的引用指向,那么dead函数将不会被调用
# del b

input()
