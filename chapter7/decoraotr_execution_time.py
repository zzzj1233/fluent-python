def basic_decoraotr(fun):
    print("basic_decoraotr called...")
    return fun


@basic_decoraotr
def test_fun():
    print("test..")


def un_decorate_fun():
    pass


if __name__ == '__main__':
    # basic_decoraotr called...
    #
    pass
