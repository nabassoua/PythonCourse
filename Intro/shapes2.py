def etoile():
    print('*',sep='',end='')
    
def diese() :
    print('#', sep='',end='')
    
def nouvelle_ligne() :
    print()

def tapis_2(l,h):
    
    i = 0
    
    
    while i<l:
        j = 0
        while j<h//2:
            etoile()
            diese()
            j += 1
        if h%2 == 1:
            etoile()
        nouvelle_ligne()
        i += 1
            
        
   
 