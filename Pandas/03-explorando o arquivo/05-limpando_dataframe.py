import pandas as pd
import os

diretorio_script = os.path.dirname(os.path.realpath(__file__))
arquivo = f"{diretorio_script}/prices.csv"      # nome do arquivo
arq = pd.read_csv(arquivo, sep=";")        # abre um arquivo EXCEL

arqCopia = arq.copy()       # copia uma dataframe para outro

# Convertendo dados do tipo 'objeto' para 'datatime'
arqCopia["DATA INICIAL"] = pd.to_datetime(arqCopia["DATA INICIAL"])
arqCopia["DATA FINAL"] = pd.to_datetime(arqCopia["DATA FINAL"])
# ------------------------------------------------------------

print(arqCopia.info())
# convertendo objetos para tipo numérico---------------------
lista = ["PREÇO MÉDIO DISTRIBUIÇÃO", "DESVIO PADRÃO DISTRIBUIÇÃO",
         "PREÇO MÍNIMO DISTRIBUIÇÃO", "PREÇO MÁXIMO DISTRIBUIÇÃO", "COEF DE VARIAÇÃO DISTRIBUIÇÃO"]
for atributo in lista:
    arqCopia[atributo] = pd.to_numeric(arqCopia[atributo], errors="coerce")

print(arqCopia.info())
'''
errors: {‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
    *raise -> Conversão inválida inválida gerará uma exceção.
    *coerce -> Conversão inválida será definida como NaN.
    *ignore -> não realiza a conversão.
'''
# ------------------------------------------------------------

# ----Verificando quais valores são NaN-----------------------
# retorna "True" caso o valor seja NaN
eh_NaN = arqCopia["PREÇO MÉDIO DISTRIBUIÇÃO"].isnull()
print('Linhas que não foram convertidas de "object" para "numeric":\n')
# mostra no dataframe original quais linhas não foram convertidas de 'object' para 'numeric' e seu valor
print(arq[eh_NaN]["PREÇO MÉDIO DISTRIBUIÇÃO"])
print('----------------------------------------------------')
print('Valores que não foram convertidas de "object" para "numeric":\n')
# mostra no dataframe original quais valores não foram convertidas de 'object' para 'numeric'
print(arq[eh_NaN]["PREÇO MÉDIO DISTRIBUIÇÃO"].unique())
print('----------------------------------------------------')
# ------------------------------------------------------------

# -----removendo linhas do dataframe que possuem valor NaN
arqCopia.dropna(inplace=True)

print(arqCopia.info())
