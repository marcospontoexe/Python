import MetaTrader5 as mt5       #importa a biblioteca

mt5.initialize()        #inicia o metatrader 5

ativos = mt5.symbols_get()  # recebe uma tupla com todos os dados de todos os ticks


for ativo in ativos:
    print(ativo.name)


mt5.shutdown()      #encerra o metatrader
