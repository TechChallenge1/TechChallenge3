from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import requests
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine
from Model.previsao_consumo import executar_previsao_consumo
from Model.classificacao_submercado import executar_classificacao_submercado
from Utils.carregar_tabela_bronze import carregar_tabela_bronze

# Criar uma instância do FastAPI
app = FastAPI()

# Modelo para representar a entrada do usuário
class ModeloEscolha(BaseModel):
    opcao: int

# Rota inicial para testar a API
@app.get("/")
async def raiz():
    return {"mensagem": "Bem-vindo à API de Modelos de Consumo e Classificação!"}

# Rota para processar o arquivo CSV da URL e carregar a tabela bronze
@app.get("/buscar_carregar_dados/")
async def processar_csv():
    url = "https://pda-download.ccee.org.br/BPAqGujWQAOczjdrW5-3Yg/content"
    try:
        # Fazer o download do arquivo CSV
        response = requests.get(url)
        response.raise_for_status()
        csv_content = response.content.decode('utf-8')

        # Ler o CSV em um DataFrame
        data = pd.read_csv(StringIO(csv_content), delimiter='\t')
        
        # Processar e carregar os dados na tabela bronze
        carregar_tabela_bronze(data)

        return {"mensagem": "Dados processados e carregados na tabela bronze com sucesso!"}
    except Exception as e:
        return {"erro": f"Erro ao processar o arquivo CSV: {e}"}

# Rota para executar os modelos com base na escolha do usuário
@app.post("/executar_modelo/")
async def executar_modelo(escolha: ModeloEscolha):
    if escolha.opcao == 1:
        try:
            executar_previsao_consumo()
            return {"mensagem": "Modelo de Previsão de Consumo executado com sucesso!"}
        except Exception as e:
            return {"erro": f"Erro ao executar o modelo de previsão: {e}"}
    elif escolha.opcao == 2:
        try:
            executar_classificacao_submercado()
            return {"mensagem": "Modelo de Classificação de Submercados executado com sucesso!"}
        except Exception as e:
            return {"erro": f"Erro ao executar o modelo de classificação: {e}"}
    else:
        return {"erro": "Opção inválida! Escolha 1 para Previsão de Consumo ou 2 para Classificação de Submercados."}
