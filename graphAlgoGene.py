import random
import copy
import matplotlib.pyplot as plt
from dijkstra import *
from graph import *
import sys
import os
sys.setrecursionlimit(5000)


def mutation(chromosome):
    chromosome3 = copy.copy(chromosome)
    if 100 >= random.randint(0,100):
        firstGene = random.randint(1, len(chromosome3)-2)
        secondGene = random.randint(1, len(chromosome3)-2)
        chromosome3[firstGene], chromosome3[secondGene] = chromosome3[secondGene], chromosome3[firstGene]

        return chromosome3

    return chromosome3

def generateTournee(tailleMatrice, startTournee):
    tournee = []
    
    tailleTournee = 50 #random.randint(1, len(tailleMatrice)/2)
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
            if chromosome[i][j] == 1:
                tournee.append(j)
                break
    return tournee

def fitnessDistance(chromosome):
    distance = 0
    temps = 0
    cout = 0
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
                    temps += chromosome[i][dest][1]
                    cout += chromosome[i][dest][2]
            except:
                pass
    return distance,temps,cout

def comparaisonGen(chromosome1, chromosome2):
    distance1 = fitnessDistance(chromosome1)
    distance2 = fitnessDistance(chromosome2)

    if distance1 > distance2:
        chromosome1 = chromosome2
    
    return chromosome1

def algoGenetique(nbGeneration, matrice):
    startTournee = input("Entrez le point de départ : ") 

    tournee = generateTournee(matrice, startTournee)

    chromosome1, liste = completMatriceTournee(len(matrice), tournee)
    index0 = chromosome1[0]
    chromosome1.append(index0)
    
    print("Chemin initiale : " + str(afficheTournee(chromosome1)))
    print("Distance total tournée initiale : "+ str(fitnessDistance(chromosome1))+ "km")

    for i in range(1, nbGeneration+1):
        print("Génération " +str(i))
        chromosome2 = mutation(chromosome1)

        distance1,temps1, cout1 = fitnessDistance(chromosome1)
        distance2,temps2, cout2 = fitnessDistance(chromosome2)

        if distance1 > distance2:
            chromosome1 = chromosome2

        distance1,temps1, cout1 = fitnessDistance(chromosome1)

        print("Chemin actuel :" + str(afficheTournee(chromosome1)))
        print("Distance total tournée actuel : "+ str(distance1) + "km")

        distanceTabl.append(fitnessDistance(chromosome1))

    for j in range(1, nbGeneration+1):
        print("Génération " +str(j))
        chromosome3 = copy.copy(chromosome1)

        chromosome2 = mutation(chromosome3)

        distance3,temps3, cout3 = fitnessDistance(chromosome3)

        distance4,temps4, cout4 = fitnessDistance(chromosome2)

        if temps3 > temps4:
            chromosome3 = chromosome2

        distance3,temps3, cout3 = fitnessDistance(chromosome3)

        print("Chemin actuel :" + str(afficheTournee(chromosome3)))

        print("Temps total tournée actuel : "+ str(temps3) + "km")
        
        tempsTabl.append(fitnessDistance(chromosome3))

    for k in range(1, nbGeneration+1):
        print("Génération " +str(k))
        chromosome5 = copy.copy(chromosome1)

        chromosome2 = mutation(chromosome5)

        distance5,temps5, cout5 = fitnessDistance(chromosome5)

        distance6,temps6, cout6 = fitnessDistance(chromosome2)

        if cout5 > cout6:
            chromosome5 = chromosome2

        distance5,temps5, cout5 = fitnessDistance(chromosome5)

        print("Chemin actuel :" + str(afficheTournee(chromosome5)))

        print("Cout total tournée actuel : "+ str(cout5) + "km")
        
        coutTabl.append(fitnessDistance(chromosome5))

    print("----------------------------------------------------")
    print("Meilleur chemin trouver par rapport à la distance : "+ str(afficheTournee(chromosome1)))
    affiche_chemin(liste, afficheTournee(chromosome1))
    print("Distance : "+ str(distance1) + "Km")
    print("Temps : "+ str(temps1) + "min")
    print("Cout : "+ str(cout1) + "€")
    print("----------------------------------------------------")
    print("Meilleur chemin trouver par rapport au temps : "+ str(afficheTournee(chromosome3)))
    affiche_chemin(liste, afficheTournee(chromosome3))
    print("Distance : "+ str(distance3) + "Km")
    print("Temps : "+ str(temps3) + "min")
    print("Cout : "+ str(cout3) + "€")
    print("----------------------------------------------------")
    print("Meilleur chemin trouver par rapport au cout : "+ str(afficheTournee(chromosome5)))
    affiche_chemin(liste, afficheTournee(chromosome5))
    print("Distance : "+ str(distance5) + "Km")
    print("Temps : "+ str(temps5) + "min")
    print("Cout : "+ str(cout5) + "€")
    print("----------------------------------------------------")

distanceTabl = []
tempsTabl = []
coutTabl = []

algoGenetique(500, matrice)

plt.figure(1)
plt.subplot(1, 2, 1)
plt.plot(distanceTabl)
plt.title('Optimisation distance')
plt.xlabel('Nombre de générations')
plt.subplot(2, 2, 2)
plt.plot(tempsTabl)
plt.title('Optimisation temps')
plt.xlabel('Nombre de générations')
plt.subplot(2, 2, 4)
plt.plot(coutTabl)
plt.title('Optimisation prix')
plt.xlabel('Nombre de générations')


plt.show()




