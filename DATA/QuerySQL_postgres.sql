-- Criando a tabela SQL que vai comportar os dados que foram carregadors da tabela origem
--drop table public.consumo_energia_submercado_2024;
--create schema bronze;
--create schema silver;
--create schema gold;

--DROP TABLE bronze.consumo_energia_submercado_2024;
CREATE TABLE bronze.consumo_energia_submercado_2024 (
    submercado VARCHAR(50),
    mes_referencia INT,
    periodo_comercializacao INT,
    consumo_reconciliado FLOAT,
    consumo_geracao FLOAT
);
--DROP TABLE bronze.consumo_energia_submercado_2023;
CREATE TABLE bronze.consumo_energia_submercado_2023 (
    submercado VARCHAR(50),
    mes_referencia INT,
    periodo_comercializacao INT,
    consumo_reconciliado FLOAT,
    consumo_geracao FLOAT
);

--DROP table gold.consumo_energia_submercado;
CREATE TABLE gold.consumo_energia_submercado (
    submercado VARCHAR(50),
    mes_referencia INT,
    periodo_comercializacao INT,
    consumo_reconciliado FLOAT,
    consumo_geracao FLOAT
);

COPY bronze.consumo_energia_submercado_2024(submercado, mes_referencia, periodo_comercializacao, consumo_reconciliado, consumo_geracao)
FROM 'C:/PROJETOS/FIAP/TechChallenge3/DATA/consumo_horario_submercado_2024.csv'
DELIMITER ';'
CSV HEADER;

COPY bronze.consumo_energia_submercado_2023(submercado, mes_referencia, periodo_comercializacao, consumo_reconciliado, consumo_geracao)
FROM 'C:/PROJETOS/FIAP/TechChallenge3/DATA/consumo_horario_submercado_2023.csv'
DELIMITER ';'
CSV HEADER;

select * from bronze.consumo_energia_submercado_2024;
select * from bronze.consumo_energia_submercado_2023;

select
Max(c.periodo_comercializacao) as maximo,
min(c.periodo_comercializacao) as minimo
from bronze.consumo_energia_submercado_2023 c;



---------------------------------------------
---------------------------------------------
---------------------------------------------

-- Tabela Silver: Consolidação de consumo por submercado e mês
CREATE TABLE IF NOT EXISTS SILVER.consumo_energia_submercado_2024_aggregated (
    submercado VARCHAR(50),
    mes_referencia INT,
    consumo_total_reconciliado FLOAT,
    consumo_total_geracao FLOAT
);


-------------------------------------------
-------------------------------------------
-------------------------------------------
CREATE OR REPLACE PROCEDURE processar_dados_silver()
LANGUAGE plpgsql
AS
$$
BEGIN
    -- Limpa os dados anteriores da tabela silver (se necessário)
    TRUNCATE TABLE SILVER.consumo_energia_submercado_2024_aggregated;

    -- Insere dados agregados da tabela bronze na tabela silver
    INSERT INTO SILVER.consumo_energia_submercado_2024_aggregated (submercado, mes_referencia, consumo_total_reconciliado, consumo_total_geracao)
    SELECT
        submercado,
        mes_referencia,
        SUM(consumo_reconciliado) AS consumo_total_reconciliado,
        SUM(consumo_geracao) AS consumo_total_geracao
    FROM
        BRONZE.consumo_energia_submercado_2024
    GROUP BY
        submercado, mes_referencia;

    RAISE NOTICE 'Dados processados e inseridos na tabela Silver.';
END;
$$;


-------------------------------------------
-------------------------------------------
-------------------------------------------

-- Tabela Gold: Tabela otimizada para análise no Data Warehouse
CREATE TABLE IF NOT EXISTS GOLD.consumo_energia_submercado_2024_dw (
    submercado VARCHAR(50),
    mes_referencia INT,
    consumo_total_reconciliado FLOAT,
    consumo_total_geracao FLOAT,
    consumo_medio_reconciliado FLOAT,
    consumo_medio_geracao FLOAT
);

-------------------------------------------
-------------------------------------------
-------------------------------------------

CREATE OR REPLACE PROCEDURE processar_dados_gold()
LANGUAGE plpgsql
AS
$$
BEGIN
    -- Limpa os dados anteriores da tabela gold (se necessário)
    TRUNCATE TABLE GOLD.consumo_energia_submercado_2024_dw;
	TRUNCATE TABLE GOLD.consumo_energia_submercado;
	
    -- Insere os dados agregados na tabela gold, com métricas calculadas
    INSERT INTO GOLD.consumo_energia_submercado_2024_dw (submercado, mes_referencia, consumo_total_reconciliado, consumo_total_geracao, consumo_medio_reconciliado, consumo_medio_geracao)
    SELECT
        submercado,
        mes_referencia,
        SUM(consumo_total_reconciliado) AS consumo_total_reconciliado,
        SUM(consumo_total_geracao) AS consumo_total_geracao,
        AVG(consumo_total_reconciliado) AS consumo_medio_reconciliado,
        AVG(consumo_total_geracao) AS consumo_medio_geracao
    FROM
        SILVER.consumo_energia_submercado_2024_aggregated
    GROUP BY
        submercado, mes_referencia;
	
	---------------
	insert into gold.consumo_energia_submercado (submercado,mes_referencia,periodo_comercializacao,consumo_reconciliado,consumo_geracao)
	select * from bronze.consumo_energia_submercado_2024
	union
	select * from bronze.consumo_energia_submercado_2023;
	

    RAISE NOTICE 'Dados processados e inseridos na tabela Gold.';
END;
$$;

-------------------------------------------
-------------------------------------------
-------------------------------------------

-- Executa a procedure de transformação para a tabela Silver
CALL processar_dados_silver();

-- Executa a procedure de transformação para a tabela Gold
CALL processar_dados_gold();


