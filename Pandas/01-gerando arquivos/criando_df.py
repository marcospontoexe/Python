import pandas as pd
import os

# -------criando um dataframe-----------
'''
* O DATAFRAME é uma tabela, com linhas e colunas.
* As colunas são chamadas de SÉRIES. Pode ter apenas um tipo de variável (float, int, boleana...), é do tipo lista
* As linhas são chmadasd de REGISTROS, ou AMOSTRAS. Pode conter vários tipos de variáveis (float, int, boleana...), é do tipo dicionário
* Ocabeçalho da tabela é chamado de FEATURES, ATRIBUTO ou VARIÁVEL
'''
print('CRIANDO UM DATAFRAME\n')
df = pd.DataFrame({     # passando um dicionário como parâmetro de entrada do dataframe
    # cada chave do dicionário pade conter mais de um valor (uma lista)
    "NOME": ["marcos", "edivânia", "leonide", "josivaldo"],
    "IDADE": [32, 56, 78, 92],
    "PESO": [60.3, 49.2, 80.4, 72.4],
    "VIVO": [True, True, True, False]
})
print(f"df.info: \n{df.info()}")
print(f"df: \n{df}")
print("------------------------------------")

# -----ALTERANDO o ÍNDICE-----------------
print("ALTERANDO o ÍNDICE")
df.index = df.NOME
print(f"df: \n{df}")
print("------------------------------------")

# --------CRIANDO SÉRIES DO TIPO COLUNA------------------
print('CRIANDO SÉRIES DO TIPO COLUNA')
# df.Series({"NOME": "Juvenal", "IDADE":26, "PESO": 96.8, "VIVO":False})
# cria uma série do para uma nova coluna
sn1 = pd.Series(["Santana", "Santos", "Silva", "Bento"], name="SOBRENOME")
sn2 = pd.Series(["Pr", "Sc", "Sp", "Rj"], name="NATURALIDADE")
# adiciona as colunas no dataframe 'tabela'
tabela = pd.DataFrame({sn1.name: sn1, sn2.name: sn2})
print(f"df: \n{tabela}")
print("------------------------------------")

# -------INSERINDO COLUNAS NO DATAFRAME----------
print('INSERINDO COLUNAS NO DATAFRAME')
# insere uma coluna no índice 1
df.insert(1, "SOBRENOME", ["Santana", "Santos", "Silva", "Bento"])
# adiciona uma coluna ao final do dicionario
df["FILHOS"] = [0, 1, 2, 3]
# adiciona uma coluna ao final do dicionario, com todas as linhas igual a 'True'
df["AUTO MÓVEL"] = True
print(f"df: \n{df}")
print("------------------------------------")

# -------INSERINDO LINHAS NO DATAFRAME----------
print('INSERINDO LINHAS NO DATAFRAME')
df.loc[4] = ["Jubileu", "Creidson", 65, 80.8, False, 5, False]
print(df)
print("------------------------------------")

# ----------APAGANDO UM COLUNA DO DATAFRAME -----
print('APAGANDO UM COLUNA DO DATAFRAME')
# del df["SOBRENOME"]        # apaga a coluna in-place(no próprio dataframe)
# apaga a coluna 'sobrenome' do dataframe 'df', e passa para o dateframe 'new'
new = df.pop("SOBRENOME")
print(f"new: \n{new}")
print(f"df: \n{df}")
# 'new' recebe 'df' com aa colunaa 'AUTO MÓVEL' e "FILHOS" apagados (axis 1 para apagar coluna, 0 para apagar linha)
new = df.drop(["AUTO MÓVEL", "FILHOS"], axis=1)
print(f"new: \n{new}")
print(f"df: \n{df}")
# o 'inplace=True' retorna a alteração para o próprio dataframe
df.drop("VIVO", axis=1, inplace=True)
print(f"df: \n{df}")
print("------------------------------------")


# --------------APAGANDO UMA LINHA------------------
print("APAGANDO UMA LINHA\n")
# 'new' recebe 'df' com o índice 'marcos' apagado
new = df.drop("marcos")
print(f"new: \n{new}")
print(f"df: \n{df}")
# o 'inplace=True' retorna a alteração para o próprio dataframe
df.drop(["edivânia", "leonide"], inplace=True)
print(f"df: \n{df}")
print("------------------------------------")

# -------salvando em um csv---------------
# Obter o caminho do diretório onde o script está localizado
diretorio_script = os.path.dirname(os.path.realpath(__file__))

# salva em CSV sem o índice, e UTF-32 para salvar os caracteres especiais
df.to_csv(f"{diretorio_script}/dados.csv",
          index=False, encoding="UTF-32", sep=";")
df.to_excel(f"{diretorio_script}/dadosExcel.xlsx",
            index=False)         # salva em excel
