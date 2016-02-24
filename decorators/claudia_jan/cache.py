import functools

def cache(func): # this is called only once
    func._cache = {}
    def newfunc(*args, **kwargs):
        sig = (args, kwargs)
        if sig not in func._cache:
            print('Used cache :)')
            func._cache[sig] = func(*args, **kwargs)
        return func._cache[sig]
    return functools.update_wrapper(newfunc, func)

@cache
def fun_add(x,y,z=1):
    return x+y+z
