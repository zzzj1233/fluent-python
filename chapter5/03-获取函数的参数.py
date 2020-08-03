from inspect import signature


def test(name, age=22):
    """
    :param name: 姓名
    :param age:  年龄
    :return:     你的信息
    """
    return {"name": name, age: age}


# name -> name  default -> <class 'inspect._empty'>
# name -> age  default -> 22
for param in signature(test).parameters.items():
    print("name -> " + param[0], " default -> " + str(param[1].default))
