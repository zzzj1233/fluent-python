from functools import reduce
from operator import add

nums = list(range(1, 101))

sum = reduce(add, nums)

# 5050
print(sum)

# True
print(callable(reduce))

# True
print(callable(add))
