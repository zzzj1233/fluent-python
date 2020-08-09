"""
    类似java
    python也会对str,int做缓存(指定范围内)

    还有tuple
"""

s1 = "Zzzj"
s2 = "Zzzj"

# True
print(s1 is s2)

i1 = 199
i2 = 199

# True
print(i1 is i2)

t1 = (1, 2, 3)
t2 = (1, 2, 3)

# True
print(t1 is t2)
