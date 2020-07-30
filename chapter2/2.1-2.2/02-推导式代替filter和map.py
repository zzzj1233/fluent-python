symbols = '$¢£¥€¤a'

# 使用for循环 + map + filter

iterator = filter(lambda symbol: symbol > 127, map(ord, symbols))
print(list(iterator))


# 使用列表推导式