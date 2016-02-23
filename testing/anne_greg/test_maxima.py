from maxima import find_maxima

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
