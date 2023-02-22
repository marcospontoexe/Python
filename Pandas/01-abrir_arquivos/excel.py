import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
#codificacao = "UTF-8"   # tipo de codificaçao do arquivo
#separador = ","         # separador usado na separação  dos dados CSV
#cabecalho = 0           # define qual linha será o cabeçalho
#selecionarCol = ["time", "open", "high", "low", "close", "real_volume"] # seleciona quais colunas o dataframe deve possuir
pagina = 0      # escolhe a página do excel
dadosEXCEL = pd.read_excel(arquivo, sheet_name=pagina)        # abre um arquivo EXCEL

print(dadosEXCEL)
