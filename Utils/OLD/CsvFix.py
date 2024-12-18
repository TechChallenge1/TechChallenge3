import pandas as pd
import os


# -------- COMEÇANDO O CÓDIGO PARA O ARQUIVO: Comercio --------

# Função para criar coluna de categoria
def categorize(df):
    current_category = None
    categories = []

    for _, row in df.iterrows():
        produto = row['Produto'].strip()
        if produto.isupper():  # Verifica se todas as letras são maiúsculas
            current_category = produto
            categories.append(current_category)
        elif produto.istitle():  # Verifica se apenas a primeira letra é maiúscula
            categories.append(current_category)
        else:
            categories.append(None)  # Caso nenhuma condição seja atendida

    df['Categoria'] = categories
    return df
print(f'Buscando o arquivo para realizar o ETL')
# Definir o caminho absoluto do arquivo CSV
file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\data\Comercio.csv'

# Verificar se o arquivo existe
if os.path.exists(file_path):
    # Ler o arquivo CSV
    data = pd.read_csv(file_path, delimiter=';')

    # Aplicar a função
    data = categorize(data)

    # Definir o caminho absoluto do arquivo de saída
    output_file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\CsvFix\comercio.csv'

    # Verificar se o diretório existe, se não, criar
    output_dir = os.path.dirname(output_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Salvar o DataFrame atualizado em um novo arquivo CSV
    data.to_csv(output_file_path, index=False, sep=';')

    print(f"Arquivo salvo em: {output_file_path}")
else:
    print(f"O arquivo {file_path} não foi encontrado.")

# -------------------------------------------------------------------------------

# -------- COMEÇANDO O CÓDIGO PARA O ARQUIVO: Producao --------

# Função para criar coluna de categoria
def categorize_producao(df):
    current_category = None
    categories = []

    for _, row in df.iterrows():
        produto = row['produto'].strip()
        if produto.isupper():  # Verifica se todas as letras são maiúsculas
            current_category = produto
            categories.append(current_category)
        elif produto.istitle():  # Verifica se apenas a primeira letra é maiúscula
            categories.append(current_category)
        else:
            categories.append(None)  # Caso nenhuma condição seja atendida

    df['Categoria'] = categories
    return df

# Definir o caminho absoluto do arquivo CSV
file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\data\Producao.csv'

print(f"Tentando acessar o arquivo: {file_path}")

# Verificar se o arquivo existe
if os.path.exists(file_path):
    print("Arquivo encontrado. Lendo o arquivo CSV...")
    
    # Ler o arquivo CSV
    data = pd.read_csv(file_path, delimiter=';')
    
    # Print para verificar as colunas disponíveis no DataFrame
    print(f"Colunas do DataFrame: {data.columns.tolist()}")

    if 'produto' in data.columns:
        print("A coluna 'produto' foi encontrada. Aplicando a função de categorização...")
        
        # Aplicar a função
        data = categorize_producao(data)
        
        print("Função de categorização aplicada com sucesso.")

        # Definir o caminho absoluto do arquivo de saída
        output_file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\CsvFix\Producao.csv'

        print(f"Verificando se o diretório de saída existe: {os.path.dirname(output_file_path)}")

        # Verificar se o diretório existe, se não, criar
        output_dir = os.path.dirname(output_file_path)
        if not os.path.exists(output_dir):
            print("Diretório de saída não encontrado. Criando o diretório...")
            os.makedirs(output_dir)
        
        print("Salvando o DataFrame atualizado em um novo arquivo CSV...")
        
        # Salvar o DataFrame atualizado em um novo arquivo CSV
        data.to_csv(output_file_path, index=False, sep=';')

        print(f"Arquivo salvo com sucesso em: {output_file_path}")
    else:
        print(f"A coluna 'produto' não foi encontrada no arquivo {file_path}.")
else:
    print(f"O arquivo {file_path} não foi encontrado.")
    
# ---------------------------------------------------------------------------------------

# -------- COMEÇANDO O CÓDIGO PARA O ARQUIVO: ProcessaViniferas --------

def categorize_cultivar(df):
    current_category = None
    categories = []

    for _, row in df.iterrows():
        cultivar = row['cultivar'].strip()
        if cultivar.isupper():  # Verifica se todas as letras são maiúsculas
            current_category = cultivar
            categories.append(current_category)
        elif cultivar.istitle():  # Verifica se apenas a primeira letra é maiúscula
            categories.append(current_category)
        else:
            categories.append(None)  # Caso nenhuma condição seja atendida

    df['Categoria'] = categories
    return df

# Definir o caminho absoluto do arquivo CSV
file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\data\ProcessaViniferas.csv'

print(f"Tentando acessar o arquivo: {file_path}")

# Verificar se o arquivo existe
if os.path.exists(file_path):
    print("Arquivo encontrado. Lendo o arquivo CSV...")
    
    # Ler o arquivo CSV
    data = pd.read_csv(file_path, delimiter='\t')  # Ajustar o delimitador conforme necessário
    
    # Print para verificar as colunas disponíveis no DataFrame
    print(f"Colunas do DataFrame: {data.columns.tolist()}")

    if 'cultivar' in data.columns:
        print("A coluna 'cultivar' foi encontrada. Aplicando a função de categorização...")
        
        # Aplicar a função
        data = categorize_cultivar(data)
        
        print("Função de categorização aplicada com sucesso.")

        # Definir o caminho absoluto do arquivo de saída
        output_file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\CsvFix\ProcessaViniferas.csv'

        print(f"Verificando se o diretório de saída existe: {os.path.dirname(output_file_path)}")

        # Verificar se o diretório existe, se não, criar
        output_dir = os.path.dirname(output_file_path)
        if not os.path.exists(output_dir):
            print("Diretório de saída não encontrado. Criando o diretório...")
            os.makedirs(output_dir)
        
        print("Salvando o DataFrame atualizado em um novo arquivo CSV...")
        
        # Salvar o DataFrame atualizado em um novo arquivo CSV
        data.to_csv(output_file_path, index=False, sep='\t')  # Ajustar o delimitador conforme necessário

        print(f"Arquivo salvo com sucesso em: {output_file_path}")
    else:
        print(f"A coluna 'cultivar' não foi encontrada no arquivo {file_path}.")
else:
    print(f"O arquivo {file_path} não foi encontrado.")


# ---------------------------------------------------------------------

# -------- COMEÇANDO O CÓDIGO PARA O ARQUIVO: ProcessaViniferas_Ajustado --------

# Carregar o dataset com o delimitador correto (tabulação)
file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\CsvFix\ProcessaViniferas.csv'
df = pd.read_csv(file_path, sep='\t')  # Use '\t' como delimitador

# Imprimir os nomes das colunas para verificação
print("Nomes das colunas:")
print(df.columns)

# Remover espaços extras no início e fim dos nomes das colunas
df.columns = df.columns.str.strip()

# Imprimir os nomes das colunas após remoção de espaços
print("\nNomes das colunas após remoção de espaços:")
print(df.columns)

# Transformar o dataframe
df_melted = df.melt(id_vars=['id', 'control', 'cultivar', 'Categoria'], 
                    var_name='Ano', 
                    value_name='Valor')

# Reordenar e limpar o dataframe
df_melted = df_melted[['id', 'control', 'cultivar', 'Ano', 'Valor', 'Categoria']]

# Garantir que a coluna 'Ano' seja numérica
df_melted['Ano'] = pd.to_numeric(df_melted['Ano'], errors='coerce')

# Salvar o dataframe transformado
output_file_path = r'C:\PROJETOS\FIAP\TechChallenge1\data\vitivinicultura\CsvFix\ProcessaViniferas_ajustado.csv'
df_melted.to_csv(output_file_path, index=False, sep=';')

print("Transformação concluída com sucesso!")
