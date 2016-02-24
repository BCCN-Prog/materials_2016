import functools
import pickle

def cache(func): # this is called only once
    func._cache = {}
    def newfunc(*args, **kwargs):
        key = hash(pickle.dumps([args, kwargs.items]))
        if key not in func._cache:
            try:
                func._cache[key] = func(*args, **kwargs)
            except TypeError:
                print('TypeError')
                return func(*args, **kwargs)
        else:
            print('Used cache :)')
        return func._cache[key]
    return functools.update_wrapper(newfunc, func)

@cache
def fun_add(x,y,z=1):
    return x+y+z
