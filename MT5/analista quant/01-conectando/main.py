import MetaTrader5 as mt5       #importa a biblioteca

mt5.initialize()        #inicia o metatrader 5

d = mt5.terminal_info()

print(f"informações do terminal: {d}")


mt5.shutdown()      #encerra o metatrader
