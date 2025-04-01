from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


def preprocess_data(data):
    categorical_columns = ['workclass', 'education', 'marital-status', 
                           'occupation', 'relationship', 'race', 
                           'sex', 'native-country', 'income']
    label_encoder = LabelEncoder()
    for col in categorical_columns:
        data[col] = label_encoder.fit_transform(data[col])
    
    X = data.drop('income', axis=1)
    y = data['income']
    
    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X, y)
    
    print("\nDistribuição das Classes após Balanceamento:")
    print(y_res.value_counts())
    
    return train_test_split(X_res, y_res, test_size=0.2, random_state=42)
