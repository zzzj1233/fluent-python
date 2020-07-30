import os

"""
    只要是可迭代对象,都可以被拆包
"""

# ('H:\\pythonProject\\book\\chapter2\\2.3', '01-拆包.py')
print(os.path.split(__file__))

dir, file_name = os.path.split(__file__)

"""
    最简单的拆包
"""
print(dir)
print(file_name)


