import random

cartes = [
    "2 ♠️","3 ♠️","4 ♠️","5 ♠️","6 ♠️","7 ♠️","8 ♠️","9 ♠️","10 ♠️","Valet ♠️","Reine ♠️","Roi ♠️","As ♠️",
    "2 ♦️","3 ♦️","4 ♦️","5 ♦️","6 ♦️","7 ♦️","8 ♦️","9 ♦️","10 ♦️","Valet ♦️","Reine ♦️","Roi ♦️","As ♦️",
    "2 ♥️","3 ♥️","4 ♥️","5 ♥️","6 ♥️","7 ♥️","8 ♥️","9 ♥️","10 ♥️","Valet ♥️","Reine ♥️","Roi ♥️","As ♥️",
    "2 ♣️","3 ♣️","4 ♣️","5 ♣️","6 ♣️","7 ♣️","8 ♣️","9 ♣️","10 ♣️","Valet ♣️","Reine ♣️","Roi ♣️","As ♣️"
    ]


# Croupier distribue 1 carte par joueur
# Croupier tire 1 carte
# Croupier distribue 1 carte par joueur

# Si Croupier obtient 10 ou As -> proposer aux joueurs une assurance
# Sinon proposer l'abandon
# Si joueur à 10 et As ET Croupier  -> gagné (x2,5)


cartes_tirees = []

def tirer(nb) :

    for _ in range(nb):
        
        randId = random.randint(0, len(cartes)-1)
        while randId in cartes_tirees:
            randId = random.randint(0, len(cartes)-1)
        cartes_tirees.append(randId)    
    return cartes[randId]
    
# Tirage des cartes

main_joueur = tirer(1)
main_croupier = tirer(1)
main_joueur = main_joueur + " | " + tirer(1)

print("Croupier :",main_croupier,"()")
print("Joueur :",main_joueur,"()")

# Input joueur

play = 1
valeur_cartes = 0

while (play == 1) :

    rep = input("Que voulez-vous faire ? (t = tirer une carte, d = doubler, a = abandonner, s = split, r = rester) ")

    if rep == "t" :

        print("tirer")
        main_joueur = main_joueur + " | " + tirer(1)
        
        print("Croupier :",main_croupier,"()")
        print("Joueur :",main_joueur,"()")

        if valeur_cartes > 21 :
            print("Busted ! (",valeur_cartes,")")
            play = 0

    if rep == "d" : 

        print("doubler")
        main_joueur = main_joueur + " | " + tirer(1)
        
        print("Croupier :",main_croupier,"()")
        print("Joueur :",main_joueur,"()")

        if valeur_cartes > 21 :
            print("Busted ! (",valeur_cartes,")")
        
        play = 0

    if rep == "a" :

        print("abandon")
        play = 0

    if rep == "s" :

        print("split")
        # au secours

    if rep == "r" :

        print("rester")
        play = 0

