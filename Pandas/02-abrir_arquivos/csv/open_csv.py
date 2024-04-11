import pandas as pd
import os

# ----------------ABRINDO ARQUIVO CSV-----------------------------
# arquivo = "..\outra pasta\dadosCSV.csv"   # caminho e nome do arquivo

# Diretório do script atual
diretorio_atual = os.path.dirname(os.path.realpath(__file__))

# Diretório pai do diretório atual
diretorio_anterior = os.path.dirname(diretorio_atual)

arquivo = f"{diretorio_anterior}/dadosCSV.csv"

codificacao = "UTF-8"   # tipo de codificaçao do arquivo
separador = ","         # separador usado na separação  dos dados CSV
cabecalho = 0           # define qual linha será o cabeçalho
# seleciona quais colunas o dataframe deve possuir
selecionarCol = ["time", "open", "high", "low", "close", "real_volume"]
numLinhas = 50      # seleciona quantas linhas o dataframe deve possuir
dadosCSV = pd.read_csv(arquivo, encoding=codificacao, sep=separador, header=cabecalho,
                       usecols=selecionarCol, nrows=numLinhas)        # abre um arquivo CSV


print(dadosCSV)
'''
# mostra as linhas sem repetir o mesmo valor
print(f"UNIQUE: {dadosCSV['time'].unique()}")
# mostra a quantidade de linhas e colunas
print(f"SHAPE: {dadosCSV.shape}")
# mostra a quantidade de dados do Dataframe (linhas X colunas)
print(f"SIZE: {dadosCSV.size}")

# mostra apenas as primeiras linhas do dataframe
print(f"HEAD:\n {dadosCSV.head()}")

# mostra informações sobre o dataframe
print(f"INFORMAÇÕES DO DATAFRAME: \n{dadosCSV.info()}")
'''
# -------Convertendo uma valor do dataframe--------
numero = int(dadosCSV.loc[[0], ["open"]].values)
print(f"OPEN: {numero}")
print(f"tipo do OPEN: {type(numero)}")
