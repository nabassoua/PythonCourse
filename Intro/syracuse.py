

def suivant(u):
    
    if u%2 == 0:
        return int(u/2)
    else:
        return (3 * u + 1)

def syracuse_rec(u):
    
    res = suivant(u)
    
    print(u,"-->", end=" ")
    
    if res == 1:
        print(1)
    else:
        syracuse_rec(res)

def syracuse_rec_while(u):
    
    print(u,"-->", end=" ")
    res = suivant(u)
    
    while res != 1:
        print(res,"-->", end=" ")
        res = suivant(res)
    print(1)
    
#output: 12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1