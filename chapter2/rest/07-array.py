from array import array
from random import random
import os

"""
    1. array : 扁平序列,存放的是指定数据类型的值,效率高
    2. 操作array和list基本一致
    3. array支持对文件进行读写操作,且效率高
"""

arr = array("i")

# 将一个可迭代对象拼接到数组的尾部
arr.extend([1, 2, 3, 4, 5])

# array('i', [1, 2, 3, 4, 5])
print(arr)

# 数组内每个元素的长度字节 : 4
print(arr.itemsize)

# 转换成list
print(arr.tolist())

# 写文件 10W个数据
arr2 = array('f', (random() for _ in range(10 ** 5)))

with open('07-array-data.bin', "wb") as f:
    arr2.tofile(f)
# 读文件
arr3 = array('f')
with open('07-array-data.bin', "rb") as f:
    arr3.fromfile(f, 10 ** 5)

# True
print(arr2 == arr3)

os.remove("07-array-data.bin")
