
#dep_funs = []
from functools import update_wrapper

import pdb

#def deprecated(better_f = ''):
#    if better_f == '':
#        def new_func(*args, **kwargs):
#            if not func._seen:
#                 print('The following function is deprecated:')
#                 print(func)
#                 print('Use ' + better_f + ' instead!')
#                 func._seen = True
#                #dep_funs.append(func)
#            return func(*args, **kwargs)
#            update_wrapper(new_func, func)
#        return new_func
#    else:
#        def real_dec (func):
#            func._seen = False
#            def new_func(*args, **kwargs):
#                if not func._seen:
#                     print('The following function is deprecated:')
#                     print(func)
#                     print('Use ' + better_f + ' instead!')
#                     func._seen = True
#                     #dep_funs.append(func)
#                return func(*args, **kwargs)
#            update_wrapper(new_func, func)
#            return new_func
#        return real_dec

def deprecated (better_f = 'another function'):
    def real_dec (func):
        func._seen = False
        def new_func(*args, **kwargs):
            if not func._seen:
                print('The following function is deprecated:')
                print(func)
                #if not better_f == '':
                print('Use ' + better_f + ' instead!')
                func._seen = True
                #dep_funs.append(func)
            return func(*args, **kwargs)
        update_wrapper(new_func, func)
        return new_func
    return real_dec


@deprecated('math.pow')
def power(x, n=1):
    """Return x^n (for natural numbers only!)"""
    y = x
    if n == 0:
        return 1
    for i in range(n-1):
        y = y*x
    return y

@deprecated('+')
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
    
print (power (3,2))
print (power (3,3))
print (add (3,3,3))
print (add (3,2,3))


    
