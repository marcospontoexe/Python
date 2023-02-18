import time
import MetaTrader5 as mt5       #importa a biblioteca
from datetime import datetime
import pandas as pd

if not mt5.initialize():        #inicia o metatrader 5
    print(f"Não foi possível iniciar o MT5! -> {mt5.last_error()}")
    quit()

#----------COLETANDO CANDLES-------------
ativo = "WINJ23"        # nome do ativo a ser pesquisado
timeframe = mt5.TIMEFRAME_H1    # período gráfico
qntd_candles = 5        # número de ticks solicitados
dia = time.time()      # data atual, (os candles são retornados da maneira retrograda)

while True:
    dados = mt5.copy_rates_from(ativo, timeframe, dia, qntd_candles)       # a Array "dados" recebe as informações do "ativo"
    arq = pd.DataFrame(dados)
    arq["time"] = pd.to_datetime(arq["time"], unit="s") # transforma a coluna de data, de horário GMT para horário UTC
    close = arq['open'].iloc[-1]        # "close" recebe apenas a última tupla do dataframe, e o índice "open" desta tupla
    print(f"Valor de abertura: {close}")
    time.sleep(2)           # pausa de 2 segundos



mt5.shutdown()      #encerra o metatrader


