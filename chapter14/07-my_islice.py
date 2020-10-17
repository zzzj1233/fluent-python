from collections.abc import Sequence


def my_islice(seq, begin, stop, step=None):
    assert isinstance(seq, Sequence)
    idx = 0
    while idx < stop:
        if idx >= begin:
            yield seq[idx]
        idx += 1


if __name__ == '__main__':
    # 用于从可迭代对象中创建指定切片范围内的生成器
    nums = [num for num in range(100)]

    gen = my_islice(nums, 20, 50)

    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
