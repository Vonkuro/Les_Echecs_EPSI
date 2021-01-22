import abc

#chemin de la pièce 
    # rend une liste de string contenant les coordonnées de chaque case

class piece(abc.ABC) :
    def __init__(self, Lettre_coor, Nombre_coor, Couleur, Symboles) :
        #Couleur est codé : 0 pour blanc et 1 pour noir
        self.coordonnee = {"lettre" : Lettre_coor, "nombre" : Nombre_coor}
        self.symbole = Symboles[Couleur]
        self.Couleur = Couleur
        self.vie = True
        self.emplacement_vers_lettre = {1 : 'a',2 : 'b',3 : 'c',4 : 'd',5 : 'e',6 : 'f',7 : 'g',8 : 'h'}
        self.lettre_vers_emplacement = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f' : 6, 'g' : 7, 'h' : 8}
    
    @abc.abstractmethod
    def mouvement(self):
        pass
    
    @abc.abstractmethod
    def chemin(self):
        pass

    def pris(self):
        self.vie = False

    def conversion_lettre(self, lettre):
        return self.lettre_vers_emplacement[lettre]

    def conversion_emplacement(self, nombre):
        return self.emplacement_vers_lettre[nombre]

    def nouvelle_position(self, Lettre_destination, Nombre_destination):
        self.coordonnee = {"lettre" : Lettre_destination, "nombre" : Nombre_destination}

    def moi(self, Lettre_destination, Nombre_destination) :
        #permet aux methodes mouvement de savoir qu'on demande un coup qui ne fait pas bouger la pièce
        if Lettre_destination == self.coordonnee["lettre"] and Nombre_destination == self.coordonnee["nombre"] :
            return True
        return False

    def get_coordonnee(self):
        return self.coordonnee

    def get_symbole(self):
        return self.symbole
    
    def get_couleur(self):
        return self.Couleur

class pion(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Pp")
        self.position_initial = True

    def nouvelle_position(self, Lettre_destination, Nombre_destination):
        self.coordonnee = {"lettre" : Lettre_destination, "nombre" : Nombre_destination}
        self.position_initial = False

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination) or not self.vie:
            return "impossible"
        #la portée servira quand on ajoutera le premier mouvement du pion
        portee = 1
        # deplacement sur une colone ?
        if Lettre_destination == self.coordonnee["lettre"] :
            # dans la bonne direction ? vers 8 pour blanc et vers 1 pour noir
            if self.Couleur == 0 and Nombre_destination == (self.coordonnee["nombre"] + portee) :
                return "avance"
            if self.Couleur == 1 and Nombre_destination == (self.coordonnee['nombre'] - portee) :
                return "avance"
            if self.position_initial :
                portee = 2
                if self.Couleur == 0 and Nombre_destination == (self.coordonnee["nombre"] + portee) :
                    return "avance"
                if self.Couleur == 1 and Nombre_destination == (self.coordonnee['nombre'] - portee) :
                    return "avance"
        emplacement_decodee = self.conversion_lettre(self.coordonnee["lettre"])
        destination_decodee = self.conversion_lettre(Lettre_destination)
        #deplacement vers une colone adjacente ?
        if emplacement_decodee + 1 == destination_decodee or emplacement_decodee - 1 == destination_decodee :
            # dans la bonne direction ? vers 8 pour blanc et vers 1 pour noir
            if self.Couleur == 0 and Nombre_destination == self.coordonnee["nombre"] + 1 :
                return "attaque"
            if self.Couleur == 1 and Nombre_destination == self.coordonnee["nombre"] - 1 :
                return "attaque"
        return "impossible"
        
    def chemin(self, Lettre_destination, Nombre_destination):
        if Lettre_destination == self.coordonnee['lettre'] :
            differance = Nombre_destination - self.coordonnee['nombre']
            if differance == 1 or differance == -1:
                return [[self.coordonnee['lettre'], Nombre_destination]]
            else :
                differance = differance/2
                return [[Lettre_destination, self.coordonnee['nombre'] + differance],[Lettre_destination, Nombre_destination]]
        return [[Lettre_destination, Nombre_destination]]


