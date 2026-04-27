from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from Laborator6.ex2 import y_train, y_test
from Laborator6.ex3 import X_train_scaled, X_test_scaled

# Presupunem că X_train_scaled, X_test_scaled, y_train, y_test sunt deja definite
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
acuratețe = accuracy_score(y_test, y_pred)

print(f"Acuratețea modelului KNN (k=3) pe setul de testare: {acuratețe * 100:.2f}%")