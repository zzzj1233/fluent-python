from collections import Counter

"""
    Counter是dict的子类
    可以统计Key出现的次数
"""

counter = Counter({'a': 1, 'b': 2, 'c': 3})

counter.update('aaabbc')

# Counter({'a': 4, 'b': 4, 'c': 4})
print(counter)
