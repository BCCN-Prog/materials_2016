import pickle
import numpy as np
import json
import pdb
import hashlib

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


def cache_to_file(func):
    def wrapper(*args, **kwargs):
        all_args = (args, kwargs)
        arg_hash = hashlib.md5(pickle.dumps(all_args)).hexdigest()
        print('hash', arg_hash)
        try:
            f = open('cached_{}_results'.format(func.__name__), 'r+')
            print('try1 works')
        except FileNotFoundError:
            f = open('cached_{}_results'.format(func.__name__), 'w')
            print('try1 does not work')
            #print('creating new file')

        try:
            print('try2 works')
            cached_data = json.load(f)
            f.close()
        except ValueError as e:
            print('try2 does not work', e)
            cached_data = {}
            f.close()

        if arg_hash in cached_data:
            print('using cached result')
            return cached_data[arg_hash]
        else:
            print('creating new cache entry')
            res = func(*args, **kwargs)
            cached_data[str(arg_hash)] = res
            print('cached data', cached_data)
            with open('cached_{}_results'.format(func.__name__), 'w') as f:
                json.dump(cached_data, f)
                f.flush()
        return res

    return wrapper


@cache
def sum(x,y, classobject, a=5, b=3):
    classobject.print_it()
    return x+y+a+b


@cache_to_file
def sum_file(x,y, classobject, a=5, b=3):
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
#    print('sum output:', sum(1,4,d,a=20))
#    print('sum output:', sum(1,4,d,a=20))
#    print('sum output:', sum(1,4,d,a=20))

    print('sum to file:', sum_file(1,4,d,a=20))
    #print('sum to file:', sum_file(4,4,d,a=20))



