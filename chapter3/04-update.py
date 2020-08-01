info = {
    "name": "zzzj",
    "age": 20,
    "gender": "男"
}

update_value = {
    "name": "dl",
    "age": 21,
    "hobby": "女"
}

info.update(update_value)

# {'name': 'dl', 'age': 21, 'gender': '男', 'hobby': '女'}
print(info)