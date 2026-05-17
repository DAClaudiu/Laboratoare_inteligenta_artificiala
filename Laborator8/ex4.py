from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)

df = wine.frame

X = df[['alcohol', 'flavanoids']]
y = df['target']

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)

plt.figure(figsize=(10, 6))
plot_tree(
    model,
    feature_names=['alcohol', 'flavanoids'],
    class_names=['Vin tip 1', 'Vin tip 2', 'Vin tip 3'],
    filled=True
)
plt.show()