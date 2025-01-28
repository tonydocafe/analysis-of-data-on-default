# func.py
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

def rede_neural(X_train, y_train, X_test, y_test):
    modelo = MLPClassifier(hidden_layer_sizes=(100,), max_iter=3000, random_state=42)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    print("\nAcurácia do modelo de rede neural:", accuracy_score(y_test, y_pred))
    print("Relatório de classificação:\n", classification_report(y_test, y_pred))

def perceptron(X_train, y_train, X_test, y_test):
    # Normalização dos dados
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Modelo Perceptron com peso balanceado
    modelo = Perceptron(max_iter=1000, random_state=42, class_weight="balanced")
    modelo.fit(X_train, y_train)

    # Predições e avaliação
    y_pred = modelo.predict(X_test)
    print("\nAcurácia do modelo Perceptron:", accuracy_score(y_test, y_pred))
    print("Relatório de classificação:\n", classification_report(y_test, y_pred, zero_division=1))

def arvore_decisao(X_train, y_train, X_test, y_test):
    modelo = DecisionTreeClassifier()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    print("Acurácia do modelo de árvore de decisão:", accuracy_score(y_test, y_pred))
    print("Relatório de classificação:\n", classification_report(y_test, y_pred))
