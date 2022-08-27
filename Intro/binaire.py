def affiche_calc_binaire(n):
    
    
       
    while (n) >= 2:
        
        
        remainder = n%2
        quotient = n//2       
        print("{} car {} = {} x {} + {}".format(remainder,n,2,quotient,remainder))
        n = quotient
    
    print(n)
   
        