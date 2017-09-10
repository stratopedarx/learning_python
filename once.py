import functools


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.called = True
            func(*args, **kwargs)

    inner.called = False
    return inner


@once
def initialize():
    print 'initialize'

initialize()

initialize()

