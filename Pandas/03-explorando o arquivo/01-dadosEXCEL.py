import pandas as pd
import os
'''
# ----------------ABRINDO ARQUIVO EXCEL-----------------------------
diretorio_script = os.path.dirname(os.path.realpath(__file__))
arquivo = f"{diretorio_script}/dadosEXCEL.xlsx"   # nome do arquivo

# escolhe a página do excel. (tb pode usar o nome da página como índice)
pagina = 0
# abre um arquivo EXCEL
dados = pd.read_excel(arquivo, sheet_name=pagina)

print(dados[["open", "close"]])  # mostra apenas as colunas selecionadas
print(dados["open"][3])     # mostra o valor da coluna X linha
print('----------------------------------------------------------')
'''
diretorio_script = os.path.dirname(os.path.realpath(__file__))
arquivo = f"{diretorio_script}/nomes.xlsx"   # nome do arquivo

arq = pd.read_excel(arquivo)        # abre um arquivo EXCEL
'''
# retorna a quantidades de linhas com o mesmo "FirstName"
qntd = arq["FirstName"].value_counts()
print(f"quantidade de nomes iguais: \n{qntd}")
# mostra os valores da coluna, sem repetir o mesmo nome
print(f"unique(): \n{arq['FirstName'].unique()}")
print('----------------------------------------------------------')

filtro = arq.FirstName == "John"   # recebe uma série contendo, "True" quando os valores da coluna "FirstName" é "John", e "False" caso contrário
print(f"soma: {sum(filtro * 1)}")    # mostra quantas linhas que contém o valor "John"
print(arq.FirstName[filtro])         # mostra apenas as linhas que contém o valor "John"
print('------------------------------------------------------')
'''
print(f"linhas vazias: \n{(arq[arq['NameStyle'].isnull(
)])}")  # mostra os valores do objeto "dados" em que os índices da coluna "Tipo_Anuncio" estão vazios
print('------------------------------------------------------')

# ---------RENOMEANDO VALORES----------------
print("--------arq------")
print(arq.info())
print("-----arqRenomeado------")
# "arqRenomeado" recebe um dataframe com as aletrações solicitadas
arqRenomeado = arq.rename(
    columns={"FirstName": "Primeiro Nome", "LastName": "Sobrenome"})
print(arqRenomeado.info())
print("--------arq após 'inplace'------")
# faz a alteração no próprio dataframe
arq.rename(columns={"FirstName": "Primeiro Nome",
           "LastName": "Sobrenome"}, inplace=True)
print(arq.info())
