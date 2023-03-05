import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "nomes.xlsx"   # nome do arquivo
arq = pd.read_excel(arquivo)        # abre um arquivo EXCEL

dados = arq.loc[:30,["FirstName", "LastName"]]  # recebe apenas as colunas e linhas filtradas
print(dados.sort_values(["FirstName", "LastName"]))     # ordena em ordem crescente, a primeira coluna selecionada e depois a segunda coluna selecionada
print(dados.sort_values(["FirstName", "LastName"], ascending=[True, False]))     # ordena a primeira coluna em ordem crescente, e a segunda coluna selecionada em ordem decrescente
print('----------------------------------------------')

#------OPERAÇÕES ENTRE COLUNAS (SÉRIES)-------------------
print(dados)
print('----------------------------------------------')
dados["NOME+SOBRENOME"] = dados.FirstName + ' ' + dados.LastName
print(dados)