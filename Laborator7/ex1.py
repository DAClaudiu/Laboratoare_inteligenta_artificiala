from sklearn.datasets import load_diabetes

# Exercitiul 1: Incarcati setul de date diabetes folosind scikit-learn

diabetes = load_diabetes()

print("Setul de date Diabetes a fost incarcat cu succes!")
print("Dimensiunea datelor:", diabetes.data.shape)
print("Dimensiunea targetului:", diabetes.target.shape)
