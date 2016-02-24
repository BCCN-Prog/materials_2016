import numpy as np
from maxima_new import find_maxima_new

def test_simple_sequence():
    
    exp = [2, 4]
    lst = [1, 2, 3, 2, 4, 3, 2]
    out = find_maxima_new(lst)
    assert exp == out
    
def test_shorter_sequence():
    
    lst = [1, 2, 3, 2]
    out = find_maxima_new(lst)
    exp = [2]
    assert exp == out
    
def test_exercise_01():
    
    lst = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima_new(lst)
    exp = [2, 4]
    assert exp == out
    
def test_exercise_02():
    
    lst = [-i**2 for i in range(-3, 4)]
    out = find_maxima_new(lst)
    exp = [3]
    assert exp == out
    
def test_exercise_03():
    
    lst = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    out = find_maxima_new(lst)
    exp = [16, 78]
    assert exp == out
    
def test_exercise_04():
    
    lst = [4, 2, 1, 3, 1, 2]
    out = find_maxima_new(lst)
    exp = [0, 3rm ]
    assert exp == out
    
def test_exercise_05():
    
    lst = [4, 2, 1, 3, 1, 5]
    out = find_maxima_new(lst)
    exp = [0, 5]
    assert exp == out
    
def test_exercise_05():
    
    lst = [4, 2, 1, 3, 1]
    out = find_maxima_new(lst)
    exp = [0, 3]
    assert exp == out
    
def test_exercise_05():
    
    lst = [1, 2, 2, 1]
    out = find_maxima_new(lst)
    exp = [1, 2]
    assert exp == out
