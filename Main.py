from Animal import Animal
from Serpent import Serpent
from Oiseau import Oiseau
from Zoo import Zoo
#on crée un panda 
panda = Animal(105, 165)
#on crée une couleuvre 
couleuvre = Serpent(0.2, 140, 12)
#on crée un condor
condor = Oiseau(9,105, 3000)


La_basse_cour=Zoo([panda,couleuvre,condor])

#print(La_basse_cour.population)


La_clique = Zoo([panda,couleuvre,condor])

La_nouvelle_basse_cour = La_basse_cour + La_clique

La_nouvelle_basse_cour.population
#print(type(La_nouvelle_basse_cour[0]))