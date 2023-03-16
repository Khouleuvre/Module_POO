from Animal import Animal

class Oiseau (Animal) :
    def __init__(self, poids, taille, altitude_max):
        #super() permet de faire référence à la classe parente 
        # c'est plus court que de faire Animal.__init__(self, poids, taille) -> mauvaise pratique
        super().__init__ (poids, taille) 
        self.__altitude_max = f"{altitude_max} mètres"

    

    def get_altitude_max (self):
        return self.__altitude_max
    
    def set_altitude_max(self, altitude_max):
        self.__altitude_max = altitude_max
        print(f"{altitude_max} mètres")
        return altitude_max
    


    altitude_max = property(get_altitude_max,set_altitude_max)
    

    def se_deplacer(self):
        return "je vole"
    