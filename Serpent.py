from Animal import Animal

class Serpent (Animal) :
    def __init__(self, poids, taille):
        Animal.__init__ (self, poids, taille)

    def se_deplacer(self):
        return "je rampe"
        