from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt

# Exercitiul 7: Regresie liniara simpla folosind bmi

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

X = df[["bmi"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print("Coeficientul modelului:", model.coef_[0])
print("Interceptul modelului:", model.intercept_)
print("Mean Squared Error:", mse)

plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, label="Date reale")
plt.plot(X_test, y_pred, linewidth=2, label="Linia de regresie")
plt.title("Regresie liniara simpla folosind BMI")
plt.xlabel("BMI")
plt.ylabel("Target")
plt.legend()
plt.grid(True)
plt.show()
