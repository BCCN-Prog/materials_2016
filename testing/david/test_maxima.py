from maxima import find_maxima


def test_simple_sequence():
    exp = [2, 4]
    x = [1, 2, 3, 2, 4, 3]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)


def test_shorter_sequence():
    exp = [2]
    x = [1, 2, 3]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)


def test_shorter_sequence2():
    exp = [0, 3, 5]
    x = [4, 2, 1, 3, 1, 5]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)


def test_shorter_sequence3():
    exp = [0, 3]
    x = [3, 2, 2, 3]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)


def test_shorter_sequence4():
    exp = [1]
    x = [1, 3, 2, 2, 1]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)


def test_shorter_sequence5():
    exp = [3]
    x = [1, 2, 2, 3, 1]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)

def test_shorter_sequence6():
    exp = [2,4]
    x = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)

def test_shorter_sequence7():
    exp = [2]
    x = [1, 2, 2, 1]
    out = find_maxima(x)
    assert exp == out, 'returns ' + str(out) + ' instead of ' + str(exp)