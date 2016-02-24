from functools import update_wrapper
import numpy as np
import hashlib as hl
import pickle
import os

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
def cache(func): # original working version of cache, does not save to disk
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
    
def cache2(func): # cache version 2, saves to disk
    def newfunc(*args, **kwargs):
        n = func.__name__
        t = (n, args, kwargs)
        t = pickle.dumps(t)
        has = hl.md5(t).hexdigest()
        global pre
        global results
        loadFromDisk()
        if has in pre:
            i = pre.index(has)
            print('cache')
            return results[i]
        else: 
            pre.append(has)
            result = func(*args, **kwargs)
            results.append(result)
            saveToDisk()
            print('no cache')
            return result
    return newfunc

def saveToDisk():
    f = open('cache', 'wb')
    global pre
    global results
    pickle.dump((pre, results), f)
    f.close()
    
def loadFromDisk():
    f = open('cache', 'rb+')
    global pre
    global results
    try:
        pic = pickle.load(f)
    except EOFError:
        return
    pre = pic[0]
    results = pic[1]
    f.close()
    
    
def cachedisk(func): # does not work
    def newfunc(*args, **kwargs):
        f = open('cache', 'rb+')
        n = func.__name__
        t = (n, args, kwargs)
        t = pickle.dumps(t)
        has = hl.md5(t).hexdigest()       
        resultSaved = False
        try:
            f.seek(0)
            for l in f:
                print("asd")
                tup = pickle.load(f)
                print(tup)
                if tup[0] == has:
                    print('asd')                
                    resultSaved = True
                    f.close()
                    print('yes')
                    return tup[1]
        except EOFError:
            pass
        if not resultSaved:
            result = func(*args, **kwargs)
            pickle.dump((has, result), f) 
            f.close()
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

@cache2   
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
    
    
