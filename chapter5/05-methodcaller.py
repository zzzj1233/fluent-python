from operator import methodcaller

to_upper = methodcaller("upper")

# HELLO WORLD
print(to_upper("Hello World"))

# 空格转换为 _
replace_with_sep = methodcaller("replace", " ", "-")

# Hello-World
print(replace_with_sep("Hello World"))
