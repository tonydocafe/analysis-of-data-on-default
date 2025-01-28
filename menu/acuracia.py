import matplotlib.pyplot as plt
import numpy as np

# Dados para cada modelo
modelos = ['Perceptron', 'Rede Neural', 'Árvore de Decisão']
acuracia = [0.4008888888888889, 0.5821111111111111, 0.7264444444444444]

# Definindo o eixo x
x = np.arange(len(modelos))

# Criando o gráfico de linhas para Acurácia
plt.figure(figsize=(10, 6))

# Plotando a linha para Acurácia
plt.plot(x, acuracia, marker='o', label='Acurácia', color='purple', linestyle='-', linewidth=2)

# Adicionando título e rótulos aos eixos
plt.title('Acurácia dos Modelos de Aprendizado')
plt.xlabel('Modelos')
plt.ylabel('Acurácia')

# Ajustando os rótulos no eixo X
plt.xticks(x, modelos)

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.tight_layout()
plt.show()
