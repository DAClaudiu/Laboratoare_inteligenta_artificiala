from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)

print(wine.feature_names)