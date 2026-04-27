import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X, y = iris.data, iris.target


X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2)

# Print shape for each subset

print("Forma subsetului de antrenare", X_train.shape)
print("Forma subsetului de testare", X_test.shape)



