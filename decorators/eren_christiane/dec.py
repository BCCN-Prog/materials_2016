import functools


def deprecated(str):
    def deprecated_aux(func):
        func._seen = False

        # @functools.wraps(func)
        def newfunc(*args, **kwargs):
            if not func._seen:
                print(func.__name__ + ' is deprecated, use ' + str)
                func._seen = True
            return func(*args, **kwargs)

        functools.update_wrapper(newfunc, func)
        return newfunc

    return deprecated_aux


@deprecated('math.pow')
def power(x, n=1):
    """Return x^n"""
    y = x
    if n == 0:
        return 1
    for i in range(n - 1):
        y = y * x
    return y


@deprecated
def add(x, y):
    """Return x + y"""
    return x + y


def test_power():
    x = 10.
    n = [0, 1, 2, 10]
    for pow_ in n:
        exp = x ** pow_
        out = power(x, n=pow_)
        assert out == exp


def test_add():
    x = [1, 2, 3]
    y = [4, 5, 6]
    for i, j in zip(x, y):
        add(i, j)


def test_power_of_zero():
    x = 0.
    pow_ = 10
    exp = 0
    out = power(x, n=pow_)
    assert exp == out


def test_very_special_case():
    exp = 1
    out = power(0, n=0)
    assert exp == out


# test_power()
# test_add()
print power(5,5)
print power.__doc__
print power.__name__
# print power(5, 5)


