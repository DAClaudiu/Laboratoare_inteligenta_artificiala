import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df["Value"] = df["Value"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)
df["Wage"] = df["Wage"].replace({"€": "", "M": "000000", "K": "000"}, regex=True)

df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df["Wage"] = pd.to_numeric(df["Wage"], errors="coerce")

plt.figure(figsize=(10,6))

sns.scatterplot(data=df, x="Wage", y="Value")

plt.title("Relatia dintre Wage si Value")
plt.xlabel("Wage")
plt.ylabel("Value")
plt.show()