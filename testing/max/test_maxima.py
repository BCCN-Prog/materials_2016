import numpy as np
from maxima import find_maxima

def test_simple_sequence():
    
    exp = [2, 4]
    x = [1, 2, 3, 2, 4, 3, 2]
    out = find_maxima(x)
    assert exp == out
    
def test_shorter_sequence():
    
    x = [1, 2, 3, 2]
    out = find_maxima(x)
    exp = [2]
    assert exp == out
    
def test_exercise_01():
    
    x = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima(x)
    exp = [2, 4]
    assert exp == out
    
def test_exercise_02():
    
    x = [-i**2 for i in range(-3, 4)]
    out = find_maxima(x)
    exp = [3]
    assert exp == out
