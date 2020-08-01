score_list = [
    ("zzzj", 100),
    ("dl", 85),
    ("cjj", 86),
    ("lsq", 70),
    ("xd", 75)
]

"""
    1. 列表推导式     []
    2. 生成器推导式   ()
    3. 字典推导式     {}
"""

dic = {name: score for name, score in score_list}

print(dic)
