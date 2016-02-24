# Advanced Scientific Programming in Python
# Exercise 3


def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x, 
           if there is a maximum plateau, the last indice is returned.
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %d instead' % type(x)
        raise TypeError(message)

    idx = []
    deriv_pos = None
    if x[0] > x[1]: idx.append(0)
    for i in range(1,len(x)-1):
        # `i` is a local maximum if the signal decreases before and after it
        if x[i-1] < x[i]:
            deriv_pos = True
        if x[i-1] <= x[i] and x[i+1] < x[i] and deriv_pos:
            idx.append(i)
            deriv_pos = False
    if x[-1] > x[-2]:
        deriv_pos = True
    if x[-1] >= x[-2] and deriv_pos: idx.append(len(x)-1)
    return idx

    # NOTE for the curious: the code above could be written using
    # list comprehension as
    # return [i for i in range(len(x)) if x[i-1]<x[i] and x[i+1]<x[i]]
    # not that this would solve the bugs ;-)
