# dados.py
import pandas as pd
from sklearn.model_selection import train_test_split

def carregar_dados(caminho_arquivo):
    data = pd.read_excel(caminho_arquivo, skiprows=1)
    X = data.iloc[:, 1:-1]  # Ignorar a coluna de ID e o alvo
    y = data.iloc[:, -1]    # A última coluna é o alvo (default)
    return X, y

def dividir_dados(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
