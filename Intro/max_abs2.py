#from math import abs


def print_max_abs(x,y,msg):
    
    print(msg, end='') #end=' ' needed to ensure next output on the same line
    
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

#assert max_abs(2,-3)==-3
#assert max_abs(3,-3)==3