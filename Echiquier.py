import abc
from Pieces import *
#jeu d'echec à rendre pour le 21/01
class Table :
    def __init__(self) :
        self.__lettre_vers_emplacement = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f' : 5, 'g' : 6, 'h' : 7}
        self.feuille = []
        self.liste_piece = []
        #les pions
        for le in "abcdefgh":
            self.liste_piece.append(pion(le,7,1))
            self.liste_piece.append(pion(le,2,0))
        #les tours
        self.liste_piece.append(tour('a',8,1))
        self.liste_piece.append(tour('h',8,1))
        self.liste_piece.append(tour('a',1,0))
        self.liste_piece.append(tour('h',1,0))
        #les fous
        self.liste_piece.append(fou('c',8,1))
        self.liste_piece.append(fou('f',8,1))
        self.liste_piece.append(fou('c',1,0))
        self.liste_piece.append(fou('f',1,0))
        #les chevalier
        self.liste_piece.append(chevalier('b',8,1))
        self.liste_piece.append(chevalier('g',8,1))
        self.liste_piece.append(chevalier('b',1,0))
        self.liste_piece.append(chevalier('g',1,0))
        #les reines
        self.liste_piece.append(dame('d',8,1))
        self.liste_piece.append(dame('d',1,0))
        #les rois
        self.liste_piece.append(roi('e',8,1))
        self.liste_piece.append(roi('e',1,0))
        #on va les placer
        self.mise_a_jour()

    def test_des_deplacement(self):
        print(self)
        while True :
            print("Continuer ?")
            n = input()
            if n == '1':
                break
            self.deplacement(True)
            self.mise_a_jour()
            print(self)
            self.deplacement(False)
            self.mise_a_jour()
            print(self)


#Gaëtan a rajouté/modifié :

    def colision(self, indice, coup) :
        #renvois : colision ? même camp ? coordonnée si adversaire
        Chemin = self.liste_piece[indice].chemin(coup[1],int(coup[2]))
        for indice_case in range(len(Chemin)) :
            for indice_piece in range(32):
                if indice_piece == indice :
                    continue
                if self.liste_piece[indice_piece].vie and self.liste_piece[indice_piece].moi(Chemin[indice_case][0], Chemin[indice_case][1]) :
                    if self.liste_piece[indice_piece].get_couleur() == self.liste_piece[indice].get_couleur():
                        #colision avec pièce de même faction
                        return [True, True]
                    else:
                        #colision avec pièce adverse à la case donnée
                        return [True, False, indice_piece, Chemin[indice_case]]
        #aucune colision
        return [False]
      
    def deplacement(self, Joueur_blanc):
        
        while True :
            Liste_indice = []
            Liste_indice_pion_supp = []
            while Liste_indice == [] and Liste_indice_pion_supp == [] :
                print("Veuillez noter votre prochain coup")
                Coup = Lire(Joueur_blanc)
                Liste_indice = self.select(Coup)
                Liste_indice_pion_supp = self.select_poin_attaque(Coup)
                
            #print(self.liste_piece[Liste_indice[0]].get_coordonnee())

            Liste_indice_valide = []
            if not Liste_indice == [] :
                for indice in Liste_indice:
                    Colision = self.colision(indice, Coup)
                    if Colision[0] :
                        if not Colision[1] and not Coup[0] in 'Pp':
                            Liste_indice_valide.append([indice, Colision[2], Colision[3]])
                    else :
                        Liste_indice_valide.append([indice])

            
            if not Liste_indice_pion_supp == [] :
                for indice in Liste_indice_pion_supp:
                    Colision = self.colision(indice, Coup)
                    if Colision[0] :
                        if not Colision[1] :
                            Liste_indice_valide.append([indice, Colision[2], Colision[3]])


            if len(Liste_indice_valide) == 0 :
                print("Ce coup est impossible, aucune pièce ne peut le réaliser")
                continue
            elif len(Liste_indice_valide) > 1 :
                print("Ce coup peut être fait avec plusieurs pieces")
                #Liste_indice_valide = lire choix de la pièce

            if len(Liste_indice_valide[0]) > 1 :
                self.liste_piece[Liste_indice_valide[0][1]].pris()
                self.liste_piece[Liste_indice_valide[0][0]].nouvelle_position(Liste_indice_valide[0][2][0], int(Liste_indice_valide[0][2][1]))
            else  :
                self.liste_piece[Liste_indice_valide[0][0]].nouvelle_position(Coup[1],int(Coup[2]))
            break
            

    def mise_a_jour(self):
        #on réécrit la representation de la table à chaque mise à jour
        self.feuille = []
        for i in range(0 ,8):
            self.feuille.append([])
            for j in range(0 ,8):
                self.feuille[i].append(' ')
        for la_piece in self.liste_piece :
            if la_piece.vie :
                emplacement_codee = la_piece.get_coordonnee() 
                emplacement_decodee = [emplacement_codee["nombre"] -1 , self.__lettre_vers_emplacement[emplacement_codee["lettre"]]]
                self.feuille[emplacement_decodee[0]][emplacement_decodee[1]] = la_piece.get_symbole()

    def select_poin_attaque(self, coup) :
        avancer=[]
        if coup[0]== 'P' :
            for nombre in [1,3,5,7,9,11,13,15] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'attaque' : 
                    avancer.append(nombre)

        elif coup[0]== 'p' :
            for nombre in [0 ,2 ,4,6,8,10,12,14] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'attaque' : 
                    avancer.append(nombre)
        return avancer        

    def select(self, coup) : 

        avancer=[]
        if coup[0]== 'P' :
            for nombre in [1,3,5,7,9,11,13,15] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'p' :
            for nombre in [0 ,2 ,4,6,8,10,12,14] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'T' :
            for nombre in [18,19] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 't' : 
            for nombre in [16,17] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'F' :
            for nombre in [22,23] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'f' :
            for nombre in [20,21] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'C' : 
            for nombre in [26,27] : 
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'c'  : 
            for nombre in [25,24] : 
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'D' : 
            for nombre in [29] :
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'd' : 
            for nombre in [28] : 
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)


        elif coup[0]== 'R' : 
            for nombre in [31] : 
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)

        elif coup[0]== 'r' : 
            for nombre in [30] : 
                retourner=self.liste_piece[nombre].mouvement(coup[1], int(coup[2]))
                if retourner== 'avance' : 
                    avancer.append(nombre)
                    
        return avancer

#Pas touché :
    def __repr__(self) :
      
        print("  a | b | c | d | e | f | g | h |")
        for i in range(7 ,-1,-1):
            print("-"*32)
            
            print(int(i+1),end="|")
            for j in range(0,8):
                item = self.feuille[i][j] 
                print(str(item)+' |', end = " ")
            print()
        print("-"*32)
        return ''


"""
test = Table()
print(test)
"""