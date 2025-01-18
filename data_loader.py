import pandas as pd

def load_data(file_path):
    colunas = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
               'marital-status', 'occupation', 'relationship', 'race', 
               'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
               'native-country', 'income']
    data = pd.read_csv(file_path, header=None, names=colunas, na_values=" ?")
    print("\nInformações sobre o Dataset:")
    print(data.info())
    print("\nValores Ausentes por Coluna:")
    print(data.isnull().sum())
    return data.dropna()
