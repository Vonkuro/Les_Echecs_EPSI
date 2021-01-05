class Table :
    def __initi__(self) :
        self.feuille = []
        for i in range(8):
            self.feuille.append([])
            for j in range(8):
                self.feuille[i].append('|_|')
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

class piece :
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur, Symboles) :
        #Couleur est codé : 0 pour blanc et 1 pour noir
        self.coordonnee = {"lettre" : Lettre_coor, "nombre" : Nombre_coor}
        self.symboles = Symboles[Couleur]
        self.vie = True
    

class pion(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Pp")

class tour(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Tt")

class fou(piece) :
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Ff")

class chevalier(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Cc")

class reine(piece):
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Rr")

class Majestee(piece): 
    #j'utilise Majestée au lieu de Roi pour ne pas confondre le Roi et la Reine
    def __initi__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Mm")

def Tour() :
    d 
