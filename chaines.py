#Intro to list of caracters

def detail_chaine(chaine):
    
    """
    Renvoie: le texte ou la phrase donnés,le nombre de caractères contenus,
    le premier et le dernier caractères
    chaine:str

    """
    print(chaine)
    print(len(chaine))
    print("{}...{}".format(chaine[0],chaine[-1]))
        
def affice_colonne(chaine):
    
    """
    affiche les lettres d'une chaîne de caractères donnée par l'utilisateur ( une par ligne ).
    chaine:str

    """
    for i in range(0,len(chaine)):
        print(chaine[i])
        
def inser_star(chaine):
    
    """
    retourne une nouvelle chaîne construite sur la base de la première en insérant une astérisque entre chacune de ses lettres 

    """
    new_list = []
    for i in range(0,len(chaine)):
        new_list[i]=chaine[i]
    return new_list

def teste_lettre(chaine,car):
    
    """
     teste si une phrase contient une lettre

    """
    c_index = 0
    count = 0
    while c_index < len(chaine):
        if(chaine[c_index] == car):
            count += 1
        c_index += 1
    print("The letter {} appears {} times".format(car,count))
            
    

def palindrome(chaine):
    
    """
     retourne True si c'est un palindrome

    """
    current_index = len(chaine)-1
    for i in range(0,len(chaine)//2):
        if(chaine[i] == chaine[current_index]):
            current_index -= 1
        else:
            print("False")
            break
    
        
def ligne_star(n):
    
    """
     retourne une chaîne de caractères composée de n fois le symbole *.

    """
    for i in range(0,n):
        #need the option end=' ' so output is on 1 ligne horizontally
        print("*",end=' ')

def carre_star(n):
    
    """
     retourne une chaîne de caractères semblable à un carré d'étoiles de côté n.

    """
    for i in range(0,n):
        ligne_star(n)
        #need the line below so that there is no space in between the
        #successive outputs
        print('')

def triangle_star(n):
    
    """
     retourne une chaîne de caractères semblable à un triangle rectangle d'étoile

    """
    for i in range(0,n):
        ligne_star(n)
        #need the line below so that there is no space in between the
        #successive outputs
        print('')
        n -= 1
     
user_texte = input("votre texte: ")
#number = int(input("n: "))
#detail_chaine(user_texte)
#affice_colonne(user_texte)
#palindrome(user_texte)
#triangle_star(number)
teste_lettre(user_texte,'m')
