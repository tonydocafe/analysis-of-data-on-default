import matplotlib.pyplot as plt
import seaborn as sns

def plot_metrics(metrics):
    plt.figure(figsize=(8, 6))
    sns.barplot(x=list(metrics.keys()), y=list(metrics.values()), palette='viridis')
    plt.ylabel('Acurácia')
    plt.title('Comparação de Acurácia entre os Modelos')
    plt.ylim(0, 1)
    plt.show()

    print("\nAcurácia de cada modelo:")
    for model, acc in metrics.items():
        print(f"Acurácia do {model}: {acc:.4f}")
