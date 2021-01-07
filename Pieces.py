import abc

class piece(abc.ABC) :
    def __init__(self, Lettre_coor, Nombre_coor, Couleur, Symboles) :
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
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Pp")

    def mouvement(self, Lettre_destination, Nombre_destination):
        pass
        """
        if 
            if self.__Couleur == 0:

            else :

        else :

"""

class tour(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Tt")
    def mouvement(self, Lettre_destination, Nombre_destination):
        pass

class fou(piece) :
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Ff")
    def mouvement(self, Lettre_destination, Nombre_destination):
        pass

class chevalier(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Cc")
    def mouvement(self, Lettre_destination, Nombre_destination):
        pass

class dame(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Dd")
    def mouvement(self, Lettre_destination, Nombre_destination):
        pass

class roi(piece): 
    #j'utilise Majestée au lieu de Roi pour ne pas confondre le Roi et la Reine
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Rr")
    def mouvement(self, Lettre_destination, Nombre_destination):
        pass
#def Tour() :
#    d 