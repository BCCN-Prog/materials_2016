from maxima import find_maxima

def test_simple_sequence():
    exp = [2,4]
    x = [1, 2, 3, 2, 4, 3]
    out = find_maxima(x)
    assert exp == out
def test_short_sequence():
    x = [1,2,3]
    out = find_maxima(x)
    exp = [2]
    assert exp == out

def test_neighbors():
    x = [1, 2, 2, 1]
    out = find_maxima(x)
    exp = [1]
    assert exp == out

def test_neighbors2():
    x = [1, 2, 2, 3, 1]
    out = find_maxima(x)
    exp = [3]
    assert exp == out
