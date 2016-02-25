'''Python namespace play

    Usage:
        from stuff import x, what_is_x, change_x, really_change_x
        x
        what_is_x()
        change_x(55)
        x
        what_is_x()

        really_change_x([1,1,1,1,1])
        x
        what_is_x()
'''

x = [1,2,3]

def what_is_x():
    print(x)

def change_x(y):
    global x
    x.append(y)

def really_change_x(y):
    global x
    x = y
