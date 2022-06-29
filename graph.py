from turtle import position
import numpy as np
from random import randint, randrange
import random
from numpy.random import choice
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

    return matrice_complet

def mutation(chromosome):
    
    if 100 >= random.randint(0,100):
        firstGene = random.randint(1, len(chromosome)-2)
        secondGene = random.randint(1, len(chromosome)-2)
        chromosome[firstGene], chromosome[secondGene] = chromosome[secondGene], chromosome[firstGene]

        return chromosome

    return chromosome

def generateTournee(tailleMatrice, startTournee):
    tournee = []
    
    tailleTournee = 4 #random.randint(1, len(tailleMatrice)/2)
    List = [i for i in range(0, len(tailleMatrice))]
    List.remove(int(startTournee))
    for j in range(tailleTournee):
        newPoint = random.choice(List)
        List.remove(newPoint)
        tournee.append(newPoint)
    tournee.insert(0, int(startTournee))
    #tournee.append(int(startTournee))

    return tournee

def populationInitial(matrice, tournee):
    chromosome = generate_matrice(len(tournee), len(matrice[0]))    
    for k in range(0,len(chromosome)):
        for j in range(0,len(matrice)):
                chromosome[k][j] = matrice[tournee[k]][j]
    return chromosome

def afficheTournee(chromosome):
    tournee = []
    for i in range(0, len(chromosome)):
        for j in range(0, len(chromosome[0])):
            if chromosome[i][j] == 0:
                tournee.append(j)
                break
    return tournee

def fitness(chromosome):
    distance = 0
    actuel = 0
    dest = 0
    for i in range(len(chromosome)):
        for j in range(0, len(chromosome[0])):
            if chromosome[i][j] == 1:
                actuel = j
            try:
                if chromosome[i+1][j] == 1:
                    dest = j
                    distance += chromosome[i][dest][0]
            except:
                pass
    return distance

def algoGenetique(nbGeneration, matrice):
    startTournee = input("Entrez le point de départ : ") 

    tournee = generateTournee(matrice, startTournee)

    chromosome1 = completMatriceTournee(len(matrice), tournee)
    distance = fitness(chromosome1)

    print("Chemin initiale : " + str(tournee))
    print("Distance total tournée initiale : "+ str(distance))

    for i in range(1, nbGeneration+1):
        print("Génération " +str(i))


def comparaisonGen(chromosome1, chromosome2, chromosome3):
    distance1 = fitness(chromosome1)
    distance2 = fitness(chromosome2)
    distance3 = fitness(chromosome3)

    if distance1 < distance3:
        chromosome1 = chromosome3
    elif distance2 < distance3:
        chromosome2 = chromosome2
    
    return chromosome1, chromosome2

matrice = generate_matrice(20, 20)
complete_matrice(matrice, 20)
complete_point(matrice)
organize_matrice(matrice)
#affiche_matrice(matrice)
dico = dijkstra_matrice(matrice)
_dico = dico_matrice(matrice)


algoGenetique(500, matrice)

print(dico)
print(_dico)



# Code

"""G = GraphVisualization()


for sommet in range(len(matrice)):
    voisins = voisinsSommetGrapheMatrice(matrice, sommet)      # on procède en deux temps, car
    print("sommet", str(sommet), ":", str([v for v in voisins])) # les indices commencent à 0
    for v in voisins:
        G.addEdge(sommet, v)
    
G.visualize()"""


matrice2 = generate_matrice(1000, 1000)



