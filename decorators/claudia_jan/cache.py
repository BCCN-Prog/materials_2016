import functools
import pickle
import hashlib

def cache(func):
    # this is called only once
    # try to open previous cache
    try:
        # we have a cache at disk
        func._cachefile = open(func.__name__+'_cache.pyc', 'rb+')
        # but use the memory cache for the current session
        func._cache = pickle.load(func._cachefile)
        func._cachefile.seek(0) # seek to top of file
        # check whether file changed, throw away cache if yes
        func_string = func.__code__.co_code + pickle.dumps(func.__code__.co_consts) + pickle.dumps(func.__code__.co_varnames)
        if not(func_string==func._cache[0]):
            func._cache = {}
            func._cache[0] = func_string
            print("Function changed, deleting cache!")

    # if there is no cache file, create one
    except FileNotFoundError:
        func._cachefile = open(func.__name__+'_cache.pyc', 'wb+')
        func._cache = {}
        func._cache[0] = func.__code__.co_code + pickle.dumps(func.__code__.co_consts) + pickle.dumps(func.__code__.co_varnames)
    # if file is empty
    except EOFError:
        func._cache = {}
        func._cache[0] = func.__code__.co_code + pickle.dumps(func.__code__.co_consts) + pickle.dumps(func.__code__.co_varnames)

    def newfunc(*args, **kwargs):
        # try to hash the signature. does not work for lambdas
        try:
            key = hashlib.md5(pickle.dumps([args, kwargs.items])).hexdigest()
        except pickle.PicklingError:
            print("Cant pickle the argument -> no caching. Used a lambda?!..Pfui!")
            return func(*args, **kwargs)
        # look for the signature in the cache
        if key not in func._cache:
            # save it in cache in memory, then write to disk.
            func._cache[key] = func(*args, **kwargs)
            pickle.dump(func._cache, func._cachefile)
            func._cachefile.seek(0)
            func._cachefile.flush()
        else:
            print('Used cache :)')
        # return cached result
        return func._cache[key]
    return functools.update_wrapper(newfunc, func)

@cache
def fun_add(x,y,z=1):
    return x+y+z

@cache
def fun_lamm(func, arg):
    return func(arg)
