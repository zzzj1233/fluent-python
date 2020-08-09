def sumavg():
    values = []

    def avg(value):
        values.append(value)
        return sum(values) // len(values)

    return avg


if __name__ == '__main__':
    sa = sumavg()
    # 1
    print(sa(1))
    # 2
    print(sa(3))
    # 4
    print(sa(10))
