from sklearn.preprocessing import StandardScaler

from Laborator6.ex2 import X_train, X_test

scaler = StandardScaler()
# Se calculează media și deviația standard pe setul de antrenare și se aplică scalarea
X_train_scaled = scaler.fit_transform(X_train)
# Pe setul de testare doar aplicăm transformarea (fără re-calculare)
X_test_scaled = scaler.transform(X_test)

print("Înainte de scalare:\n", X_train[:3])
print("\nDupă scalare:\n", X_train_scaled[:3])