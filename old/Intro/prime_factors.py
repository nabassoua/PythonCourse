def is_prime(n):
    
    i = 2
    prime = True
    
    while i<=n//2:
        
        rem = n%i
        
        if rem != 0:
            i += 1
        else:
            return not prime
        
    return prime   
    
def list_prime(x):
    
    j = 2
    
    while j <= x:
        if is_prime(j):
            print(j)
            j += 1
        else:
            j += 1


    
    
    
    
        