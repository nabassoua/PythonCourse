def reduction(n):
    
    if n<10:
        return 0
    elif n>=0 or n<50:
        return 0.1
    elif n>=50:
        return 0.2

def prix_livraison(prix):
    
    livraison = 0.1*prix
    
    if livraison < 5:
        return 5
    elif livraison >=5 or livraison <= 100:
        return livraison
    
def facture(n,p):
    print('Prix : {} $'.format(p))
    print('Reduction : -{} %'.format(n))
    print('Cout livraison : {} $'.format(prix_livraison(p)))
    print('---------------------------')
    print('Prix total(dont livraison) : {} $'.format(p-(p*reduction(n))+prix_livraison(p)))
    