class SumAvg:
    def __init__(self):
        self.values = []

    def __call__(self, new_value):
        self.values.append(new_value)
        return sum(self.values) // len(self.values)


if __name__ == '__main__':
    sumavg = SumAvg()
    # 1
    print(sumavg(1))
    # 2
    print(sumavg(3))
    # 4
    print(sumavg(10))
