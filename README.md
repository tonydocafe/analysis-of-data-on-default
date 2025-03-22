# Análise de Dados com o Dataset "Adult" 🚀

Bem-vindo ao projeto de análise de dados do dataset "Adult"! Este repositório é o ponto de partida para explorar, processar e avaliar modelos de classificação sobre dados de renda, visando prever se uma pessoa ganha mais ou menos que 50K com base em diversas características.

## Estrutura do Projeto 🎯

O coração deste projeto está no arquivo `main.py`, que organiza a execução do pipeline de dados e modelos. Aqui está o que cada script faz:

### Arquivo: `main.py`
**Propósito**: Este é o ponto de entrada para o projeto de análise de dados. Ele coordena a execução dos scripts auxiliares e garante que tudo funcione em harmonia.

**Funcionalidades principais**:
- Chama os scripts auxiliares:
  - `data_loader.py`: Carrega e processa o dataset.
  - `model_trainer.py`: Treina e avalia os modelos de classificação.
  - `visualization.py`: Gera gráficos de comparação de desempenho.
- Coordena as etapas do pipeline de dados e modelos.

### Arquivo: data_loader.py
**Propósito** Gerencia o carregamento, limpeza e balanceamento do dataset "Adult".


**Funcionalidades principais**:

- Carrega o arquivo de dados (adult.data) e remove valores ausentes.

- Converte variáveis categóricas em valores numéricos com LabelEncoder.

- Aplica o algoritmo SMOTE para balancear as classes (repare que, no dataset original, temos um desbalanceamento entre as classes).

### Arquivo: model_trainer.py
**Propósito** Treina e avalia modelos de classificação no dataset processado.


**Funcionalidades principais**::

- Treina três modelos:

  - Perceptron

  - Árvore de Decisão

  - Redes Neurais

- Exibe métricas de desempenho (precisão, recall e f1-score) para cada modelo.

### Arquivo: visualization.py
**Propósito**: Gera gráficos comparativos de desempenho entre os modelos de classificação.


**Funcionalidades principais**:

- Criação de gráficos de barras comparando a acurácia de cada modelo.

- Exibição interativa dos gráficos usando matplotlib e seaborn.

### Resumo dos Dados 📊
**Registros:**
-  32.561


**Colunas:** 
- 15


**Valores Ausentes:** Algumas colunas têm valores ausentes:


- workclass: 1.836 valores ausentes.


- occupation: 1.843 valores ausentes.


- native-country: 583 valores ausentes.


**Tipos de Dados:**


- Numéricos (int64): 6 colunas


- Categóricos (object): 9 colunas


**Memória:**


- Tamanho: 3.7 MB

### Ação Recomendadas 🛠️
**Valores Ausentes:** Decida como tratar esses dados, seja preenchendo com a moda ou média ou removendo as linhas.

**Balanceamento de Classes:** O dataset foi balanceado usando técnicas como SMOTE, garantindo que as classes "income <=50K" e "income >50K" tenham o mesmo número de registros.

### Desempenho do Modelo 💪
**Acurácia Geral:** 90%

**Métricas por Classe:**

**Classe 0 (income <=50K):** Precisa de 90% de precisão e recall.

**Classe 1 (income >50K):** Resultados semelhantes, com precisão e recall de 89-90%.

### Dependências 📦
Certifique-se de ter as dependências necessárias instaladas:

- pandas

- scikit-learn

- xgboost

- matplotlib

- seaborn

- imbalanced-learn

**Como rodar**:
```bash
$ python3 main.py

