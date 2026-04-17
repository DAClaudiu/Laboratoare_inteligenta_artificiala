import pandas as pd

df = pd.read_csv("data.csv")

df["Position"] = df["Position"].fillna("Unknown")

print(df["Position"])