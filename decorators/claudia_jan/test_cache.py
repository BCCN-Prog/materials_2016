# tets for decorator cache
import pickle
import cache

def test_simple():
    @cache.cache
    def f(x):
        return x+1
    f(1)
    f(2)
    f(1)

    print('Changing function, run again')
    @cache.cache
    def f(x):
        return x+2
    f(1)
    f(2)
    f(1)
