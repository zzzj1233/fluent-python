b = 123


def test(a):
    print(a)
    print(b)


def test2(a):
    global b
    print(a)
    print(b)
    b = 2


# 正常执行
test(1)

"""
    11行发生异常 : local variable 'b' referenced before assignment
    因为函数内对变量b进行了赋值操作,所以b被认为是函数内局部变量,但是局部变量又找不到,所有抛出异常
    
    将b标记为全局变量即可
"""
test2(2)
