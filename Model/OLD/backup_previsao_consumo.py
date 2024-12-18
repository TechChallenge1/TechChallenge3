import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def executar_previsao_consumo():
    # Carregar o arquivo CSV
    data = pd.read_csv('C:/PROJETOS/FIAP/TechChallenge3/DATA/consumo_horario_submercado_2024.csv', delimiter=';')

    # Pré-processamento dos dados
    data['MES_REFERENCIA'] = data['MES_REFERENCIA'].astype(str)
    data['ANO'] = data['MES_REFERENCIA'].str[:4].astype(int)
    data['MES'] = data['MES_REFERENCIA'].str[4:].astype(int)

    # Selecionar as features (variáveis independentes) e a variável alvo
    features = ['PERIODO_COMERCIALIZACAO', 'MES', 'ANO', 'SUBMERCADO']
    X = data[features]
    y = data['CONSUMO_RECONCILIADO']

    # Codificar a variável categórica 'SUBMERCADO' usando One-Hot Encoding
    X = pd.get_dummies(X, columns=['SUBMERCADO'], drop_first=True)

    # Dividir os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Treinar o modelo Random Forest Regressor
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Fazer previsões no conjunto de teste
    y_pred = rf_model.predict(X_test)

    # Avaliar o modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'Erro Quadrático Médio (MSE): {mse:.2f}')
    print(f'Coeficiente de Determinação (R²): {r2:.4f}')

    # Importância das features
    importances = rf_model.feature_importances_
    feature_names = X.columns
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    print('\nImportância das Features:')
    print(feature_importance_df)

    # Gráfico de Importância das Features
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
    plt.gca().invert_yaxis()
    plt.title('Importância das Variáveis no Random Forest')
    plt.xlabel('Importância')
    plt.ylabel('Variável')
    plt.tight_layout()
    plt.show()

    # Gráfico de Valores Reais vs. Previstos
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.title('Random Forest Regression: Valores Reais vs. Previstos')
    plt.xlabel('Consumo Real (MWh)')
    plt.ylabel('Consumo Previsto (MWh)')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.tight_layout()
    plt.show()

    # Gráfico de Resíduos
    residuos = y_test - y_pred
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuos, alpha=0.5)
    plt.hlines(y=0, xmin=y_pred.min(), xmax=y_pred.max(), colors='r', linestyles='dashed')
    plt.title('Resíduos vs. Valores Previstos')
    plt.xlabel('Consumo Previsto (MWh)')
    plt.ylabel('Resíduos')
    plt.tight_layout()
    plt.show()