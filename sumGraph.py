from graph import *
from graph import _dico
from dijkstra import *
from itertools import combinations


city = [2, 6, 7, 8] 

matrice_complet = generate_matrice(len(city), 10)

temp = combinations(city, 2)

for i in list(temp):
    longueur,chemin = dij_rec(dico, i[0], i[1])
    print('Plus court chemin de ',i,  'est: ',chemin)
    champ = []
    dist = 0
    time = 0
    cost = 0
    for elem in range(len(chemin)+1):
        try:
            for k in range(len(_dico[chemin[elem]])):
                if _dico[chemin[elem]][k]["voisin"] == chemin[elem+1] :
                    dist += _dico[chemin[elem]][k]["distance"]
                    time += _dico[chemin[elem]][k]["temps"]
                    cost += _dico[chemin[elem]][k]["total"]
                    break
        except:
            break
    x = city.index(i[0])
    y = city.index(i[1])
    champ.append(dist)
    champ.append(time)
    champ.append(round(cost, 2))
    print(champ)
    matrice_complet[x][i[1]] = champ
    matrice_complet[y][i[0]] = champ
    
affiche_matrice(matrice_complet)