def affiche_calc_binaire(n):
          
    while (n) >= 2:
        
        
        remainder = n%2
        quotient = n//2       
        print(remainder, end=' ')
        n = quotient
    
    print(n)
   
        