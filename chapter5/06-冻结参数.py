from functools import partial
from operator import add

add_plus = partial(add, 10)

# 11
print(add_plus(1))

for i in range(0, 10):
    # 11~19
    print(add_plus(i))
