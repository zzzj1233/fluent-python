import random

"""
    if dict[key] not exists:
        dict[key] = default
    else:
        pass
"""

random_list = [random.randint(0, 500) for _ in range(0, 20)]

sta_dict = dict()

for num in random_list:
    if num % 3 == 0:
        sta_dict.setdefault("3", []).append(num)
    elif num % 4 == 0:
        sta_dict.setdefault("4", []).append(num)
    elif num % 5 == 3:
        sta_dict.setdefault("5", []).append(num)

"""
{
 '3': [255, 240, 282, 387, 357, 138, 33, 150], 
 '4': [176],
 '5': [383, 193] 
}
"""
print(sta_dict)
