from random import randint
import random
import copy
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import *
from itertools import combinations

# Defining a Class
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
        
# Calcul voisins
def voisinsSommetGrapheMatrice(matrice, sommet):
    liste = matrice[sommet]
    voisins = \
        [i for i, value in enumerate(liste) if liste[i] != 0] #SOLUTION
    return voisins

def field(matrice, i, j, inferieur, superieur):
    inf = inferieur
    sup = superieur
    _cost_essence = 1.80
    
    field = []
    km=(70, 80, 90, 110, 130)
    dist = randint(inf, sup)
    velocity = random.choice(km)
    time = round((dist/velocity)*60)
    conso = 8
    peage_cost = 0
    if velocity == 130:
        conso += conso*0.2
        peage_cost += round((1.9+4.5*(dist/sup)),1)
    elif velocity == 110:
        conso += conso*0.15
    price_essence = round((((dist*conso)/100) * _cost_essence),1)
    total_price = round((peage_cost + price_essence),1)
    field.append(1)
    field.append(dist)
    field.append(velocity) #supprimer
    field.append(time)
    field.append(conso)
    field.append(peage_cost)
    field.append(price_essence)
    field.append(total_price)
    matrice[i][j] = field
    matrice[j][i] = field
    
def affiche_matrice(matrice):
    for line in matrice:
        print(line)
        
def generate_matrice(M,N):
    matrice = []
    for i in range(M):
        line=[]
        for j in range(N):
            line.append(0)
        matrice.append(line)
    return matrice
        
def complete_matrice(matrice, M):
    for i in range(M):
        _nb_element = 2
        _element = random.sample(range(M), _nb_element)
        try:
            for j in _element:
                if i != j :
                    field(matrice, i, j, 1, 50)
        except:
            _element = []
            _element = random.sample(range(M), _nb_element)
        finally:
            for j in _element:
                if i != j :
                    field(matrice, i, j, 1, 50)
        _element = []        
    return matrice

def complete_point(matrice):
    for i in range(1, len(matrice)):
        field(matrice, 0, i, 50, 100)

def organize_matrice(matrice):
    for i in range(0, len(matrice)):
        for j in range(i+1, len(matrice)):
            matrice[j][i] = matrice [i][j]                      
            
def dico_matrice(matrice):
    _map = {}
    _list = []

    dico = {
    "bool_chemin": None,
    "voisin": None,
    "distance": None, 
    "vitesse": None, # supprimer
    "temps": None,
    "consommation": None,
    "peage": None,
    "cout": None,
    "total": None
    }
    
    for i in range(0, len(matrice)):
        _list.clear()
        for j in range(0, len(matrice)):
            if matrice[i][j] != 0:
                dico["bool_chemin"] = matrice[i][j][0]
                dico["voisin"] = j
                dico["distance"] = matrice[i][j][1]
                dico["vitesse"] = matrice[i][j][2]
                dico["temps"] = matrice[i][j][3]
                dico["consommation"] = matrice[i][j][4]
                dico["peage"] = matrice[i][j][5]
                dico["cout"] = matrice[i][j][6]
                dico["total"] = matrice[i][j][7]
                _list.append(copy.deepcopy(dico))    
        _map[i] = copy.deepcopy(_list)
    return _map

def dijkstra_matrice(matrice):
    _map = {}

    dico = {}
    
    for i in range(0, len(matrice)):
        for j in range(0, len(matrice)):
            if matrice[i][j] != 0:
                dico.update( {j : matrice[i][j][1]}) 
        _map[i] = copy.deepcopy(dico)
        dico = {}
    return _map

def completMatriceTournee(lenght, city):

    matrice_complet = generate_matrice(len(city), lenght)
    
    liste = []
    
    heure = 0
    heure_passe = 0
    
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
        try:
            for j in range(len(chemin_complet)):
                if chemin_complet[j] == chemin_complet[j+1]:
                    chemin_complet.pop(j+1)       
        except:
            pass
        finally:
            print("Chemin Complet: ", chemin_complet)

matrice = generate_matrice(100, 100)
complete_matrice(matrice, 100)
complete_point(matrice)
organize_matrice(matrice)
#affiche_matrice(matrice)
dico = dijkstra_matrice(matrice)
_dico = dico_matrice(matrice)







