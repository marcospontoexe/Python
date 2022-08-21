import MetaTrader5 as mt5       #importa a biblioteca
import pandas as pd
import matplotlib.pyplot as plt

mt5.initialize()        #inicia o metatrader 5

ativo = "WINV22"

data = pd.DataFrame()

dados = mt5.copy_rates_from_pos(ativo, mt5.TIMEFRAME_D1, 0, 1000)
data = [y["close"] for y in dados]

print(data)

mt5.shutdown()      #encerra o metatrader
