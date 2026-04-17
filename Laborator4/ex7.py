import pandas as pd

df = pd.read_csv("data.csv")

top_nationalitati = df["Nationality"].value_counts()

print("Cea mai frecventa nationalitate:")
print(top_nationalitati.head(1))

print("\nTop 5 nationalitati:")
print(top_nationalitati.head(5))