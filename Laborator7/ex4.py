from sklearn.datasets import load_diabetes
import pandas as pd

# Exercitiul 4: Accesarea informatiilor statistice: media, deviatia standard, minimul etc.

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

print("Informatii statistice despre setul de date:")
print(df.describe())

print("\nMedia fiecarei coloane:")
print(df.mean())

print("\nDeviatia standard pentru fiecare coloana:")
print(df.std())

print("\nValoarea minima pentru fiecare coloana:")
print(df.min())
