from Animal import Animal

class Serpent (Animal) :
    def __init__(self, poids, taille, vitesse):
        super().__init__ (poids, taille)
        self.__vitesse = vitesse


    

    def se_deplacer(self):
        return "je rampe"
        