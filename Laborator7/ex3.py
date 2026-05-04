from sklearn.datasets import load_diabetes

# Exercitiul 3: Listati toate caracteristicile disponibile

diabetes = load_diabetes()

print("Caracteristicile disponibile sunt:")
print(diabetes.feature_names)
