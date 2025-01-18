import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

# Carregar o Dataset no Python
colunas = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
           'marital-status', 'occupation', 'relationship', 'race', 
           'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
           'native-country', 'income']

# Leitura do arquivo e tratamento de valores ausentes
dados = pd.read_csv('adult.data', header=None, names=colunas, na_values=" ?")

print("Primeiras Linhas do Dataset:\n", dados.head())  # Exibe as primeiras linhas para análise

# Exibe informações gerais do dataset, como tipos de dados e valores ausentes
print("\nInformações sobre o Dataset:")
print(dados.info())

# Remover valores ausentes do dataset
data = dados.dropna()

# Transformação de variáveis categóricas utilizando LabelEncoder para convertê-las para valores numéricos
label_encoder = LabelEncoder()
for col in ['workclass', 'education', 'marital-status', 'occupation', 
            'relationship', 'race', 'sex', 'native-country', 'income']:
    data[col] = label_encoder.fit_transform(data[col])

# Divisão dos dados em variáveis independentes (X) e dependente (y)
X = data.drop('income', axis=1)
y = data['income']

# Balanceamento das classes com SMOTE
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Divisão em conjunto de treino e teste (80% treino, 20% teste) utilizando os dados balanceados
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Modelos de classificação a serem utilizados
# Regressão Logística
model_lr = LogisticRegression(max_iter=1000)
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)

# Árvore de Decisão
model_dt = DecisionTreeClassifier()
model_dt.fit(X_train, y_train)
y_pred_dt = model_dt.predict(X_test)

# XGBoost
model_xgb = XGBClassifier()
model_xgb.fit(X_train, y_train)
y_pred_xgb = model_xgb.predict(X_test)

# Avaliação dos Modelos
# Exibe o relatório de classificação para o modelo XGBoost
print("\nRelatório de Classificação do Modelo XGBoost:")
print(classification_report(y_test, y_pred_xgb))

# Gráficos Comparativos de Acurácia
print("\nGráficos de Acurácia dos Modelos:")

# Métricas de Acurácia para cada modelo
metrics = {
    'Regressão Logística': accuracy_score(y_test, y_pred_lr),
    'Árvore de Decisão': accuracy_score(y_test, y_pred_dt),
    'XGBoost': accuracy_score(y_test, y_pred_xgb)
}

# Criando o gráfico de barras para comparar a acurácia dos modelos
sns.barplot(x=list(metrics.keys()), y=list(metrics.values()))
plt.ylabel('Acurácia')
plt.title('Comparação de Acurácia entre os Modelos')
plt.show()

# Exibindo a acurácia dos modelos no console com texto em português
print("\nAcurácia de cada modelo:")
print(f"Acurácia da Regressão Logística: {metrics['Regressão Logística']:.4f}")
print(f"Acurácia da Árvore de Decisão: {metrics['Árvore de Decisão']:.4f}")
print(f"Acurácia do XGBoost: {metrics['XGBoost']:.4f}")
