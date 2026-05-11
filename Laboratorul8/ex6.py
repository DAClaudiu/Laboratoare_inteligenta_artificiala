from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

wine = load_wine(as_frame=True)

df = wine.frame


X = df[wine.feature_names]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

importante = model.feature_importances_

rezultat = pd.DataFrame({
    'Caracteristica': wine.feature_names,
    'Importanta': importante
})

rezultat = rezultat.sort_values(
    by='Importanta',
    ascending=False
)

print(rezultat)