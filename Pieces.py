import abc


class piece(abc.ABC) :
    def __init__(self, Lettre_coor, Nombre_coor, Couleur, Symboles) :
        #Couleur est codé : 0 pour blanc et 1 pour noir
        self.__coordonnee = {"lettre" : Lettre_coor, "nombre" : Nombre_coor}
        self.__symbole = Symboles[Couleur]
        self.__Couleur = Couleur
        self.__vie = True
        #self.__emplacement_vers_lettre = {1 : 'a',2 : 'b',3 : 'c',4 : 'd',5 : 'e',6 : 'f',7 : 'g',8 : 'h'}
        self.__lettre_vers_emplacement = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f' : 6, 'g' : 7, 'h' : 8}
    
    @abc.abstractmethod
    def mouvement(self):
        pass
    

    def nouvelle_position(self, Lettre_destination, Nombre_destination):
        self.__coordonnee = {"lettre" : Lettre_destination, "nombre" : Nombre_destination}

    def moi(self, Lettre_destination, Nombre_destination) :
        #permet aux methodes mouvement de savoir qu'on demande un coup qui ne fait pas bouger la pièce
        if Lettre_destination == self.__coordonnee["lettre"] and Nombre_destination == self.__coordonnee["nombre"] :
            return True
        return False

    def get_coordonnee(self):
        return self.__coordonnee

    def get_symbole(self):
        return self.__symbole

class pion(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Pp")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination):
            return "impossible"
        #la portée servira quand on ajoutera le premier mouvement du pion
        portee = 1
        # deplacement sur une colone ?
        if Lettre_destination == self.__coordonnee["lettre"] :
            # dans la bonne direction ? vers 8 pour blanc et vers 1 pour noir
            if self.__Couleur == 0 and Nombre_destination == self.__coordonnee["nombre"] + portee :
                return "avance"
            if self.__Couleur == 1 and Nombre_destination == self.__coordonnee["nombre"] - portee :
                return "avance"
        emplacement_decodee = self.__lettre_vers_emplacement[self.__coordonnee["lettre"]]
        destination_decodee = self.__lettre_vers_emplacement[Lettre_destination]
        #deplacement vers une colone adjacente ?
        if emplacement_decodee + 1 == destination_decodee or emplacement_decodee - 1 == destination_decodee :
            # dans la bonne direction ? vers 8 pour blanc et vers 1 pour noir
            if self.__Couleur == 0 and Nombre_destination == self.__coordonnee["nombre"] + 1 :
                return "attaque"
            if self.__Couleur == 1 and Nombre_destination == self.__coordonnee["nombre"] - 1 :
                return "attaque"
        return "impossible"
            


class tour(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Tt")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination):
            return "impossible"
        #déplacment sur la même colone ou la même ligne ?
        if Lettre_destination == self.__coordonnee["lettre"] or Nombre_destination == self.__coordonnee["nombre"]:
            return "avance"
        return "impossible"

class fou(piece) :
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Ff")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination):
            return "impossible"
        #tranforme les lettres en chiffre
        emplacement_decodee = self.__lettre_vers_emplacement[self.__coordonnee["lettre"]]
        destination_decodee = self.__lettre_vers_emplacement[Lettre_destination]
        #calcule de les différences
        differance_lettre = emplacement_decodee - destination_decodee
        differance_nombre = self.__lettre_vers_emplacement[self.__coordonnee["nombre"]] - Nombre_destination
        #les différences sont t'elles égale au signe près ?
        if differance_lettre == differance_nombre or differance_lettre == -1 * differance_nombre :
            return "avance"
        return "impossible"

class chevalier(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Cc")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination):
            return "impossible"
        #tranforme les lettres en chiffre
        emplacement_decodee = self.__lettre_vers_emplacement[self.__coordonnee["lettre"]]
        destination_decodee = self.__lettre_vers_emplacement[Lettre_destination]
        #calcule de la différence sur les colones
        differance_nombre = self.__lettre_vers_emplacement[self.__coordonnee["nombre"]] - Nombre_destination
        #une colone et deux lignes ?
        if emplacement_decodee + 1 == destination_decodee or emplacement_decodee - 1 == destination_decodee :
            if differance_nombre == 2 or differance_nombre == - 2 :
                return "avance"
        #deux colones et une lignes ?
        if emplacement_decodee + 2 == destination_decodee or emplacement_decodee - 2 == destination_decodee :
            if differance_nombre == 1 or differance_nombre == - 1 :
                return "avance"
        return "impossible"


class dame(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Dd")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination):
            return "impossible"
        #addition du déplacement de la tour et du fou
        if Lettre_destination == self.__coordonnee["lettre"] or Nombre_destination == self.__coordonnee["nombre"]:
            return "avance"
        emplacement_decodee = self.__lettre_vers_emplacement[self.__coordonnee["lettre"]]
        destination_decodee = self.__lettre_vers_emplacement[Lettre_destination]
        differance_nombre = self.__lettre_vers_emplacement[self.__coordonnee["nombre"]] - Nombre_destination
        if emplacement_decodee + 1 == destination_decodee or emplacement_decodee - 1 == destination_decodee :
            if differance_nombre == 2 or differance_nombre == - 2 :
                return "avance"
        if emplacement_decodee + 2 == destination_decodee or emplacement_decodee - 2 == destination_decodee :
            if differance_nombre == 1 or differance_nombre == - 1 :
                return "avance"
        return "impossible"


class roi(piece): 
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Rr")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination):
            return "impossible"
        #tranforme les lettres en chiffre
        emplacement_decodee = self.__lettre_vers_emplacement[self.__coordonnee["lettre"]]
        destination_decodee = self.__lettre_vers_emplacement[Lettre_destination]
        # déplacmemt 1, -1 ou 0 en colone
        if emplacement_decodee + 1 == destination_decodee or emplacement_decodee - 1 == destination_decodee or emplacement_decodee == destination_decodee :
            differance_nombre = self.__lettre_vers_emplacement[self.__coordonnee["nombre"]] - Nombre_destination
            #déplacement 1, -1 ou 0 en ligne
            if differance_nombre == 1 or differance_nombre == -1  or differance_nombre == 0:
                return "avance"
        return "impossible"

#def Tour() :
     