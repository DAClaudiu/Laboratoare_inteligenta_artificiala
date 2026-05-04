from sklearn.datasets import load_diabetes
import pandas as pd

# Exercitiul 2: Afisati primele 5 randuri intr-un DataFrame Pandas

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

print("Primele 5 randuri din setul de date:")
print(df.head())
