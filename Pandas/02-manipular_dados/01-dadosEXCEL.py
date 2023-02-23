import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
pagina = 0      # escolhe a página do excel. (tb pode usar o nome da página como índice)
dados = pd.read_excel(arquivo, sheet_name=pagina)        # abre um arquivo EXCEL

print(dados[["open", "close"]]) # mostra apenas as colunas selecionadas