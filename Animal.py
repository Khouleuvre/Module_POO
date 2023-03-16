class Animal :
    def __init__(self, poids, taille):
        if poids <= 0 : 
            raise ValueError
        else:
            self.__poids = f"{poids} kg"

        if taille <= 0 :
            raise ValueError
        else :
            self.__taille = f"{taille} cm"


    def __get_poids (self):
        return self.__poids    

    def __set_poids(self, poids):
        self.__poids = f"{poids} kg"    
    
    poids = property(__get_poids,__set_poids)

    def se_deplacer(self) :
        pass

    def __str__(self):
        return f"je suis un animal de {self.__poids} et {self.__taille} en moyenne"

    def get_str (self) :
        return self.__str__
    def set_str (self, str) :
        self.str = self.__str__