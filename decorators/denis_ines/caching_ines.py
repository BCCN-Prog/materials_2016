
def cache(func):
    func.cache = {}
    def new_func (*args, **kwargs):
        argl = get_arg_list (args, kwargs)
        arg_string = ','.join(map(str, argl)) 
        if func.cache == None :
            res = func(*args, **kwargs)
            func.cache[arg_string] = res
            return res
        if arg_string in func.cache:
            print('Same arguments have already been called, result was: ')
            #print(func.cache[arg_string])
            return func.cache[arg_string]
        else:
            res = func(*args, **kwargs)
            func.cache[arg_string] = res
            return res
    return new_func
        

def get_arg_list (args, kwargs):
    res = args
    ki = kwargs.keys()
    for k in ki:
        res.append(ki)
        res.append(kwargs[ki])
    return res

@cache
def power(x, n=1):
    """Return x^n (for natural numbers only!)"""
    y = x
    if n == 0:
        return 1
    for i in range(n-1):
        y = y*x
    return y
    
    
print(power(2,3))
print(power(3,3))
print(power(2,4))
print(power(2,3))
