from Animal import Animal

class Oiseau (Animal) :
    def __init__(self, poids, taille, altitude_max):
        #super() permet de faire référence à la classe parente 
        # c'est plus court que de faire Animal.__init__(self, poids, taille) -> mauvaise pratique
        super().__init__ (poids, taille)
        self.altitude_max = altitude_max

    def se_deplacer(self):
        return "je vole"
    