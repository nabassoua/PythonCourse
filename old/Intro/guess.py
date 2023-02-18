from random import randint

comp_guess = randint(0,100)
print(comp_guess)
human_guess = int(input('Choose a number between 0 and 100: '))
prix_iters(7,human_guess)

def prix_iters(n,prix):
    
    current_prix = prix_trials(prix)
    
    if prix == current_prix:
        return True
    else:
        return prix_iters(n-1,prix) or False

def prix_trials(prix):
    
    if prix == comp_guess:
        print('Your guess is correct!')
    elif prix < comp_guess:
        print('Your guess is too small. Try a bigger number!')
    else: 
        print('Your guess is too big. Try a smaller number!')


    

    
                  