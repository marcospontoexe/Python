import pandas as pd

#-------criando um dataframe-----------
'''
* O DATAFRAME é uma tabela, com linhas e colunas.
* As colunas são chamadas de SÉRIES. Pode ter apenas um tipo de variável (float, int, boleana...)
* As linhas são chmadasd de REGISTROS, ou AMOSTRAS. Pode conter vários tipos de variáveis (float, int, boleana...)
* Ocabeçalho da tabela é chamado de FEATURES, ATRIBUTO ou VARIÁVEL
'''
df = pd.DataFrame({     # passando um dicionário como parâmetro de entrada do dataframe
    "NOME":["marcos", "edivânia", "leonide", "josivaldo"],           #cada chave do dicionário pade conter mais de um valor (uma lista)
    "IDADE":[32, 56, 78, 92],
    "PESO":[60.3, 49.2, 80.4, 72.4],
    "VIVO":[True, True, True, False]
})
print(df.info())
print(df)

#-------salvando em um csv---------------
df.to_csv("dados.csv", index=False)         # salva sem o índice
