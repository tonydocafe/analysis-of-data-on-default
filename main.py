from data_loader import load_data
from preprocessing import preprocess_data
from models import train_models
from visualization import plot_metrics

def main():
    # Caminho do arquivo de dados
    file_path = 'adult.data'
    
    # Carregar os dados
    data = load_data(file_path)
    
    # Pré-processar os dados
    X_train, X_test, y_train, y_test = preprocess_data(data)
    
    # Treinar e avaliar os modelos
    metrics = train_models(X_train, y_train, X_test, y_test)
    
    # Visualizar os resultados
    plot_metrics(metrics)

if __name__ == '__main__':
    main()
