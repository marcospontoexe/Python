import pandas as pd

#-------criando um dataframe-----------
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
