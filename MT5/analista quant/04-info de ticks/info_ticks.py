import MetaTrader5 as mt5       #importa a biblioteca
import pandas as pd
mt5.initialize()        #inicia o metatrader 5

ativo = "WINJ23"        # nome do ativo a ser pesquisado
infoTicks = mt5.symbol_info(ativo)  # recebe uma  estrutura de tuplas com todos os dados de todos os ticks
dinfo = infoTicks._asdict()         #transforma a classe em dicionário

for k in dinfo.keys():
    print(f"{k} -> {dinfo[k]}")


#-------------TRANSFORMANDO EM DATAFRAME------------
lista = list(dinfo.items())
df = pd.DataFrame(lista, columns=["PROPRIEDADE", "VALOR"])
print(df)

mt5.shutdown()      #encerra o metatrader