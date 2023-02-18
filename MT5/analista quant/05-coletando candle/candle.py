import time
import MetaTrader5 as mt5       #importa a biblioteca
from datetime import datetime
import pandas as pd

if not mt5.initialize():        #inicia o metatrader 5
    print(f"Não foi possível iniciar o MT5! -> {mt5.last_error()}")
    quit()

#----------COLETANDO CANDLES-------------
ativo = "WINJ23"        # nome do ativo a ser pesquisado
timeframe = mt5.TIMEFRAME_H1    # período gráfico (H1 = período horário)
qntd_candles = 100         # número de ticks solicitados
dia = time.time()      # data atual, (os candles são retornados da maneira retrograda)

dados = mt5.copy_rates_from(ativo, timeframe, dia, qntd_candles)       # a Array "dados" recebe as informações do "ativo"

arq = pd.DataFrame(dados)

arq["time"] = pd.to_datetime(arq["time"], unit="s") # transforma a coluna de data, de horário GMT para horário UTC
print(arq)

arq.to_csv("dados.csv", index=False)

mt5.shutdown()      #encerra o metatrader


