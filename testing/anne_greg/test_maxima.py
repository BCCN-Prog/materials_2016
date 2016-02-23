from maxima import find_maxima
import numpy as np

def test_simple_sequence():
    x = [1, 2, 3, 2, 4, 3]
    out = find_maxima(x)
    exp = [2, 4]
    print(out)
    assert exp == out
    
def test_shorter_sequence():
    x = [1, 2, 3]
    out = find_maxima(x)
    exp = [2]
    print(out)
    assert exp == out
    
def test_symmetric_sequence():
    x = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima(x)
    exp = [2, 4]
    print(out)
    assert exp == out
    
def test_square():
    x = [-i**2 for i in range(-3, 4)] #-9, -4, -1, 0, -1, -4, -9
    out = find_maxima(x)
    exp = [3]
    print(out)
    assert exp == out

def test_sine():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    out = find_maxima(x)
    exp = [16, 78]
    print(out)
    assert exp == out

def test_more_sequences():
    x = [4, 2, 1, 3, 1, 2]
    out = find_maxima(x)
    exp = [0, 3, 5]
    print(out)
    assert exp == out
    
    x = [4, 2, 1, 3, 1, 5]
    out = find_maxima(x)
    exp = [0, 3, 5]
    print(out)
    assert exp == out
   
    x = [4, 2, 1, 3, 1]
    out = find_maxima(x)
    exp = [0, 3]
    print(out)
    assert exp == out
