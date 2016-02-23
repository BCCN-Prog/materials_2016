from maxima import find_maxima
import numpy as np

def test_simple_sequence():
    expected = [2,4]
    x = [1,2,3,2,4,3]
    output = find_maxima(x)
    assert output == expected

def test_shorter_sequence():
    x = [1,2,3]
    exp = [2]
    out = find_maxima(x)
    assert out == exp, 'expected {}, but got {}'.format(exp, out)

def test_3():
    x = [0, 1, 2, 1, 2, 1, 0]
    exp = [2,4]
    out = find_maxima(x)
    assert out == exp

def test_4():
    x = [-i**2 for i in range(-3, 4)]
    exp = [3]
    out = find_maxima(x)
    assert out == exp

def test_5():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    exp = [16, 78]
    out = find_maxima(x)
    assert out == exp


def test_6():
    x = [4, 2, 1, 3, 1, 2]
    exp = [0, 3, 5]
    out = find_maxima(x)
    assert out == exp, 'expected {}, but got {}'.format(exp, out)

def test_7():
    x = [4, 2, 1, 3, 1, 5]
    exp = [0, 3, 5]
    out = find_maxima(x)
    assert out == exp, 'expected {}, but got {}'.format(exp, out)
