import pandas as pd

#----------------ABRINDO ARQUIVO EXCEL-----------------------------
arquivo = "bank.csv"   # nome do arquivo
dados = pd.read_csv(arquivo, sep=";")        # abre um arquivo csv


#----USANDO UMA FUNÇÃO DE AGRUPAMENTO (mean, max, min, sum, describe)----
filtro1 = dados.marital == "married"        # recebe apenas as linhas que contem "married" na coluna "marital" recebem True, e o resto recebe False
print(dados[filtro1])
print(dados[filtro1].age)    # mostra apenasa coluna "age", das linhas que contem "married" na coluna "marital"
print(f"média: {dados[filtro1].age.mean()}")   # mostra a média da filtragem
print('----------------------------------------------')


#------USANDO O MÉTODO GROUPBY-----------------
print(dados[["marital", "education", "age"]].groupby(["marital", "education"]).mean())  # mostra a media de idades das colunas agrupadas "marital" e "education",
print('----------------------------------------------')