# tets for decorator cache
import pickle
import cache

def test_simple():
    @cache.cache
    def f(x):
        return x+1
    print('Computes f(1)=2')
    f(1)
    print('Computes f(2)=3')
    f(2)
    print('Computes f(1)=2')
    f(1)

    print('Changing function, run again')
    @cache.cache
    def f(x):
        return x+2
    print('Computes f(1)=3')
    f(1)
    print('Computes f(2)=4')
    f(2)
    print('Computes f(1)=3')
    f(1)

    print('Undo changes, run again')
    @cache.cache
    def f(x):
        return x+1
    print('Computes f(1)=2')
    f(1)
    print('Computes f(2)=3')
    f(2)
    print('Computes f(1)=2')
    f(1)
