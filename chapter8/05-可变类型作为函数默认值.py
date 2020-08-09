class Bus:
    """
        pycharm已经抛出警告
        Default argument value is mutable
    """

    def __init__(self, stus=[]):
        self.stus = stus

    def up(self, stu):
        self.stus.append(stu)

    def down(self, stu):
        self.stus.remove(stu)

    def __repr__(self):
        return "Bus(stus: {} )".format(self.stus)


bus = Bus()

bus.up("zzzj")
bus.up("dl")

# Bus(stus: ['zzzj', 'dl'] )
print(bus)

bus2 = Bus()

bus2.up("cjj")

# Bus(stus: ['zzzj', 'dl', 'cjj'] )
# list依然有zzzj和dl

"""
    因为默认值在函数被加载时,就成为了函数的属性
    就算创建再多的对象,这个 stu = [], []依旧指向的是同一个内存地址
"""
print(bus2)
