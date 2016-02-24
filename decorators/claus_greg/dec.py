import functools

def deprecated(func):
    # if not hasattr(deprecated, 'dict'):
        # deprecated.dict={}
    # deprecated.dict[func.__name__]=False
    func._seen = False

    def newfunc(*args, **kwargs):
        # if not deprecated.dict[func.__name__]:
            # print('This function is deprecated')
            # deprecated.dict[func.__name__] = True
        if not func._seen:
            print('This function is deprecated')
            func._seen = True
        return func(*args, **kwargs)
    functools.update_wrapper(newfunc, func)
    return newfunc

@deprecated
def power(x, n=1):
    """Return x^n (for natural numbers only!)"""
    y = x
    if n == 0:
        return 1
    for i in range(n-1):
        y = y*x
    return y

@deprecated
def add(x, y, z):
    return x + y + z

def test_power():
    x = 10.
    p = [0, 1, 2, 10]
    for pow_ in p:
        exp = x**pow_
        out = power(x, n=pow_)
        assert out == exp

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

for i in range(10):
    print(power(i, 2))
    print(add(i, i, i))

print(power.__doc__)
