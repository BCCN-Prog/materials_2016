from time import sleep
import numpy as np

def cache(func):

    def newfunc(*args, **kwargs):
        identifier = str([arg for arg in args] + [(kwarg, kwargs[kwarg]) for kwarg in kwargs])
        #print identifier
        if not hasattr(func, 'dict'):
            func.dict = {}
        if identifier in func.dict:
            return func.dict[identifier]
        else:
            result = func(*args, **kwargs)
            func.dict[identifier] = result
            return result

    return newfunc

@cache
def identity(x, y=1):
    sleep(2)
    return x, y


print(identity(8))
print(identity(8))

print(identity(8,y=1))

print(identity(8,2))
print(identity(8,2))
print(identity(8,2))

x = np.array([1,2,3,4])
print(identity(x,x))
print(identity(x,x))
print(identity(x,x))
