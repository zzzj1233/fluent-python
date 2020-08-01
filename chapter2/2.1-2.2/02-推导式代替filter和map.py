symbols = '$¢£¥€¤a'

# 使用for循环 + map + filter

iterator = filter(lambda symbol: symbol > 127, map(ord, symbols))
# [162, 163, 165, 8364, 164]
print(list(iterator))

# 使用列表推导式

# [162, 163, 165, 8364, 164]
print([ord(symbol) for symbol in symbols if ord(symbol) > 127])
