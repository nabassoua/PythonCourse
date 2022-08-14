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
    new_chaine = chaine
    for i in range(0,len(chaine)):
        if i%2 == 1:
            new_chaine[i]='*'
    return new_chaine   

user_texte = input("votre texte: ")
#detail_chaine(user_texte)
#affice_colonne(user_texte)
inser_star(user_texte)
