from copy import deepcopy

l1 = [1, [2, 3], 4]

l2 = deepcopy(l1)

# True
print(l1 == l2)

l1[1].append(5)

# False
print(l1 == l2)

# [1, [2, 3], 4]
print(l2)