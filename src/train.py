def predict(x):
    return slope * x + intercept


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

#selection de la première colonne de notre dataset (la taille de la population)
X = data.iloc[0:len(data), 0]
#selection de deuxième colonnes de notre dataset (le profit effectué)
Y = data.iloc[0:len(data), 1]

print(X)
print(Y)

axes = plt.axes()
axes.grid()  # dessiner une grille pour une meilleur lisibilité du graphe
plt.scatter(
    X, Y
)  # X et Y sont les variables qu'on a extraite dans le paragraphe précédent
plt.show()

from scipy import stats
#linregress() renvoie plusieurs variables de retour. On s'interessera
# particulierement au slope et intercept
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

#la variable fitLine sera un tableau de valeurs prédites depuis la tableau de variables X
axes = plt.axes()
axes.grid()  # dessiner une grille pour une meilleur lisibilité du graphe
plt.scatter(
    X, Y
)  # X et Y sont les variables qu'on a extraite dans le paragraphe précédent
fitLine = predict(X)
plt.plot(X, fitLine, c='r')
plt.show()
