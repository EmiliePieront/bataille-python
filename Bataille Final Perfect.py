import random
#Mes tableaux ==============================================================

tab1 = {
    "2 coeur": 2,
    "3 coeur": 3,
    "4 coeur": 4,
    "5 coeur": 5,
    "6 coeur": 6,
    "7 coeur": 7,
    "8 coeur": 8,
    "9 coeur": 9,
    "10 coeur": 10,
    "Valet coeur": 11,
    "Dame coeur": 12,
    "Roi coeur": 13,
    "As coeur": 14,
    "2 trèfle": 2,
    "3 trèfle": 3,
    "4 trèfle": 4,
    "5 trèfle": 5,
    "6 trèfle": 6,
    "7 trèfle": 7,
    "8 trèfle": 8,
    "9 trèfle": 9,
    "10 trèfle": 10,
    "Valet trèfle": 11,
    "Dame trèfle": 12,
    "Roi trèfle": 13,
    "As trèfle": 14,
    "2 carreaux": 2,
    "3 carreaux": 3,
    "4 carreaux": 4,
    "5 carreaux": 5,
    "6 carreaux": 6,
    "7 carreaux": 7,
    "8 carreaux": 8,
    "9 carreaux": 9,
    "10 carreaux": 10,
    "Valet carreaux": 11,
    "Dame carreaux": 12,
    "Roi carreaux": 13,
    "As carreaux": 14,
    "2 pique": 2,
    "3 pique": 3,
    "4 pique": 4,
    "5 pique": 5,
    "6 pique": 6,
    "7 pique": 7,
    "8 pique": 8,
    "9 pique": 9,
    "10 pique": 10,
    "Valet pique": 11,
    "Dame pique": 12,
    "Roi pique": 13,
    "As pique": 14,
}
tabMirroir = {}
#Mes sous programmes =========================================================
def ecranNoir():
    print("\n\n\n\n")

def jouerGame(tabMirroir):
    carte1 = random.choice(list(tabMirroir))
    carte2 = random.choice(list(tabMirroir))
    while carte1 == carte2:
        carte1 = random.choice(list(tabMirroir))
    input("Appuyer sur 1 touche pour jouer une carte!\n\n")
    return carte1, carte2

def lancerUneCarte(carte1, carte2):
    print("Vous jouez :")
    print(carte1)
    print("L'ordinateur joue :")
    print(carte2)

def calculDesPoints(carte1, carte2, tabMirroir, compteurPoint):
    if tabMirroir[carte1] > tabMirroir[carte2]:
        print("C'est gagné")
        compteurPoint += 2
    elif carte1 == carte2:
            print("Bataille!!!")
            jouerGame(tabMirroir)
            if tabMirroir[carte1] > tabMirroir[carte2]:
                print("C'est gagné")
                compteurPoint += 4
            else:
                print("C'est perdu")
    else:
        print("C'est perdu")
    del tabMirroir[carte2], tabMirroir[carte1]
    return compteurPoint, tabMirroir

def finDePartie(compteurPoint):
    if compteurPoint > 26:
        print("C'est Gagné ! Vous avez : ", compteurPoint, "cartes, et l'ordinateur : ", 52 - compteurPoint)
    elif compteurPoint == 26:
        print("Egalité ;) Vous avez chacun 26 cartes.")
    else:
        print("C'est perdu ! L'ordinateur a ", 52 - compteurPoint, "cartes, et vous : ", compteurPoint)

def rejouerJeu():
    rejouer = (input("Vous voulez rejouer? 1 Pour Oui, 0 Pour non"))
    if rejouer == "1":
        envieJouer = True
    else:
        envieJouer = False
    return envieJouer
#Main code ==================================================================

compteurPoint = 0
envieJouer = True
while envieJouer == True:
    for i in range(0, len(tab1)):
        tabMirroir.update(tab1)
    compteur = 0
    while compteur < 26:
        carte1, carte2 = jouerGame(tabMirroir)
        lancerUneCarte(carte1, carte2)
        compteurPoint, tabMirroir = calculDesPoints(carte1, carte2, tabMirroir, compteurPoint)
        compteur += 1
        ecranNoir()
    finDePartie(compteurPoint)
    envieJouer = rejouerJeu()
print(envieJouer)


