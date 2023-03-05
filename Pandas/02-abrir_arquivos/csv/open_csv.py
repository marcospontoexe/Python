import pandas as pd

#----------------ABRINDO ARQUIVO CSV-----------------------------
arquivo = "..\outra pasta\dadosCSV.csv"   # caminho e nome do arquivo
codificacao = "UTF-8"   # tipo de codificaçao do arquivo
separador = ","         # separador usado na separação  dos dados CSV
cabecalho = 0           # define qual linha será o cabeçalho
selecionarCol = ["time", "open", "high", "low", "close", "real_volume"] # seleciona quais colunas o dataframe deve possuir
numLinhas = 50      # seleciona quantas linhas o dataframe deve possuir
dadosCSV = pd.read_csv(arquivo, encoding=codificacao, sep=separador, header=cabecalho, usecols=selecionarCol, nrows=numLinhas)        # abre um arquivo CSV

print(dadosCSV)
print(f"SHAPE: {dadosCSV.shape}")              # mostra a quantidade de linhas e colunas
print(f"SIZE: {dadosCSV.size}")             # mostra a quantidade de dados do Dataframe (linhas X colunas)
print(f"HEAD: {dadosCSV.head()}")              # mostra apenas as primeiras linhas do dataframe
print(f"INFORMAÇÕES DO DATAFRAME: \n{dadosCSV.info()}")        # mostra informações sobre o dataframe


