import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine

def carregar_tabela_bronze(data: pd.DataFrame):
    """
    Carrega os dados em uma tabela bronze no PostgreSQL e chama as procedures para processar os dados silver e gold.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados processados.
    """
    # Configuração do banco de dados
    db_user = "postgres"
    db_password = "12092020"
    db_host = "localhost"
    db_port = "5432"
    db_name = "tech_challenge_3"

    try:
        # Configurar a conexão com o banco de dados PostgreSQL
        engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

        # Carregar os dados na tabela bronze
        print("Carregando dados na tabela bronze...")
        data.to_sql('tabela_bronze', engine, if_exists='replace', index=False)
        
        # Verificar se os dados foram carregados com sucesso
        print("Dados carregados na tabela bronze com sucesso!")

        # Chamar as procedures no banco de dados
        print("Chamando as procedures para processar os dados silver e gold...")
        with engine.connect() as connection:
            connection.execute(text("CALL processar_dados_silver();"))
            connection.execute(text("CALL processar_dados_gold();"))
            connection.commit()  # Certifique-se de chamar o commit

        print("Procedures executadas com sucesso!")

    except Exception as e:
        print(f"Erro ao carregar dados na tabela bronze ou executar procedures: {e}")
