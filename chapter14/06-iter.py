from random import randint


def gen():
    return randint(0, 6)


if __name__ == '__main__':
    # iter函数两个参数的用法

    # 一直迭代,直到gen函数返回值为5,抛出StopIter异常
    for i in iter(gen, 5):
        print(i)
