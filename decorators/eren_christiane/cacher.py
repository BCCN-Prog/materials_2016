import pickle
import hashlib
import numpy as np


function_name_to_params_and_results_map = {}

CACHE_FILENAME = 'pickle_of_pickles.pkl'


def meta_cached(func):
    def load_cache():
        try:
            global function_name_to_params_and_results_map
            f = open(CACHE_FILENAME, "rb")
            function_name_to_params_and_results_map = pickle.load(f)
            f.close()
            # print('loaded')
            print function_name_to_params_and_results_map
        except:
            print('No pickles found.')

    load_cache()
    return func


def get_code(func):
    return func.__code__.co_code + str(func.__code__.co_consts)


@meta_cached
def cached(func):
    def newfunc(*args, **kwargs):
        hash_of_args = hashlib.md5(pickle.dumps(args)).hexdigest()
        code = get_code(func)
        if code in function_name_to_params_and_results_map:
            params_to_results_map = function_name_to_params_and_results_map[code]
            if not (hash_of_args in params_to_results_map):
                params_to_results_map[hash_of_args] = func(*args, **kwargs)
                print('cache miss')
            save_cache()
            return params_to_results_map[hash_of_args]

        else:
            res = func(*args, **kwargs)
            params_to_results_map = {hash_of_args: res}
            function_name_to_params_and_results_map[code] = params_to_results_map
            print('cache miss')
            save_cache()
            return res

    return newfunc


def save_cache():
    f = open(CACHE_FILENAME, "wb")
    pickle.dump(function_name_to_params_and_results_map, f)
    f.flush()
    # print(function_name_to_params_and_results_map)


@cached
def add(x, y):
    return x + y + 3


@cached
def add_lists(ll):
    return sum(ll)


@cached
def mult(x, y, z):
    return x * y * z


@cached
def add_lists_np(ll):
    return np.sum(ll)


@cached
def take5(func):
    return func(5)


add(5, 5)
add(5, 5)
add(3, 3)
mult(3, 3, 4)
mult(3, 3, 4)


#
# add_lists([1,2,3])
# add_lists([1,2,3])
#
# print 'np'
# add_lists_np(np.ones((1,5)))
# add_lists_np(np.ones((1,5)))

# def multiply_by_two(x): return 3 * x


# multiply_by_two = lambda x: 2*x

# take5(multiply_by_two)
# take5(multiply_by_two)

