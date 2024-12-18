# Projeto de Machine Learning para Análise de Consumo de Energia

Este projeto tem como objetivo aplicar técnicas de Machine Learning para realizar a previsão de consumo de energia e a classificação de submercados utilizando dados de consumo energético. Ele foi desenvolvido como parte de um trabalho acadêmico e pode ser usado como referência para projetos similares no setor de energia.

## Visão Geral

### 1. Previsão de Consumo de Energia

Utilizando um modelo de regressão (Random Forest Regressor), foi possível prever o consumo de energia com base em variáveis como o período de comercialização, mês, ano e submercado.

**Métricas de desempenho:**
- Erro Quadrático Médio (MSE): 591.546,09
- Coeficiente de Determinação (R²): 0,9968

### 2. Classificação de Submercados

Um modelo de classificação (Random Forest Classifier) foi treinado para identificar a qual submercado os registros pertencem, considerando características como consumo de energia e período de comercialização.

**Métricas de desempenho:**
- Acurácia: 84%
- **F1-Score:**
  - NORDESTE: 0.72
  - NORTE: 0.97
  - SUDESTE: 1.00
  - SUL: 0.69

## Estrutura do Projeto

Estrutura do Projeto
├── utils/
│ ├── previsao_consumo.py
│ ├── classificacao_submercado.py
├── main.py
├── README.md
├── requirements.txt
├── consumo_horario_submercado_2024.csv


## Arquivos

- **previsao_consumo.py**: Contém o código para o modelo de previsão de consumo utilizando Random Forest Regressor.
- **classificacao_submercado.py**: Implementa o modelo de classificação para prever o submercado de um registro utilizando Random Forest Classifier.
- **main.py**: Arquivo principal para execução dos modelos. Possui uma interface que permite ao usuário escolher qual modelo executar.
- **requirements.txt**: Lista de dependências necessárias para executar o projeto.
- **consumo_horario_submercado_2024.csv**: Base de dados utilizada no treinamento e avaliação dos modelos.

## Como Executar o Projeto


Execute o arquivo main.py para iniciar o programa:

''' $ python main.py

Você será solicitado a escolher entre as opções de modelos:

Previsão de Consumo de Energia
Classificação de Submercados

Siga as instruções no terminal para visualizar os resultados.

## Base de Dados
-Descrição
O dataset contém informações de consumo energético organizadas por submercado, mês de referência e período de comercialização. As principais colunas utilizadas nos modelos incluem:

- MES_REFERENCIA: Mês e ano do registro no formato AAAAMM.
- PERIODO_COMERCIALIZACAO: Período em que o consumo foi registrado.
- CONSUMO_RECONCILIADO: Valor do consumo energético registrado.
- SUBMERCADO: Submercado de energia associado ao registro (NORTE, NORDESTE, SUDESTE, SUL).

## Resultados
- Previsão de Consumo de Energia
O modelo apresentou alta precisão, com um coeficiente de determinação (R²) de 99,68%, mostrando que ele é capaz de prever o consumo energético com grande acurácia.

- Classificação de Submercados
O modelo alcançou uma acurácia geral de 84%. O desempenho foi excelente para os submercados "Sudeste" e "Norte", mas houve maior dificuldade em distinguir entre "Nordeste" e "Sul" devido à similaridade nas características dos dados.

## Melhorias Futuras
Aprimorar a Classificação: Usar mais dados históricos e incluir variáveis adicionais que possam ajudar a distinguir melhor os submercados "Nordeste" e "Sul".
Expansão do Dataset: Adicionar novos períodos ou dados externos (como condições climáticas ou demográficas) para aumentar a precisão dos modelos.
Explorar Outros Modelos: Testar algoritmos diferentes como Gradient Boosting ou XGBoost para comparar resultados.

## Dependências
As bibliotecas utilizadas no projeto incluem:

- pandas
- numpy
- matplotlib
- scikit-learn
As versões específicas podem ser encontradas no arquivo requirements.txt.

## Licença
Este projeto foi desenvolvido para fins acadêmicos e pode ser utilizado como referência. Sinta-se à vontade para adaptá-lo e expandi-lo conforme necessário.

## Dashboard
Esse projeto alimenta um Dashboard que foi criado em Power BI e está disponivel aqui no GitHub, além de também estar disponivel em uma URL publica:
- Link: https://app.powerbi.com/view?r=eyJrIjoiNWUwYjdjY2YtZTNhMi00NTEyLWJhMWMtYWZhYWEwZDc0ZWIwIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9
- 
  

## Video Explicativo
Existe um video no youtube explicando a solução com o objetivo acadêmico
- Link: https://youtu.be/HT5oqya--q8
- 
