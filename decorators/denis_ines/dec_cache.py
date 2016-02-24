import pickle
import numpy as np

def cache(func):
    func._cached = {}
    def wrapper(*args, **kwargs):
        all_args = (args, kwargs)
        arg_hash = hash(pickle.dumps(all_args))
        if arg_hash in func._cached:
            print('using cached result')
            return func._cached[arg_hash]
        else:
            print('creating new cache entry')
            res = func(*args, **kwargs)
            func._cached[arg_hash] = res
            return res
    return wrapper


@cache
def sum(x,y, classobject, a=5, b=3):
    classobject.print_it()
    return x+y+a+b

class dummy(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def print_it(self):
        print('Hi!')

if __name__=='__main__':
    d = dummy(np.arange(10000), np.arange(30000))
    print('sum output:', sum(1,4,d,a=20))
    print('sum output:', sum(1,4,d,a=20))
    print('sum output:', sum(1,4,d,a=20))


