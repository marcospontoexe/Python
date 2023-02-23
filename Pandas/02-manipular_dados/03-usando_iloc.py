import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
pagina = 0      # escolhe a página do excel. (tb pode usar o nome da página como índice)
dados = pd.read_excel(arquivo, sheet_name=pagina)        # abre um arquivo EXCEL

# o "iloc" permite usar apenas números para filtrar linhas e colunas
print(dados.iloc[[1,5,6]]) # mostra apenas as linhas 1, 5 e 6
print(dados.iloc[0:5, 1:3]) # mostra apenas as linhas do índice 0 ao 5, das colunas 1 a 4
print(dados.iloc[[1,3], 0:4]) # mostra apenas a linhas 1 e 3, das colunas 0 até 3
