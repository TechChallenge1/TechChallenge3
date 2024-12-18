import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


# Configuração do banco de dados
db_user = "postgres"
db_password = "12092020"
db_host = "localhost"
db_port = "5432"
db_name = "tech_challenge_3"

# Criar a engine do SQLAlchemy
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Consultar os dados diretamente do PostgreSQL
query = """
SELECT 
    submercado, 
    mes_referencia, 
    periodo_comercializacao, 
    consumo_reconciliado 
FROM 
    gold.consumo_energia_submercado
"""
try:
    data = pd.read_sql(query, engine)
    print("Dados lidos com sucesso!")
except Exception as e:
    print(f"Erro ao ler os dados do banco: {e}")

# Verificar e ajustar as colunas do DataFrame
data.columns = data.columns.str.upper()

if 'MES_REFERENCIA' not in data.columns:
    print("Coluna MES_REFERENCIA não encontrada no DataFrame.")


# Pré-processamento dos dados
data['MES_REFERENCIA'] = data['MES_REFERENCIA'].astype(str)
data['ANO'] = data['MES_REFERENCIA'].str[:4].astype(int)
data['MES'] = data['MES_REFERENCIA'].str[4:].astype(int)

# Selecionar as features (variáveis independentes) e a variável alvo
features = ['PERIODO_COMERCIALIZACAO', 'MES', 'ANO', 'SUBMERCADO']
if not all(col in data.columns for col in features):
    print("Nem todas as colunas necessárias estão disponíveis no DataFrame.")


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

# Preparar os resultados para salvar no banco
results_df = pd.DataFrame({
    'Consumo_Real': y_test.values,
    'Consumo_Previsto': y_pred
})

importances = rf_model.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
feature_importance_df['Execution_Timestamp'] = pd.Timestamp.now()

# Salvar os resultados no PostgreSQL
try:
    results_df.to_sql('previsao_consumo_resultados', engine, schema='gold', if_exists='replace', index=False)
    feature_importance_df.to_sql('previsao_consumo_importancia_features', engine, schema='gold', if_exists='replace', index=False)
    print("Resultados da previsão salvos no PostgreSQL com sucesso.")
except Exception as e:
    print(f"Erro ao salvar os resultados no PostgreSQL: {e}")

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


