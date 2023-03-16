from Animal import Animal
from Serpent import Serpent
from Oiseau import Oiseau

#on crée un panda 
panda = Animal(105, 165)
#on crée une couleuvre 
couleuvre = Serpent(0.2, 140)
#on crée un condor
condor = Oiseau(9,105, 3000)

print(panda.poids)
print (couleuvre.se_deplacer())
print(condor.se_deplacer())
print(condor.altitude_max)
