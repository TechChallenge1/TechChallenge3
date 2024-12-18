-- Tabela para resultados de classificação de submercados
--drop table gold.resultados_classificacao
CREATE TABLE gold.resultados_classificacao (
    id SERIAL PRIMARY KEY,
    valor_real VARCHAR(50),
    valor_previsto VARCHAR(50),
    importancia_feature JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Tabela para resultados de previsão de consumo
--drop table resultados_previsao
CREATE TABLE gold.resultados_previsao (
    id SERIAL PRIMARY KEY,
    valor_real NUMERIC,
    valor_previsto NUMERIC,
    residuos NUMERIC,
    importancia_feature JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from gold.resultados_classificacao;
select * from gold.resultados_previsao;

-------------------------------------------------------------



-- Tabela para Resultados da Classificação (classificacao_resultados)
drop table gold.classificacao_resultados;
CREATE TABLE gold.classificacao_resultados (
    id SERIAL PRIMARY KEY,              -- Chave primária com incremento automático
    real VARCHAR(255) NOT NULL,         -- Valor real da classificação
    previsto VARCHAR(255) NOT NULL,     -- Valor previsto pelo modelo
    execution_timestamp TIMESTAMP DEFAULT NOW() -- Timestamp de execução
);

-- Tabela para Importância de Features da Classificação (classificacao_importancia_features)
drop table gold.classificacao_importancia_features;
CREATE TABLE gold.classificacao_importancia_features (
    id SERIAL PRIMARY KEY,              -- Chave primária com incremento automático
    feature VARCHAR(255) NOT NULL,      -- Nome da variável (feature)
    importance FLOAT NOT NULL,          -- Importância da variável
    execution_timestamp TIMESTAMP DEFAULT NOW() -- Timestamp de execução
);

-- Tabela para Resultados da Previsão de Consumo (previsao_consumo_resultados)
drop table gold.previsao_consumo_resultados;
CREATE TABLE gold.previsao_consumo_resultados (
    id SERIAL PRIMARY KEY,               -- Chave primária com incremento automático
    consumo_real FLOAT NOT NULL,         -- Valor real do consumo
    consumo_previsto FLOAT NOT NULL,     -- Valor previsto pelo modelo
    execution_timestamp TIMESTAMP DEFAULT NOW() -- Timestamp de execução
);

-- Tabela para Importância de Features da Previsão de Consumo (previsao_consumo_importancia_features)
drop table gold.previsao_consumo_importancia_features;
CREATE TABLE gold.previsao_consumo_importancia_features (
    id SERIAL PRIMARY KEY,               -- Chave primária com incremento automático
    feature VARCHAR(255) NOT NULL,       -- Nome da variável (feature)
    importance FLOAT NOT NULL,           -- Importância da variável
    execution_timestamp TIMESTAMP DEFAULT NOW() -- Timestamp de execução
);

select * from gold.classificacao_resultados;
select * from gold.classificacao_importancia_features;
select * from gold.previsao_consumo_resultados;
select * from  gold.previsao_consumo_importancia_features;










