import sklearn.datasets as datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

feature_names = iris.feature_names
class_names = iris.target_names

print("Numarul de exemple si dimensiunea caracteristicilor: ", X.shape)
print("Denumirile coloanelor (atributelor): ", feature_names)
print("Numele claselor: ", class_names)
