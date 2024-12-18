import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def executar_classificacao_submercado():
    # Carregar o arquivo CSV
    data = pd.read_csv('C:/PROJETOS/FIAP/TechChallenge3/DATA/consumo_horario_submercado_2024.csv', delimiter=';')

    # Pre-processamento dos dados
    data['MES_REFERENCIA'] = data['MES_REFERENCIA'].astype(str)
    data['ANO'] = data['MES_REFERENCIA'].str[:4].astype(int)
    data['MES'] = data['MES_REFERENCIA'].str[4:].astype(int)

    # Selecionar as features (variáveis independentes) e a variável alvo
    features = ['PERIODO_COMERCIALIZACAO', 'MES', 'ANO', 'CONSUMO_RECONCILIADO']
    X = data[features]
    y = data['SUBMERCADO']

    # Dividir os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Treinar o modelo Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Fazer previsões no conjunto de teste
    y_pred = rf_classifier.predict(X_test)

    # Avaliar o modelo
    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred))

    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    # Importância das features
    importances = rf_classifier.feature_importances_
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

    # Gráfico de Matriz de Confusão
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Matriz de Confusão')
    plt.colorbar()
    tick_marks = np.arange(len(rf_classifier.classes_))
    plt.xticks(tick_marks, rf_classifier.classes_, rotation=45)
    plt.yticks(tick_marks, rf_classifier.classes_)
    plt.ylabel('Valor Real')
    plt.xlabel('Valor Previsto')

    # Anotar os valores na matriz
    thresh = conf_matrix.max() / 2.
    for i, j in np.ndindex(conf_matrix.shape):
        plt.text(j, i, format(conf_matrix[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if conf_matrix[i, j] > thresh else "black")

    plt.tight_layout()
    plt.show()
