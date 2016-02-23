# Advanced Scientific Programming in Python
# Exercise 3

import numpy as np


def check_maxima(d, negative_indices):
    maximas = []
    for i in negative_indices:
        index_before = i-1
        if d[index_before] > 0:
            maximas.append(i)
        if d[index_before] < 0:
            continue
        while d[index_before] == 0 and index_before>1:
            index_before -= 1
            if d[index_before] > 0:
                maximas.append(i)
            if d[index_before] < 0:
                break
    return maximas


def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %d instead' % type(x)
        raise TypeError(message)

    if len(x) == 1:
        return [0]

    d = np.hstack((0,np.diff(x)))
    negative_indices = np.where(d<0)[0]
    # is_maxima = (negative_indices - 1 >= 0)
    maxima = (np.array(check_maxima(d, negative_indices)) -1).tolist()
    # maxima = (maxima - 1).tolist()
    if d[-1] > 0:
        maxima.append(len(x)-1)
    if d[1] < 0:
        maxima.append(0)
    return sorted(maxima)
