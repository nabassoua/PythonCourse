def affiche_calc_binaire(n):
    
    print(1,end=' ')
       
    while (n//2) >= 1:
        
        
        remainder = n%2
        quotient = n//2       
        print(remainder,end=' ')
        n = n//2
    
