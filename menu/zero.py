import matplotlib.pyplot as plt
import numpy as np

# Dados para cada modelo
modelos = ['Perceptron', 'Rede Neural', 'Árvore de Decisão']
precision_0 = [0.80, 0.85, 0.83]
recall_0 = [0.31, 0.57, 0.81]
f1_0 = [0.45, 0.68, 0.82]

# Definindo o eixo x
x = np.arange(len(modelos))

# Criando o gráfico de linhas para Precision, Recall e F1 da classe 0
plt.figure(figsize=(10, 6))

# Plotando as linhas para as métricas de classe 0
plt.plot(x, precision_0, marker='o', label='Precision (0)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, recall_0, marker='o', label='Recall (0)', color='green', linestyle='-', linewidth=2)
plt.plot(x, f1_0, marker='o', label='F1 (0)', color='coral', linestyle='-', linewidth=2)

# Adicionando título e rótulos aos eixos
plt.title('Precision, Recall e F1 para a Classe 0')
plt.xlabel('Modelos')
plt.ylabel('Valor das Métricas')

# Ajustando os rótulos no eixo X
plt.xticks(x, modelos)

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.tight_layout()
plt.show()
