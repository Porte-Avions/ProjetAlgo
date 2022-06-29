import numpy as np
import pickle
import matplotlib.pyplot as plt
import networkx as nx

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
        
def voisinsSommetGrapheMatrice(matrice, sommet):
    liste = matrice[sommet]
    voisins = \
        [i for i, value in enumerate(liste) if liste[i] != 0] #SOLUTION
    return voisins

def generate_matrice(M,N):
    matrice = []
    for i in range(M):
        line=[]
        for j in range(N):
            line.append(0)
        matrice.append(line)
    return matrice
  
matrice2 = generate_matrice(1000, 1000)

open_file = open("C:\\Users\\Utilisateur\\Desktop\\matrice.pkl", "rb")
matrice = pickle.load(open_file)
open_file.close()   

#city = [2, 526, 852, 937] 
city = [22, 586, 752, 837] 

for elem in city:
    for j in range(len(matrice)):
        matrice2[elem][j] = matrice[elem][j]

"""list1 = []
for elem in city:
  for j in range(len(matrice)):
    if matrice2[elem][j] != 0:
        for k in range(len(matrice)):
            matrice2[j][k] = matrice[j][k]
        list1.append(j)
      
list2 = []
for elem in list1:
  for j in range(len(matrice)):
    if matrice[elem][j] != 0:
        for k in range(len(matrice)):
            matrice2[j][k] = matrice[j][k]
        list2.append(j)
       
new_list2 = list(set(list2))

for elem in city:
    new_list2.remove(elem)

for elem in new_list2:
  for j in range(len(matrice)):
    if matrice[elem][j] != 0:
        for k in range(len(matrice)):
            matrice2[j][k] = matrice[j][k]"""

G = GraphVisualization()


for sommet in range(len(matrice2)):
    voisins = voisinsSommetGrapheMatrice(matrice2, sommet)      # on procède en deux temps, car
    #print("sommet", str(sommet), ":", str([v for v in voisins])) # les indices commencent à 0
    for v in voisins:
        G.addEdge(sommet, v)
    
G.visualize()
