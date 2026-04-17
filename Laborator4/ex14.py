import pandas as pd

df = pd.read_csv("data.csv")

df["Scor"] = (
    0.3 * df["Overall"] +
    0.3 * df["Potential"] +
    0.2 * df["SprintSpeed"] +
    0.2 * df["ShortPassing"]
)

print(df[["Name", "Overall", "Potential", "SprintSpeed", "ShortPassing", "Scor"]])