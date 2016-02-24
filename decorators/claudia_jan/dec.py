import functools

def deprecate(func, instead): # this is called only once
    # thats why setting to false here does not effect the additional function calls
    func._called = False
    def newfunc(*args, **kwargs):
        if not func._called:
            func._called = True
            print('This function is deprecated, use ' + instead)
        return func(*args, **kwargs)
    # uses doc, name, and signature of original function see
    # documentation of update_wrapper
    return functools.update_wrapper(newfunc, func)

# do namechange to pass argument to decorator.
def deprecated(instead = 'None'):
    # partial calls function with additional arguments
    return functools.partial(deprecate, instead=instead)

@deprecated('math.power')
def power(x, n=1):
    """Return x^n (for natural numbers only!)"""
    y = x
    if n == 0:
        return 1
    for i in range(n-1):
        y = y*x
    return y

@deprecated()
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
