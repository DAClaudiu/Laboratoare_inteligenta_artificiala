from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Exercitiul 8: Regresie pe doua caracteristici: bmi si bp

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

X = df[["bmi", "bp"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

r2_score = model.score(X_test, y_test)

print("Coeficienti model:")
print("bmi:", model.coef_[0])
print("bp:", model.coef_[1])
print("Intercept:", model.intercept_)
print("Scor R^2 pe setul de testare:", r2_score)
