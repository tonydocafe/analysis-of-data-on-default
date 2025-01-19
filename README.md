"""
Arquivo: main.py
Propósito: Este é o ponto de entrada para o projeto de análise de dados do dataset 'Adult'. 
Ele organiza a execução dos scripts que carregam, processam, treinam e avaliam modelos de classificação.

Funcionalidades principais:
1. Chamadas aos scripts auxiliares:
   - data_loader.py: Carrega e processa o dataset.
   - model_trainer.py: Treina e avalia os modelos de machine learning.
   - visualization.py: Gera gráficos de comparação de desempenho.
2. Coordenação das etapas do pipeline de dados e modelos.

Dependências externas:
- pandas, scikit-learn, xgboost, matplotlib, seaborn, imbalanced-learn

Execução:
$ python3 main.py
"""
"""
Arquivo: data_loader.py
Propósito: Gerenciar o carregamento, limpeza e balanceamento do dataset 'Adult'.

Funcionalidades principais:
1. Leitura do arquivo de dados ('adult.data') e remoção de valores ausentes.
2. Conversão de variáveis categóricas em valores numéricos usando LabelEncoder.
3. Aplicação do algoritmo SMOTE para balancear as classes.

Dependências:
- pandas, sklearn.preprocessing.LabelEncoder, imblearn.over_sampling.SMOTE

Este script é chamado por 'main.py'.
"""

"""
Arquivo: model_trainer.py
Propósito: Treinar e avaliar modelos de classificação no dataset processado.

Funcionalidades principais:
1. Treinamento de três modelos:
   - Regressão Logística
   - Árvore de Decisão
   - XGBoost
2. Cálculo e exibição de métricas de desempenho para cada modelo.

Dependências:
- scikit-learn, xgboost

Este script é chamado por 'main.py' e requer os dados balanceados gerados por 'data_loader.py'.
"""
"""
Arquivo: visualization.py
Propósito: Gerar gráficos comparativos de desempenho entre os modelos de classificação.

Funcionalidades principais:
1. Criação de gráficos de barras comparando a acurácia de cada modelo.
2. Exibição interativa dos gráficos utilizando matplotlib e seaborn.

Dependências:
- matplotlib, seaborn

Este script é chamado por 'main.py' para apresentar os resultados de forma visual.
"""



