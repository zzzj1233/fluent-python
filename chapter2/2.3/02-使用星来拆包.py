a, b, c, d, e = range(0, 5)

"""
    全拆 :  0 - 4
"""
print(a, b, c, d, e)

a, *bc, d = range(0, 4)

"""
    两边拆: 0 [1, 2] 3
"""
print(a, bc, d)

"""
    如果长度不够
    0 [] 1
"""
a, *bc, d = range(0, 2)

print(a, bc, d)
