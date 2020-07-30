symbols = '$¢£¥€¤a'

# ord函数用于将一个字符串转为为unicode编码
print(ord(symbols[-1]))

unicode_list = []

for symbol in symbols:
    unicode_list.append(ord(symbol))

print(unicode_list)

unicode_list2 = [ord(symbol) for symbol in symbols]

print(unicode_list2)
