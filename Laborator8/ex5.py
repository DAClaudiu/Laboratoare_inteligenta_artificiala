from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

wine = load_wine(as_frame=True)

df = wine.frame


X = df[['alcohol', 'flavanoids']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model_complet = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

model_complet.fit(X_train, y_train)

y_pred = model_complet.predict(X_test)

acuratete = accuracy_score(y_test, y_pred)

print("Acuratețea pe setul de testare:", acuratete)