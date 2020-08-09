import time
from functools import wraps


def clock(func):
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        spend_time = end - start

        args_str = ', '.join(repr(arg) for arg in args)
        kw_str = ['{} = {}'.format(repr(key), repr(value)) for key, value in kwargs.items()]

        function_name = func.__name__

        print("method : [{}] , 耗时:[{}] , result:[{}] , args : [{}] , kwargs: [] ".format(function_name, str('%.6f' % spend_time), result, args_str, kw_str))

    return clocked


@clock
def test(a):
    return 1 + a


# method : [test] , 耗时:[0.000001] , result:[3] , args : [2] , kwargs: []
test(2)
