from Animal import Animal
from Serpent import Serpent
from Oiseau import Oiseau
class Zoo:
    def __init__ (self, animal, zoo2=None) :
        population = list()     
        if isinstance(animal, Animal):
            population.append(animal)
        elif isinstance(animal,list):
            population += [x for x in animal]
        elif isinstance(animal, Zoo):
            population += [x for x in animal]
            print ("Fuuuusion!")
        else : 
            raise ValueError
        self.population = population
        

    def __add__  (self, zoo2) :
        return Zoo([x for x in self.population] + [x for x in zoo2.population])
    
    def __repr__(self, zoo2):
        return
    
    #def set_population (self,population) :
    #    return [x for x in self.population]

    #property = (get_population,set_population)