import matplotlib.pyplot as plt
import numpy as np

from Laborator6.ex1 import iris, X, y
from Laborator6.ex3 import scaler
from Laborator6.ex4 import knn

# 7.1 Vizualizare (lungime petală vs lățime petală)
plt.scatter(X[:, 2], X[:, 3], c=y, cmap='brg', edgecolors='k')
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.title('Distribuția claselor Iris')
plt.show()

# 7.2 Predicție pentru date noi
print("\n--- Testează modelul cu date proprii ---")
sl = float(input("Sepal length: "))
sw = float(input("Sepal width: "))
pl = float(input("Petal length: "))
pw = float(input("Petal width: "))

date_noi = np.array([[sl, sw, pl, pw]])
date_noi_scalate = scaler.transform(date_noi) # Scalarea este vitală!

predicitie = knn.predict(date_noi_scalate)
nume_clasa = iris.target_names[predicitie][0]

print(f"\nRezultat: Floarea introdusă este probabil o Iris {nume_clasa.capitalize()}.")