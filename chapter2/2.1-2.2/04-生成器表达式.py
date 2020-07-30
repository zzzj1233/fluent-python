"""
    生成器表达式和列表表达式的区别
    列表表达式 : [expression]
    生成器表达式 : (expression)
"""

generator = (i for i in range(0, 20))

# 延迟生成
print(next(generator))
print(next(generator))
print(next(generator))