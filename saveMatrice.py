import pickle
from graph import matrice

open_file = open("C:\\Users\\Utilisateur\\Desktop\\matrice.pkl", "wb")
pickle.dump(matrice, open_file)
open_file.close()