from maxima import find_maxima

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

