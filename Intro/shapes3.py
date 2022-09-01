def etoile():
    print('*',sep='',end='')
    
def diese() :
    print('#', sep='',end='')
    
def nouvelle_ligne() :
    print()

def tapis_3(l,h):
    
    i = 0
    
    while i<l:
        j = 0
        while j<h//2:
             if i%2 == 0:
                 etoile()
                 diese()
             else:
                 diese()
                 etoile()
             j += 1
        if h%2 == 1:
            if i%2 == 0:
                etoile()
            else:
                diese()
        nouvelle_ligne()
        i += 1
    
 