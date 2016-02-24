power_flag = True
add_flag = True

def deprecated(func):
    def newfunc1(*args, **kwargs):
        global power_flag
        if power_flag:
            print('Power function is deprecated')
            power_flag = False
        return func(*args, **kwargs)

    def newfunc2(*args, **kwargs):
        global add_flag
        if add_flag:
            print('Add function is deprecated')
            add_flag = False
        return func(*args, **kwargs)
    return newfunc1 if func.__name__ == "power" else newfunc2


@deprecated
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
    x = [1,2,3]
    y = [4,5,6]
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

test_power()
test_add()