----------------------------------

DROP TABLE gold.dim_periodo_comercializacao;
CREATE TABLE gold.dim_periodo_comercializacao (
    id_dim_periodo_comercializacao serial,
	periodo_comercializacao INT,
    dia_do_mes INT,
    hora_do_dia INT,
    minuto_do_dia INT
);

-- Inserir dados na tabela dimension_periodo_comercializacao
DO $$
DECLARE
    periodo INT;
    dia INT;
    hora INT;
    minuto INT;
BEGIN
    -- Loop para percorrer os períodos de 1 a 744
    FOR periodo IN 1..744 LOOP
        -- Calcular o dia (1 a 31) considerando 96 períodos por dia
        dia := (periodo - 1) / 96 + 1;

        -- Calcular a hora do dia (0 a 23), considerando 4 períodos por hora
        hora := (periodo - 1) / 4 % 24;

        -- Calcular o minuto do dia (0, 15, 30, 45)
        minuto := ((periodo - 1) % 4) * 15;

        -- Inserir os dados calculados na tabela
        INSERT INTO gold.dim_periodo_comercializacao (periodo_comercializacao, dia_do_mes, hora_do_dia, minuto_do_dia)
        VALUES (periodo, dia, hora, minuto);
    END LOOP;
END $$;

SELECT * FROM gold.dim_periodo_comercializacao
