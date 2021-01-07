import abc
#jeu d'echec à rendre pour le 21/01
class Table :
    def __init__(self) :
        self.__lettre_vers_emplacement = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f' : 5, 'g' : 6, 'h' : 7}
        self.feuille = []
        self.liste_piece =[]
        #les pions
        for l in "abcdefgh":
            self.liste_piece.append(pion(l,7,1))
            self.liste_piece.append(pion(l,2,0))
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
        self.liste_piece.append(reine('d',8,1))
        self.liste_piece.append(reine('d',1,0))
        #les rois
        self.liste_piece.append(Majestee('e',8,1))
        self.liste_piece.append(Majestee('e',1,0))
        #on va les placer
        self.mise_a_jour()

    def mise_a_jour(self):
        #on réécrit la representation de la table à chaque mise à jour
        self.feuille = []
        for i in range(8):
            self.feuille.append([])
            for j in range(8):
                self.feuille[i].append('|_|')
        for la_piece in self.liste_piece :
            emplacement_codee = la_piece.get_coordonnee() 
            emplacement_decodee = [emplacement_codee["nombre"], self.__lettre_vers_emplacement[emplacement_codee["lettre"]]]
            self.feuille[emplacement_decodee[0]][emplacement_decodee[1]] = la_piece.get_symbole


class piece(abc.ABC) :
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur, Symboles) :
        #Couleur est codé : 0 pour blanc et 1 pour noir
        self.__coordonnee = {"lettre" : Lettre_coor, "nombre" : Nombre_coor}
        self.__symbole = Symboles[Couleur]
        self.__Couleur = Couleur
        self.__vie = True
        self.__lettre_vers_emplacement = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f' : 5, 'g' : 6, 'h' : 7}
    
    @abc.abstractmethod
    def mouvement(self):
        pass

    def get_coordonnee(self):
        return self.__coordonnee

    def get_symbole(self):
        return self.__symbole

class pion(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Pp")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if 
            if self.__Couleur == 0:

            else :

        else :



class tour(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Tt")

class fou(piece) :
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Ff")

class chevalier(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Cc")

class dame(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Dd")

class Roi(piece): 
    #j'utilise Majestée au lieu de Roi pour ne pas confondre le Roi et la Reine
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Rr")

def Tour() :
    d 
