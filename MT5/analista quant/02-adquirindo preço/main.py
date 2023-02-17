import MetaTrader5 as mt5       #importa a biblioteca
from datetime import datetime
import pandas as pd

mt5.initialize()        #inicia o metatrader 5

'''
d = mt5.terminal_info()     #a classe 'd' recebe as informações do mt5

d = d._asdict()         #transforma a classe em dicionário

for k in d.keys():
    print(f"{k} -> {d[k]}")
'''

#----------COLETANDO PREÇO-------------
ativo = "WINJ23"        # nome do ativo a ser pesquisado
flag= mt5.COPY_TICKS_ALL   # flag para selecionar
dia = datetime(2022,12,14)      # data inicial da pesquisa

dados = mt5.copy_ticks_from(ativo, dia, 30, flag)       # a Array "dados" recebe as informações do "ativo"

arq = pd.DataFrame(dados)
print(arq)

print(type(arq))

mt5.shutdown()      #encerra o metatrader


