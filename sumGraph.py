from concurrent.futures import thread
from graph import *
from graph import _dico
from dijkstra import *
from itertools import combinations

def completMatrice(lenght, city):

    matrice_complet = generate_matrice(len(city), lenght)
    
    liste = []
    
    for i in reversed(liste):
            liste.append(i)

    temp = combinations(city, 2)

    for i in list(temp):
        longueur,chemin = dij_rec(dico, i[0], i[1])
        print('Plus court chemin de ',i,  'est: ',chemin)
        liste.append(chemin)
         
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
    
    liste_finale = []
    for h in range(len(liste)):
        for k in reversed(liste[h]):
            liste_finale.append(k)
        liste.append(liste_finale)
        liste_finale = []
        
    return matrice_complet, liste

def affiche_chemin(liste, tournee):
    chemin_complet = []
    try:
        for elem in range(len(tournee)):
            for t in range(len(liste)):
                if(liste[t][0] == tournee[elem] and liste[t][len(liste[t])-1] == tournee[elem+1]):
                    chemin_complet += liste[t]
    except: 
        pass
    finally:
        print(chemin_complet)
        try:
            for j in range(len(chemin_complet)):
                if chemin_complet[j] == chemin_complet[j+1]:
                    chemin_complet.pop(j+1)       
            print(chemin_complet)
        except:
            pass
        finally:
            print(chemin_complet)


city = [22, 782, 456, 810] 
tournee = [22, 782, 456, 810, 22] 
matrice_complet,liste = completMatrice(1000, city)
affiche_chemin(liste, tournee)



