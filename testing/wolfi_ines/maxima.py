# Advanced Scientific Programming in Python
# Exercise 3
#The pink stuff directly unter the header is the doc string, so it can be read in the help
    #what does the function do? --> as a comment, not as description
    #Examples
    #Input arguments (if specific is required)
    #Output, and what type they should be 
import numpy as np

def find_maxima(x, edges = True):

    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
    x -- 1D list of real numbers
    edges: local maxima on the edges included?

    Output:
    idx -- list of indices of the local maxima in x
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %d instead' % type(x)
        raise TypeError(message)

    idx = []
    

    
    if not edges:
        if len(x) < 3:
            return []
        else:
            for i in range(1, len(x)-1):
        # `i` is a local maximum if the signal decreases before and after it
                if x[i-1] < x[i] and x[i+1] < x[i]:
                    idx.append(i)
            return idx
            
        
    else:   
        if len(x) < 2:
            idx = [1]
        else:
            a = x[1]
            b = x[-2]
            x = [a]+x+[b]
            xd = np.diff(x)
            for i in range(1,len(x)-1):
                # `i` is a local maximum if the signal decreases before and after it
                if x[i-1] < x[i] and x[i+1] < x[i]:
                    idx.append(i-1)
                if x[i-1] < x[i] and x[i+1] == x[i]:
                    xdd = xd[i:]
                    xdd = xdd[np.nonzero(xdd)]
                    if len(xdd)>0:
                        if xdd[0] <1:
                            idx.append(i-1)          
            if x[0] == x[1]:
                xd = np.diff(x)
                xdd = xd[np.nonzero(xd)]
                if len(xdd)>0:
                    if xdd[0] <1:
                        idx = [0] + idx
        
        return idx

    # NOTE for the curious: the code above could be written using
    # list comprehension as
    # return [i for i in range(len(x)) if x[i-1]<x[i] and x[i+1]<x[i]]
    # not that this would solve the bugs ;-)
