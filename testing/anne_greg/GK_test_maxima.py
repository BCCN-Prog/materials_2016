from maxima2 import find_maxima

def test_simple_sequence():
    exp = [2, 4]
    x = [1, 2, 3, 2, 4, 3]

    assert exp == find_maxima(x)

def test_shorter_sequence():
    exp = [2]
    x = [1, 2, 3]

    assert exp == find_maxima(x)
