import matplotlib.pyplot as plt
import numpy as np

# Dados para cada modelo
modelos = ['Perceptron', 'Rede Neural', 'Árvore de Decisão']
acuracia = [0.4008888888888889, 0.5821111111111111, 0.7264444444444444]
precision_0 = [0.80, 0.85, 0.83]
recall_0 = [0.31, 0.57, 0.81]
f1_0 = [0.45, 0.68, 0.82]
precision_1 = [0.22, 0.29, 0.38]
recall_1 = [0.71, 0.63, 0.42]
f1_1 = [0.34, 0.40, 0.40]

# Definindo o eixo x
x = np.arange(len(modelos))

# Criando o gráfico de linhas
plt.figure(figsize=(12, 8))

# Plotando as linhas para cada métrica
plt.plot(x, precision_0, marker='o', label='Precision (0)', color='lightblue', linestyle='-', linewidth=2)
plt.plot(x, recall_0, marker='o', label='Recall (0)', color='lightgreen', linestyle='-', linewidth=2)
plt.plot(x, f1_0, marker='o', label='F1 (0)', color='lightcoral', linestyle='-', linewidth=2)

plt.plot(x, precision_1, marker='o', label='Precision (1)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, recall_1, marker='o', label='Recall (1)', color='green', linestyle='-', linewidth=2)
plt.plot(x, f1_1, marker='o', label='F1 (1)', color='red', linestyle='-', linewidth=2)

plt.plot(x, acuracia, marker='o', label='Acurácia', color='purple', linestyle='-', linewidth=2)

# Adicionando título e rótulos aos eixos
plt.title('Métricas dos Modelos de Aprendizado (Linha)')
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
