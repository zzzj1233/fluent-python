from functools import lru_cache

"""
    typed: 是否针对参数类型做区分
           如果参数是不同类型的,则会保存不同的结果
"""


@lru_cache(maxsize=128, typed=False)
def test(a):
    print("test -> a = {}".format(a))
    return a


if __name__ == '__main__':
    test(1)
    test(2)
    test(3)
    # 被缓存结果直接返回了
    test(3)
