import pandas as pd

# ----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
# escolhe a página do excel. (tb pode usar o nome da página como índice)
pagina = 0
# abre um arquivo EXCEL
dados = pd.read_excel(arquivo, sheet_name=pagina)

# o filter permite realizar busca mais avançada (é possível usar o regex)
print(dados.filter(items=["open", "close"]))  # mostra as colunas solicitadas
# mostra todas as colunas que contem a letra 'o' no cabeçalho
print(dados.filter(like="o"))
# mostra todas as colunas que contem "qualquer letra" + "os" + "qualquer letra" no cabeçalho
print(dados.filter(regex=".os."))
