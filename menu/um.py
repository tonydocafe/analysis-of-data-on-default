import matplotlib.pyplot as plt
import numpy as np

# Dados para cada modelo
modelos = ['Perceptron', 'Rede Neural', 'Árvore de Decisão']
precision_1 = [0.22, 0.29, 0.38]
recall_1 = [0.71, 0.63, 0.42]
f1_1 = [0.34, 0.40, 0.40]

# Definindo o eixo x
x = np.arange(len(modelos))

# Criando o gráfico de linhas para Precision, Recall e F1 da classe 1
plt.figure(figsize=(10, 6))

# Plotando as linhas para as métricas de classe 1
plt.plot(x, precision_1, marker='o', label='Precision (1)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, recall_1, marker='o', label='Recall (1)', color='green', linestyle='-', linewidth=2)
plt.plot(x, f1_1, marker='o', label='F1 (1)', color='red', linestyle='-', linewidth=2)

# Adicionando título e rótulos aos eixos
plt.title('Precision, Recall e F1 para a Classe 1')
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
