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
    idx -- list of indices of the local maxima in x
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %d instead' % type(x)
        raise TypeError(message)

    idx = []
    i = 0
    while i < (len(x)-1):
        # `i` is a local maximum if the signal decreases before and after it
        if i==0:
            if x[i]>x[i+1]:
                idx.append(i)
        elif x[i] == x[i+1] and x[i]>x[i-1]:
            j=i+2
            while (j<len(x)):
                if x[i]==x[j]:
                    j=+1
                elif x[j]>x[i]:
                    idx.append(j)
                    i = j + 1
                    break
                else:
                    idx.append(i)
                    i = j + 1
                    break
        if i > (len(x)-2):
            break
            # we use <= so that for neighboring maxima the first occurence wins
        if x[i-1] < x[i] and x[i+1] <= x[i]:
            idx.append(i)
        i += 1

    if i == (len(x)-1):
        if x[i]>x[i-1]:
            idx.append(i)
    return idx

    # NOTE for the curious: the code above could be written using
    # list comprehension as
    # return [i for i in range(len(x)) if x[i-1]<x[i] and x[i+1]<x[i]]
    # not that this would solve the bugs ;-)
