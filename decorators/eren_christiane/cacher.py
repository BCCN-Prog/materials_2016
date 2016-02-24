function_name_to_params_and_results_map = {}

def cached(func):
    def newfunc(*args, **kwargs):
        if type(args[0]) == list:
            # print 'converting'
            args = tuple(args[0])

            if func.__name__ in function_name_to_params_and_results_map:
                params_to_results_map = function_name_to_params_and_results_map[func.__name__]
                if not (args in params_to_results_map):
                    params_to_results_map[args] = func(list(args), **kwargs)
                    print 'cache miss'
                return params_to_results_map[args]

            else:
                res = func(list(args), **kwargs)
                params_to_results_map = {args: res}
                function_name_to_params_and_results_map[func.__name__] = params_to_results_map
                print 'cache miss'
                return res

        if func.__name__ in function_name_to_params_and_results_map:
            params_to_results_map = function_name_to_params_and_results_map[func.__name__]
            if not (args in params_to_results_map):
                params_to_results_map[args] = func(*args, **kwargs)
                print 'cache miss'
            return params_to_results_map[args]

        else:
            res = func(*args, **kwargs)
            params_to_results_map = {args: res}
            function_name_to_params_and_results_map[func.__name__] = params_to_results_map
            print 'cache miss'
            return res


    return newfunc

@cached
def add(x,y):
    return x + y

@cached
def add_lists(ll):
    return sum(ll)

@cached
def mult(x,y, z):
    return x * y * z


add(5,5)
add(5,5)
add(3,3)
mult(3,3,4)
mult(3,3,4)

add_lists([1,2,3])
add_lists([1,2,3])