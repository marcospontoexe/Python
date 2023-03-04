import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
pagina = 0      # escolhe a página do excel. (tb pode usar o nome da página como índice)
dados = pd.read_excel(arquivo, sheet_name=pagina)        # abre um arquivo EXCEL

# o filter permite realizar busca mais avançada (é possível usar o regex)
print(dados.filter(items=["open", "close"])) # mostra as colunas solicitadas
print(dados.filter(like="o"))       # mostra todas as colunas que contem a letra 'o' no cabeçalho
print(dados.filter(regex=".os."))       # mostra todas as colunas que contem "qualquer letra" + "o" + "qualquer letra" no cabeçalho