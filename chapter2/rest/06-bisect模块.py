import bisect

"""
    1. bisect.bisect(sortedSeq, val) : index:Int
        返回的index的元素的值大于val
        index左侧的值都小于等于val
"""

l = [1, 3, 5, 7, 9]

# return : 3 -> l[3] = 7
print(bisect.bisect(l, 6))

# return : 3
print(bisect.bisect(l, 5))

"""
    2. bisect.insort(sortedSeq, val)
        向一个排好序的序列中插入值
        任然保证其顺序
"""

bisect.insort(l, 6)

# [1, 3, 5, 6, 7, 9]
print(l)