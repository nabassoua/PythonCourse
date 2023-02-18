def max_abs(x,y):
       
    if abs(y) > abs(x):
        return y
    elif abs(y) < abs(x):
        return x
    elif abs(x) == abs(y):
        if x > 0:
            return x
        else:
            return y

def print_max_abs(x,y,msg):
    print('{} {}'.format(msg,max_abs(x,y)))