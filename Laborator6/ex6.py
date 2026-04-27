from sklearn.metrics import confusion_matrix, classification_report

from Laborator6.ex1 import iris
from Laborator6.ex2 import y_test
from Laborator6.ex4 import y_pred

# Folosim predictiile de la modelul cu k=3 (ex 4)
cm = confusion_matrix(y_test, y_pred)
raport = classification_report(y_test, y_pred, target_names=iris.target_names)

print("Matricea de Confuzie:")
print(cm)
print("\nRaport de Clasificare:")
print(raport)

# Interpretare: Clasa 'setosa' are de obicei scoruri de 1.00 (perfectă),
# fiind cea mai ușor de identificat.