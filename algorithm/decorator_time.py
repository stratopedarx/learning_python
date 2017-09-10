import time
import functools


def decorator_time(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        debug = 'The function "{}" takes {} seconds for {}.\n'.format(func.__name__, finish - start, *args)

        with open('algorithm times.txt', 'a') as f:
            f.write(debug)
        print debug

        return result
    return inner
