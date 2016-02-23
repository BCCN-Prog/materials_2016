from maxima import find_maxima
import numpy as np

def test_simple_sequence():
    x=[4,5,9,7,8,9,1]
    exp=[2,5]
    out=find_maxima(x)
    assert exp==out

def test_shorter_sequence():
    x=[4,2,1,3,1,2]
    exp=[3]
    out=find_maxima(x)
    assert exp==out
    
def test_squares():
    x=[-(i**2) for i in range(-3,4)]
    exp=[3]
    out=find_maxima(x)
    assert exp==out

#def test_sin():
#    x=[np.sin(2*alpha) for alpha in np.linspace(0.0,5.0,100)]
 #   out=find_maxima(x)
 #   print(out)
 
def test_repeated_max():
    x=[1,2,2,1]
    exp=[1,2]
    out=find_maxima(x)
    assert exp==out
    
def test_jumping():
    x=[4,2,1,3,1,5]
    exp=[3]
    out=find_maxima(x)
    assert exp==out
 
   

    


