import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "dadosEXCEL.xlsx"   # nome do arquivo
pagina = 0      # escolhe a página do excel. (tb pode usar o nome da página como índice)
dados = pd.read_excel(arquivo, sheet_name=pagina)        # abre um arquivo EXCEL

print(dados[["open", "close"]]) # mostra apenas as colunas selecionadas
print(dados["open"][3])     # mostra o valor da coluna X linha
print('----------------------------------------------------------')

arquivo = "nomes.xlsx"   # nome do arquivo
arq = pd.read_excel(arquivo)        # abre um arquivo EXCEL
qntd = arq["FirstName"].value_counts()        #retorna a quantidades de linhas com o mesmo "FirstName"
print(f"quantidade de nomes iguais: \n{qntd}")
print(f"unique(): \n{arq['FirstName'].unique()}")   #mostra os valores da coluna, sem repetir o mesmo nome
print('----------------------------------------------------------')

filtro = arq.FirstName == "John"   # recebe uma série contendo, "True" quando os valores da coluna "FirstName" é "John", e "False" caso contrário
print(f"soma: {sum(filtro * 1)}")    # mostra quantas linhas que contém o valor "John"
print(arq.FirstName[filtro])         # mostra apenas as linhas que contém o valor "John"
print('------------------------------------------------------')

print(f"linhas vazias: \n{(arq[arq['NameStyle'].isnull()])}")  #mostra os valores do objeto "dados" em que os índices da coluna "Tipo_Anuncio" estão vazios



