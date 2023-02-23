import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
pagina = 1      # escolhe a página do excel. (tb pode usar o nome da página como índice)
dados = pd.read_excel(arquivo, sheet_name=pagina)        # abre um arquivo EXCEL

print(dados)

#---------VERIFICANDO O NOME DAS PÁGINAS DO EXCEL-----------------
arq = pd.ExcelFile(arquivo)     # abre um arquivo em excel
print(arq.sheet_names)     # retorna uma lista com os nomes das páginas do excel

