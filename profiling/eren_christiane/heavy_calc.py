def f(x):
    long_ = range(10**x)
    y = []
    for idx in long_:
        y.extend([idx*2])
    return y

def g(y):
    z = []
    for idx in f(y):
        z.append(idx/2)
    return z

pow = 5

a = g(pow)