class tour(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Tt")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination) or not self.vie:
            return "impossible"
        #déplacment sur la même colone ou la même ligne ?
        if Lettre_destination == self.coordonnee["lettre"] or Nombre_destination == self.coordonnee["nombre"]:
            return "avance"
        return "impossible"
    
    def chemin(self, Lettre_destination, Nombre_destination):
        retour = []
        if Lettre_destination == self.coordonnee['lettre'] :
            if self.coordonnee['nombre'] < Nombre_destination :
                for i in range(self.coordonnee['nombre']+1, Nombre_destination + 1)  :
                    retour.append([Lettre_destination, i])
            else :
                for i in range(self.coordonnee['nombre']-1, Nombre_destination - 1, -1)  :
                    retour.append([Lettre_destination, i])
        else :
            destination = self.conversion_lettre(Lettre_destination)
            emplacement = self.conversion_lettre(self.coordonnee['lettre'])
            if emplacement < destination :
                for i in range(emplacement +1, destination + 1)  :
                    lettre = self.conversion_emplacement(i)
                    retour.append([lettre, Nombre_destination])
            else :
                for i in range(emplacement -1, destination - 1, -1)  :
                    lettre = self.conversion_emplacement(i)
                    retour.append([lettre, Nombre_destination])
        return retour


class fou(piece) :
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Ff")

    def mouvement(self, Lettre_destination, Nombre_destination) :
        if self.moi(Lettre_destination, Nombre_destination) or not self.vie:
            return "impossible"
        #tranforme les lettres en chiffre
        emplacement_decodee = self.conversion_lettre(self.coordonnee["lettre"])
        destination_decodee = self.conversion_lettre(Lettre_destination)
        #calcule de les différences
        differance_lettre = emplacement_decodee - destination_decodee
        differance_nombre = self.coordonnee["nombre"] - Nombre_destination
        #les différences sont t'elles égale au signe près ?
        if differance_lettre == differance_nombre or differance_lettre == -1 * differance_nombre :
            return "avance"
        return "impossible"

    def chemin(self, Lettre_destination, Nombre_destination):
        retour = []
        #tranforme les lettres en chiffre
        emplacement_c = self.conversion_lettre(self.coordonnee["lettre"])
        destination_c = self.conversion_lettre(Lettre_destination)
        #calcule de les différences
        differance_lettre = destination_c - emplacement_c 
        differance_nombre = self.coordonnee["nombre"] - Nombre_destination

        if differance_lettre > 0 :
            for l in range(1, differance_lettre + 1):
                lettre = self.conversion_emplacement(l + emplacement_c)
                if differance_nombre > 0 :
                    retour.append([lettre, self.coordonnee["nombre"] - l])
                else :
                    retour.append([lettre, self.coordonnee["nombre"] + l])
        else :
            for l in range(-1, differance_lettre - 1, -1):
                lettre = self.conversion_emplacement(l + emplacement_c)
                if differance_nombre > 0 :
                    retour.append([lettre, self.coordonnee["nombre"] + l])
                else :
                    retour.append([lettre, self.coordonnee["nombre"] - l])

        return retour


class chevalier(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Cc")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination) or not self.vie:
            return "impossible"
        #tranforme les lettres en chiffre
        emplacement_decodee = self.conversion_lettre(self.coordonnee["lettre"])
        destination_decodee = self.conversion_lettre(Lettre_destination)
        #calcule de la différence sur les colones
        differance_nombre = self.coordonnee["nombre"] - Nombre_destination
        #une colone et deux lignes ?
        if emplacement_decodee + 1 == destination_decodee or emplacement_decodee - 1 == destination_decodee :
            if differance_nombre == 2 or differance_nombre == - 2 :
                return "avance"
        #deux colones et une lignes ?
        if emplacement_decodee + 2 == destination_decodee or emplacement_decodee - 2 == destination_decodee :
            if differance_nombre == 1 or differance_nombre == - 1 :
                return "avance"
        return "impossible"

    def chemin(self, Lettre_destination, Nombre_destination):
        return [[Lettre_destination, Nombre_destination]]

class dame(piece):
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Dd")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination) or not self.vie:
            return "impossible"
        #addition du déplacement de la tour et du fou
        if Lettre_destination == self.coordonnee["lettre"] or Nombre_destination == self.coordonnee["nombre"]:
            return "avance"
        #tranforme les lettres en chiffre
        emplacement_decodee = self.conversion_lettre(self.coordonnee["lettre"])
        destination_decodee = self.conversion_lettre(Lettre_destination)
        #calcule de les différences
        differance_lettre = emplacement_decodee - destination_decodee
        differance_nombre = self.coordonnee["nombre"] - Nombre_destination
        #les différences sont t'elles égale au signe près ?
        if differance_lettre == differance_nombre or differance_lettre == -1 * differance_nombre :
            return "avance"
        return "impossible"

    def chemin(self, Lettre_destination, Nombre_destination):
        retour = []
        if Lettre_destination == self.coordonnee['lettre'] :
            if self.coordonnee['nombre'] < Nombre_destination :
                for i in range(self.coordonnee['nombre']+1, Nombre_destination + 1)  :
                    retour.append([Lettre_destination, i])
            else :
                for i in range(self.coordonnee['nombre']-1, Nombre_destination - 1, -1)  :
                    retour.append([Lettre_destination, i])
        elif Nombre_destination == self.coordonnee['nombre']:
            destination = self.conversion_lettre(Lettre_destination)
            emplacement = self.conversion_lettre(self.coordonnee['lettre'])
            if emplacement < destination :
                for i in range(emplacement +1, destination + 1)  :
                    lettre = self.conversion_emplacement(i)
                    retour.append([lettre, Nombre_destination])
            else :
                for i in range(emplacement -1, destination - 1, -1)  :
                    lettre = self.conversion_emplacement(i)
                    retour.append([lettre, Nombre_destination])
        else :
            #tranforme les lettres en chiffre
            emplacement_c = self.conversion_lettre(self.coordonnee["lettre"])
            destination_c = self.conversion_lettre(Lettre_destination)
            #calcule de les différences
            differance_lettre = destination_c - emplacement_c 
            differance_nombre = self.coordonnee["nombre"] - Nombre_destination

            if differance_lettre > 0 :
                for l in range(1, differance_lettre + 1):
                    lettre = self.conversion_emplacement(l + emplacement_c)
                    if differance_nombre > 0 :
                        retour.append([lettre, self.coordonnee["nombre"] - l])
                    else :
                        retour.append([lettre, self.coordonnee["nombre"] + l])
            else :
                for l in range(-1, differance_lettre - 1, -1):
                    lettre = self.conversion_emplacement(l + emplacement_c)
                    if differance_nombre > 0 :
                        retour.append([lettre, self.coordonnee["nombre"] + l])
                    else :
                        retour.append([lettre, self.coordonnee["nombre"] - l])

        return retour

class roi(piece): 
    def __init__(self, Lettre_coor, Nombre_coor, Couleur) :
        piece.__init__(self, Lettre_coor, Nombre_coor, Couleur, "Rr")

    def mouvement(self, Lettre_destination, Nombre_destination):
        if self.moi(Lettre_destination, Nombre_destination) or not self.vie:
            return "impossible"
        #tranforme les lettres en chiffre
        emplacement_decodee = self.conversion_lettre(self.coordonnee["lettre"])
        destination_decodee = self.conversion_lettre(Lettre_destination)
        # déplacmemt 1, -1 ou 0 en colone
        if emplacement_decodee + 1 == destination_decodee or emplacement_decodee - 1 == destination_decodee or emplacement_decodee == destination_decodee :
            differance_nombre = self.coordonnee["nombre"] - Nombre_destination
            #déplacement 1, -1 ou 0 en ligne
            if differance_nombre == 1 or differance_nombre == -1  or differance_nombre == 0:
                return "avance"
        return "impossible"
    
    def chemin(self, Lettre_destination, Nombre_destination):
        return [[Lettre_destination, Nombre_destination]]

#def Tour() :
     

def message_erreur_lire():
    print("L'écritue d'un coup se fait avec un format très particulier.")
    print("Il est nécessaire d'écrire le symbole de la piece puis la lettre de la colone et le chiffre de la ligne indiquant la case où la piece doit se déplacer")
    print("Exemple : Df4")
    print("La dame blance doit se rendre à la case de colone f et de ligne 4")

def Lire(Joueur_blanc):
    while True :
        try:
            lecteur=input()
            if len(lecteur) != 3 or lecteur[1] not in 'abcdefgh':
                message_erreur_lire()
            elif Joueur_blanc and lecteur[0] not in 'PTFCDR' :
                message_erreur_lire()
            elif not Joueur_blanc and lecteur[0] not in 'ptfcdr' :
                message_erreur_lire()
            elif int(lecteur[2]) < 1 or int(lecteur[2]) > 8:
                message_erreur_lire()
            else :
                return lecteur
        except ValueError:
            message_erreur_lire()
"""
test = Lire()
print(test)
"""