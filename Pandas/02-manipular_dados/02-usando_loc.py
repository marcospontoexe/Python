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
