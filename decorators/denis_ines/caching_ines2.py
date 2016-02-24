import pickle
from functools import update_wrapper

def cache(func):
    cash = {}
    na = func.__name__
    dump_str = 'pickle.dump(cash, open("' + na +'.p",  "wb"))'
    print (dump_str)
    print (type(dump_str))
    load_str='cash2 = pickle.load(open("' +na+ '.p", "rb+"))'
    eval(dump_str)
    def new_func (*args, **kwargs):
        argl = get_arg_list (args, kwargs)
        arg_string = ','.join(map(str, argl)) 
        exec(load_str)
        if cash == None :
            res = func(*args, **kwargs)
            cash[arg_string] = res
            eval(dump_str)
            return res
        if arg_string in cash:
            print('Same arguments have already been called, result was: ')
            #print(func.cache[arg_string])
            return cash[arg_string]
        else:
            res = func(*args, **kwargs)
            cash[arg_string] = res
            exec(dump_str)
            return res
    update_wrapper(new_func, func)
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
