from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt

# Exercitiul 5: Creati o histograma pentru caracteristica BMI

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

plt.figure(figsize=(8, 5))
plt.hist(df["bmi"], bins=20, edgecolor="black")
plt.title("Histograma caracteristicii BMI")
plt.xlabel("BMI")
plt.ylabel("Frecventa")
plt.grid(True)
plt.show()
