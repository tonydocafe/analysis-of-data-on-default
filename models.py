from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_models(X_train, y_train, X_test, y_test):
    # Regressão Logística
    model_lr = LogisticRegression(max_iter=1000, random_state=42)
    model_lr.fit(X_train, y_train)
    y_pred_lr = model_lr.predict(X_test)
    
    # Árvore de Decisão
    model_dt = DecisionTreeClassifier(random_state=42)
    model_dt.fit(X_train, y_train)
    y_pred_dt = model_dt.predict(X_test)
    
    # XGBoost
    model_xgb = XGBClassifier(random_state=42)
    model_xgb.fit(X_train, y_train)
    y_pred_xgb = model_xgb.predict(X_test)
    
    print("\nRelatório de Classificação do Modelo XGBoost:")
    print(classification_report(y_test, y_pred_xgb))
    
    metrics = {
        'Regressão Logística': accuracy_score(y_test, y_pred_lr),
        'Árvore de Decisão': accuracy_score(y_test, y_pred_dt),
        'XGBoost': accuracy_score(y_test, y_pred_xgb)
    }
    return metrics
