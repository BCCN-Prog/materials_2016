from functools import wraps

class deprecated(object):
    def __init__(self, *args):
        assert len(args)<=1, 'Too many arguments in deprecated decorator!'
        if callable(args[0]):
            self.use = None
            self.func = args[0]
        else:
            self.use = args[0]
            self.func = args[1]
        self._seen = True
    def __call__(self):
        @wraps(self.func)
        def newfunc(*args, **kwargs):
            if not self._seen and self.use:
                print('This function is deprecated! Use {} instead.'.format(self.use))
                self._seen = True
            elif not self._seen:
                print('This function is deprecated!')
                self._seen = True
            return func(*args, **kwargs)
        return newfunc

@deprecated('math.pow')
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
    
#print (power (3,2))
#print (power (3,3))


    
