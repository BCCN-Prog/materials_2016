from functools import update_wrapper
import numpy as np
import hashlib as hl
import pickle

#hl.md5(bal).hashdigest()

def deprecated2(arg): # decorator
    def deprecated(func):
        func._seen = False # underscore means do not touch (convention)
        def newfunc(*args, **kwargs): # *args: positional args; **kwargs: keyword (=named) args
            if not func._seen:
                print('This function is deprecated. Use %s instead.' %arg)
                func._seen = True
            return func(*args, **kwargs)
        update_wrapper(newfunc, func)
        return newfunc
    return deprecated
   
pre = []
results = []
def cache(func):
    #pre = []
    #results = []
    def newfunc(*args, **kwargs):
        n = func.__name__
        t = (n, args, kwargs)
        t = pickle.dumps(t)
        has = hl.md5(t).hexdigest()
        global pre
        global results
        if has in pre:
            i = pre.index(has)
            return results[i]
        else: 
            pre.append(has)
            result = func(*args, **kwargs)
            results.append(result)
            return result
    return newfunc
   
@deprecated2('math.pow')
def power(x, n = 1):
    """return x^n (for natural numbers only)"""
    y = x
    if n == 0:
        return 1
    for i in range(n-1):
        y = y*x
    return y

@cache
def add(x,y,z):
    return x+y+z

@cache    
def addv(x, y,z=1):
    assert type(x) == type(y)
    if type(x) is not np.array:
        return x+y+z
    else:
        p = np.ones(x.shape[0])*z
    return x+y+p

def test_power():
    x = 10
    p = [0, 1, 2, 10]
    for pow_ in p:
        exp = x**pow_
        out = power(x, n = pow_)
        assert out == exp

def test_power_of_zero():
    x = 0.
    pow_ = 10
    exp = 0
    out = power(x, n = pow_)
    assert exp == out
    
def test_very_special_case():
    exp = 1
    out = power(0, n = 0)
    assert exp == out
    
    
