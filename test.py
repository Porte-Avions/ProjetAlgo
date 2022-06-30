import random
from math import *

from sympy import randMatrix

heure = 0
heure_passe = 0

time=0
temps = 25

for i in range(40):
    if(heure+300 <= heure_passe <= heure+400) :
        print("bouchon")
        time += temps * round(random.uniform(1.1,1.7),1)
        heure_passe = time
    elif heure_passe >= heure+400:
        heure = heure_passe
    else:
        time += temps
        heure_passe = time
    print(heure_passe)
    
print(time)

