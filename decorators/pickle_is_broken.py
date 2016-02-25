import pickle
FNAME = 'pickle_is_broken.pic'

class A:
    attr = 10

    def save(self):
        fh = open(FNAME, 'wb')
        pickle.dump(self, fh)
        fh.close()

def test_saving():
    a = A()
    a.save()
    fh = open(FNAME, 'rb')
    b = pickle.load(fh)
    fh.close()
    assert a.attr == b.attr

def test_modify():
    a = A()
    a.attr = 100
    a.save()
    fh = open(FNAME, 'rb')
    b = pickle.load(fh)
    fh.close()
    assert a.attr == b.attr

def test_back_to_the_future():
    global A
    a = A()
    a.save()
    # years have passed
    class A:
        number = 10

    a = A()
    fh = open(FNAME, 'rb')
    b = pickle.load(fh)
    fh.close()
    assert a.number == b.attr
    assert a.number == b.number

