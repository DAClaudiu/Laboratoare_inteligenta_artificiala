import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

top5 = df["Nationality"].value_counts().head(5)

plt.figure(figsize=(8,8))
plt.pie(top5, labels=top5.index, autopct="%1.1f%%")

plt.title("Proportia jucatorilor pe nationalitati (Top 5)")
plt.show()