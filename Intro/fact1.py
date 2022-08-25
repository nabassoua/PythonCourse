def fac(n):
    
    prod=1
    i=2
    
    while i<=n:
        
        prod = prod * i
        i += 1
    
    return prod

def affich_fac(n):
    
    i=1
    while i<=n:
    
        print("{}! = {}".format(i,fac(i)))
        i+=1
