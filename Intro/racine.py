import math as mth

def racine_carre(n):
    sol = mth.sqrt(n)
    print("Square root of {} is {} and therefore its integer part is {}".format(n,sol,int(sol)))
    