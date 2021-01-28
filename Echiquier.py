import abc
from Pieces import *
import Global

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

    def Echec(self, Joueur_blanc):
        if Joueur_blanc:
            return self.liste_piece[30].vie
        else :
            return self.liste_piece[31].vie



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
                Coup = self.Coup_Mat(Joueur_blanc)
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
                Liste_indice_valide = [self.doute(Liste_indice_valide)]

            if len(Liste_indice_valide[0]) > 1 :
                self.liste_piece[Liste_indice_valide[0][1]].pris()
                self.liste_piece[Liste_indice_valide[0][0]].nouvelle_position(Liste_indice_valide[0][2][0], int(Liste_indice_valide[0][2][1]))
            else  :
                self.liste_piece[Liste_indice_valide[0][0]].nouvelle_position(Coup[1],int(Coup[2]))
            break

    def trouve(self, lettre, nombre):
        indice = None
        for i in range(0 , 32): 
            element=self.liste_piece[i].get_coordonnee()
            lettre_decodee = self.__lettre_vers_emplacement[element['lettre']]
            if lettre==lettre_decodee  and nombre==element['nombre'] : 
                indice=i
                break
        return indice

    def prise_avant(self, Joueur_blanc) :
        Liste_indice_pion_supp = []
        while Liste_indice_pion_supp == [] :
            print("Noter le coup")
            Coup = self.Coup_Mat(Joueur_blanc)
            Liste_indice_pion_supp = self.select_poin_attaque(Coup)
        for indice in Liste_indice_pion_supp:
            Colision = self.colision(indice, Coup)
            if not Colision[0] :
                if Joueur_blanc :
                    coordonnee = self.liste_piece[indice].get_coordonnee()
                    if coordonnee['nombre'] == 5 :
                        lettre_decodee = self.__lettre_vers_emplacement[coordonnee['lettre']]
                        Pion = []
                        cible = None
                        if lettre_decodee != 0  and self.feuille[4][lettre_decodee - 1] == 'p' : 
                            Pion.append(self.trouve(lettre_decodee - 1, 5))
                        if lettre_decodee != 7  and self.feuille[4][lettre_decodee + 1] == 'p':
                            Pion.append(self.trouve(lettre_decodee + 1, 5))
                        for y in Pion :
                            if self.liste_piece[y].get_Tour() == Global.Tour_Jeu - 1:
                                cible = y
                        if cible != None :
                            self.liste_piece[cible].pris()
                            self.liste_piece[indice].nouvelle_position(Coup[1],int(Coup[2]))
                        else :
                            return None

                else :
                    coordonnee = self.liste_piece[indice].get_coordonnee()
                    if coordonnee['nombre'] == 4 :
                        lettre_decodee = self.__lettre_vers_emplacement[coordonnee['lettre']]
                        Pion = []
                        cible = None
                        if lettre_decodee != 0  and self.feuille[4][lettre_decodee - 1] == 'P' : 
                            Pion.append(self.trouve(lettre_decodee - 1, 4))
                        if lettre_decodee != 7  and self.feuille[4][lettre_decodee + 1] == 'P':
                            Pion.append(self.trouve(lettre_decodee + 1, 4))
                        for y in Pion :
                            if self.liste_piece[y].get_Tour() == Global.Tour_Jeu - 1:
                                cible = y
                        if cible != None :
                            self.liste_piece[cible].pris()
                            self.liste_piece[indice].nouvelle_position(Coup[1],int(Coup[2]))
                        else :
                            return None

    def doute(self, liste_indice) :
        for i in range(len(liste_indice)) :
            coordonnee = self.liste_piece[liste_indice[i][0]].get_coordonnee()
            print("Il y a la pièce en ", coordonnee['lettre'],coordonnee['nombre'])
        print("Laquelle de ces pièces parlez-vous ?(écrire un nombre entre 1 et le nombre de pièces)")
        while True:
            try :
                lecteur = int(input())
                if lecteur > 0 and lecteur <= len(liste_indice):
                    break
            except ValueError:
                print("Un nombre")
        return liste_indice[lecteur-1]

    def Mat(self, Joueur_blanc):
        liste_indice = []
        if Joueur_blanc :
            pions = [0 ,2 ,4,6,8,10,12,14]
            autre_pieces = [16,17,20,21,25,24,28,30]
            Roi = self.liste_piece[31].get_coordonnee()
        else :
            pions = [1,3,5,7,9,11,13,15]
            autre_pieces = [18,19,22,23,26,27,29,31]
            Roi = self.liste_piece[30].get_coordonnee()
        Roi_v2 = ['',Roi['lettre'], Roi['nombre']]
        for indice in pions:
            if self.liste_piece[indice].vie and self.liste_piece[indice].mouvement(Roi['lettre'], Roi['nombre']) == "attaque":
                test_collision = self.colision(indice, Roi_v2)
                if test_collision[0] and not test_collision[1]:
                    liste_indice.append(indice)
        for indice in autre_pieces:
            if self.liste_piece[indice].vie and self.liste_piece[indice].mouvement(Roi['lettre'], Roi['nombre']) == "avance":
                test_collision = self.colision(indice, Roi_v2)
                if test_collision[0] and not test_collision[1]:
                    liste_indice.append(indice)
        #si la liste n'est pas vide alors le roi est en danger
        return liste_indice

    def Coup_Mat(self, Joueur_blanc):
        Danger = self.Mat(Joueur_blanc)
        if Danger == [] :
            Coup = Lire(Joueur_blanc)
        else :
            coordonnee_danger = []
            for indice in Danger :
                coordonnee = self.liste_piece[indice].get_coordonnee()
                coordonnee_danger.append([coordonnee['lettre'], coordonnee['nombre']])
            continuation = True
            while continuation :
                print("Vous êtes en Mat !")
                Coup = Lire(Joueur_blanc)
                if Coup[0] == 'R' or Coup[0] == 'r':
                    break
                for autorisee in coordonnee_danger :
                    if Coup[1] == autorisee[0] and int(Coup[2]) == autorisee[1] :
                        continuation = False
        return Coup

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

    def menu(self , Joueur) : #true = blanc , false = noir 
        coup = '9'
        while coup not in '012':
            print("Vous pouvez tapper: ")
            print("  - 0 pour demander les coups possibles d'une pièces")
            print("  - 1 pour jouer un coup")
            print("  - 2 pour faire une prise en avant")
            coup=input() 
            if coup=='0' : #dernière modif
                get_coordonnee=[]
                choisir =self.help()
                get_coordonnee.append(choisir[0])
                get_coordonnee.append(int(choisir[1]))
                for i in range(0 , 32): 

                    element=self.liste_piece[i].get_coordonnee()

                    if get_coordonnee[0]==element['lettre']  and get_coordonnee[1]==element['nombre'] : 

                        indice=i 

                        break
                indice=i
                #choisir les cases qu'il faut tester
                
                coup_disponible=[]
                cases=['a1' , 'a2' , 'a3' , 'a4' , 'a5' , 'a6' , 'a7' , 'a8' ,
                'b1' , 'b2' ,'b3' , 'b4' ,'b5' , 'b6' ,'b7' , 'b8' ,
                'c1' , 'c2' , 'c3' , 'c4', 'c5' , 'c6', 'c7' , 'c8',
                'd1', 'd2', 'd3' , 'd4 ' ,'d5' , 'd6' , 'd7' , 'd8',
                'e1' , 'e2' , 'e3' , 'e4' , 'e5' , 'e6' , 'e7' , 'e8' ,
                'f1' , 'f2' , 'f3' , 'f4' , 'f5' , 'f6' , 'f7' , 'f8' ,
                'g1' , 'g2' , 'g3' , 'g4' , 'g5' , 'g6' , 'g7' , 'g8' ,
                'h1' , 'h2' , 'h3' , 'h4' , 'h5' , 'h6' , 'h7' , 'h8' 
                ]      
                for case in cases :

                    retour=self.liste_piece[indice].mouvement(case[0] , int(case[1]))
                    if retour== 'avance' or retour == 'attaque' : 
                    
                        coup_disponible.append(case)
                    

                
                if len(coup_disponible)>0 : 
                    print('La liste des coups disponible pour la pièce que tu as séléctionner :')
                    for case in coup_disponible:
                        print(case,end=' ')
                    print('')
                    self.deplacement(Joueur)
                
                else: 
                    print('Pas de coups disponible pour cette pièce !')
                #fin modif
            elif coup =='1' :
                self.deplacement(Joueur)
            elif coup == '2':
                self.prise_avant(Joueur)
        


    def help(self):
        while True :

            choisir=input('Selectionner la pièce que vous voulez déplacer : \n')

            if len(choisir)==2 : 
                if choisir[0] in 'abcdefgh' : 
                    if choisir[1] in '12345678' : 
                        return choisir 
            
            else :     
                print('Faites attention à votre écriture!') 

"""
test = Table()
print(test)

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

"""