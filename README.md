"""
##### Arquivo: main.py
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

##### Arquivo: data_loader.py
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

##### Arquivo: model_trainer.py
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

#####  Arquivo: visualization.py
Propósito: Gerar gráficos comparativos de desempenho entre os modelos de classificação.

Funcionalidades principais:
1. Criação de gráficos de barras comparando a acurácia de cada modelo.
2. Exibição interativa dos gráficos utilizando matplotlib e seaborn.

Dependências:
- matplotlib, seaborn

Este script é chamado por 'main.py' para apresentar os resultados de forma visual.
"""

-----------------------------------------------------------------------------------


SAIDA

Resumo:

O dataset possui 32.561 registros e 15 colunas.
Algumas colunas têm valores ausentes, como workclass (1.836 valores ausentes), occupation (1.843) e native-country (583).
Tipos de dados:
int64 (6 colunas): Valores numéricos inteiros.
object (9 colunas): Valores categóricos ou strings.
Tamanho em memória: 3.7 MB.

Resumo:

Três colunas têm valores ausentes:
workclass: 1.836 valores ausentes.
occupation: 1.843 valores ausentes.
native-country: 583 valores ausentes.

Ação recomendada: 

Decida como lidar com esses valores:
Preenchimento (e.g., com a moda ou média).
Remoção de linhas com valores ausentes.


O dataset original foi balanceado (usando SMOTE ou outra técnica) para que as duas classes (income <=50K e income >50K) tenham o mesmo número de registros (22.654 cada).
Isso melhora o desempenho dos modelos em datasets originalmente desbalanceados.


Desempenho do Modelo:

Acurácia Geral: 90%.
Métricas para cada classe:
precision (Precisão): Proporção de predições corretas para cada classe.
recall (Revocação): Proporção de exemplos positivos que o modelo conseguiu identificar.
f1-score: Combinação harmônica de precision e recall.

Resumo:

Classe 0 (income <=50K): Boa precisão e revocação (90%).
Classe 1 (income >50K): Resultados semelhantes (89-90%).

Suporte:

Quantidade de amostras de teste para cada classe (0: 4.542, 1: 4.520).





