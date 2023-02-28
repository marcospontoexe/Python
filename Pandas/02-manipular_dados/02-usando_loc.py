import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
pagina = 0      # escolhe a página do excel. (tb pode usar o nome da página como índice)
dados = pd.read_excel(arquivo, sheet_name=pagina)        # abre um arquivo EXCEL

# o "loc" permite usar string para filtrar linhas e colunas
print(dados.loc[[1,5,6]]) # mostra apenas as linhas 1, 5 e 10
print(dados.loc[:, ["open", "close"]]) # mostra todas as linhas das colunas selecionadas
print(dados.loc[[1,3], "time": "low"]) # mostra apenas a linhas 1 e 3, das coluna "time", até "low"
print(dados.loc[1:3, "time": "low"]) # mostra apenas a linhas 1 ate 3, das coluna "time", até "low"

#-----usando operação lógica---------------
nome = "nomes.xlsx"
arq = pd.read_excel(nome)        # abre um arquivo EXCEL

print(arq.loc[0:, [True, False, True, False, False, False, False, False, False]])     # mostra apenas a coluna 0 e 2

names = arq.loc[0:,["FirstName", "LastName"]]  # recebe apenas as colunas "FirstName" e "LastName"
filtro = arq["FirstName"] == "Andrew"       # "filtro" recebe "True" quando as linhas da coluna "FirstName" contem "Andrew"
print(names[filtro])            # mostra apenas as linhas que contém "True" na coluna "FirstName"

