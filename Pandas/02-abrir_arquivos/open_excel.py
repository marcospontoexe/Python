import pandas as pd
import os

# Para abrir excel é necessário instalar a biblioteca openpyxl
# ----------------ABRINDO ARQUIVO EXCEL-----------------------------
diretorio_script = os.path.dirname(os.path.realpath(__file__))
arquivo = f"{diretorio_script}/dadosEXCEL.xlsx"   # nome do arquivo
# escolhe a página do excel. (tb pode usar o nome da página como índice)
pagina = 1
# abre um arquivo EXCEL
dados = pd.read_excel(arquivo, sheet_name=pagina)

print(dados)

# ---------VERIFICANDO O NOME DAS PÁGINAS DO EXCEL-----------------
arq = pd.ExcelFile(arquivo)     # abre um arquivo em excel
print(arq.sheet_names)     # retorna uma lista com os nomes das páginas do excel
