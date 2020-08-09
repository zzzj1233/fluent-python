"""
    nonlocal关键字作用闭包函数的内部函数

    一旦内部函数需要修改外部函数的变量

    就需要使用nonlocal关键字声明变量

    原因和使用global关键字一样
"""


def test():
    call_count = 0

    def test2():
        nonlocal call_count
        call_count += 1
        return call_count

    return test2
