import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from Laborator6.ex2 import y_train, y_test
from Laborator6.ex3 import X_train_scaled, X_test_scaled

k_values = range(1, 16)
scoruri = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    scoruri.append(accuracy_score(y_test, model.predict(X_test_scaled)))

plt.figure(figsize=(10, 6))
plt.plot(k_values, scoruri, marker='o', color='green')
plt.title('Impactul valorii k asupra acurateții')
plt.xlabel('Valoarea k')
plt.ylabel('Acuratețe')
plt.grid(True)
plt.show()

# Comentariu: Valoarea optimă este de obicei un k impar (pentru a evita egalitatea)
# care oferă cea mai mare acuratețe fără a complica modelul inutil.