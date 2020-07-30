words = ['a', 'b', 'c']
nums = [1, 2, 3, 4, 5]

print([(word, num) for word in words for num in nums])

print("-" * 50)

print([(num, word) for num in nums for word in words])
