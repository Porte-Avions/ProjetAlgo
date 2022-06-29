from graph import *
from graph import _dico
from dijkstra import *
from itertools import combinations


def completMatrice(lenght, city):

    matrice_complet = generate_matrice(len(city), lenght)

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
        
    for j in range(len(city)):
        x = city[j]
        matrice_complet[j][x] = 1
        

city = [22, 782, 456, 810, 892, 52, 825, 320, 952, 853, 742, 12, 259, 963, 201, 542, 568, 745, 123, 529] 
completMatrice(1000, city)
    
"""affiche_matrice(matrice_complet)

G = GraphVisualization()

for sommet in range(len(matrice_complet)):
    voisins = voisinsSommetGrapheMatrice(matrice_complet, sommet)      # on procède en deux temps, car
    print("sommet", str(sommet), ":", str([v for v in voisins])) # les indices commencent à 0
    for v in voisins:
        s = city[sommet]
        G.addEdge(s, v)
    
G.visualize()"""



test={
    22:{ 782: [437, 638, 24, 888, 598, 630, 420, 293, 233, 445, 469, 814, 58]}
}