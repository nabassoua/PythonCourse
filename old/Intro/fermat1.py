def fermat(n):
    
    return (2**(2**n)) + 1


def premier_facteur(n):
    
    diviseur = 2
    
    while n%diviseur != 0:
        diviseur += 1
    
    return diviseur

