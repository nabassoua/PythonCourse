from random import randint

def choix_ordi():
    
    selection = randint(1,3)
    
    if selection == 1:
        return 'pierre'
    elif selection == 2:
        return 'feuille'
    elif selection == 3:
        return 'ciseaux'
    

choix_ordinateur = choix_ordi()
    
    
choix=input('Quel est ton choix, humain ? ')
#print('Humain, tu as choisi {}'.format(choix))

if choix=='pierre' or choix=='feuille' or choix=='ciseaux':
    print('ok')
    print('humain: {}'.format(choix))
else:
    choix = choix_ordi()
    print('Choix incorrect, je choisis pour toi : {}'.format(choix))

print('Ordinateur: {}'.format(choix_ordinateur))

if choix_ordinateur=='pierre' and choix=='feuille':
    print('Vainqueur : ordinateur')
elif choix_ordinateur=='feuille' and choix=='pierre':
    print('Vainqueur : humain')    
elif choix_ordinateur=='pierre' and choix=='ciseaux':
    print('Vainqueur : ordinateur')       
elif choix_ordinateur=='ciseaux' and choix=='pierre':
    print('Vainqueur : humain')
elif choix_ordinateur=='ciseaux' and choix=='feuille':
    print('Vainqueur : ordinateur') 
elif choix_ordinateur=='feuille' and choix=='ciseaux':
    print('Vainqueur : humain')
else:
    print('Egalite')