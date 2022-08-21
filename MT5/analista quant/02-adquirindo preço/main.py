import MetaTrader5 as mt5       #importa a biblioteca

mt5.initialize()        #inicia o metatrader 5

d = mt5.terminal_info()     #a classe 'd' recebe as informações do mt5

d = d._asdict()         #transforma a classe em dicionário

for k in d.keys():
    print(f"{k} -> {d[k]}")


mt5.shutdown()      #encerra o metatrader
