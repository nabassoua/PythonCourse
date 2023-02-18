#from math import abs


def max_abs(x,y):
    if abs(y) > abs(x):
        return y
    else:
        if abs(y) < abs(x):
            return x
        elif abs(x) == abs(y):
            if x > 0:
                return x
            else:
                return y

assert max_abs(2,-3)==-3
assert max_abs(3,-3)==3