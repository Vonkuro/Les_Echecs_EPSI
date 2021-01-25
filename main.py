from Echiquier import *
from Pieces import *

def Partie():
    print("Une nouvelle partie d'echec.")
    echiquier = Table()
    print(echiquier)
    tour_blanc = False
    while echiquier.Echec(tour_blanc):
        if  not tour_blanc :
            print("Les blancs avec leur pièces en Majuscules")
            tour_blanc = True
        else:
            print("Les noirs avec leur pièces en Minuscules")
            tour_blanc = False
        echiquier.deplacement(tour_blanc)
        echiquier.mise_a_jour()
        print(echiquier)


Partie()