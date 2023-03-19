import pandas as pd

arq = pd.read_csv("prices.csv", sep=";")        # abre um arquivo EXCEL

arqCopia = arq.copy()       # copia uma dataframe para outro

# Convertendo dados do tipo 'objeto' para 'datatime'
arqCopia["DATA INICIAL"] = pd.to_datetime(arqCopia["DATA INICIAL"])
arqCopia["DATA FINAL"] = pd.to_datetime(arqCopia["DATA FINAL"])
#------------------------------------------------------------

# convertendo objetos para tipo numérico---------------------
lista = ["PREÇO MÉDIO DISTRIBUIÇÃO", "DESVIO PADRÃO DISTRIBUIÇÃO", "PREÇO MÍNIMO DISTRIBUIÇÃO", "PREÇO MÁXIMO DISTRIBUIÇÃO", "COEF DE VARIAÇÃO DISTRIBUIÇÃO"]
for atributo in lista:
    arqCopia[atributo] = pd.to_numeric(arqCopia[atributo], errors="coerce")
'''
errors: {‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
    *raise -> Conversão inválida inválida gerará uma exceção.
    *coerce -> Conversão inválida será definida como NaN.
    *ignore -> não realiza a conversão.
'''
#------------------------------------------------------------

#----Verificando quais valores são NaN-----------------------
eh_NaN = arqCopia["PREÇO MÉDIO DISTRIBUIÇÃO"].isnull()  # retorna "True" caso o valor seja NaN
print('Linhas que não foram convertidas de "object" para "numeric":\n')
print(arq[eh_NaN]["PREÇO MÉDIO DISTRIBUIÇÃO"])        # mostra no dataframe original quais linhas não foram convertidas de 'object' para 'numeric' e seu valor
print('----------------------------------------------------')
print('Valores que não foram convertidas de "object" para "numeric":\n')
print(arq[eh_NaN]["PREÇO MÉDIO DISTRIBUIÇÃO"].unique())        # mostra no dataframe original quais valores não foram convertidas de 'object' para 'numeric'
print('----------------------------------------------------')
#------------------------------------------------------------

#-----removendo linhas do dataframe que possuem valor NaN
arqCopia.dropna(inplace=True)

print(arqCopia.info())