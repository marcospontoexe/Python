import time
import MetaTrader5 as mt5       #importa a biblioteca
from datetime import datetime
#import matplotlib
import pandas as pd
import cufflinks as cf      # biblioteca para gerar grafico em candles
cf.set_config_file(offline=True)      # possibilitar a execução offline da biblioteca cufflinks, e associa à bib pandas

if not mt5.initialize():        #inicia o metatrader 5
    print(f"Não foi possível iniciar o MT5! -> {mt5.last_error()}")
    quit()

#----------COLETANDO CANDLES-------------
ativo = "WINJ23"        # nome do ativo a ser pesquisado
timeframe = mt5.TIMEFRAME_H1    # período gráfico (H1 = período horário)
qntd_candles = 100         # número de ticks solicitados
inicio = 0      # A numeração das barras vai do presente para o passado, ou seja, a barra zero significa a atual

mt5.symbol_select(ativo, True)        # insere o ativo no meta trader 5 (False remove o ativo)

dados = mt5.copy_rates_from_pos(ativo, timeframe, inicio, qntd_candles)       # Recebe barras do terminal MetaTrader 5, a partir do índice especificado

arq = pd.DataFrame(dados)   # transforma em dataframe
arq["time"] = pd.to_datetime(arq["time"], unit="s") # transforma a coluna de data, de horário GMT para horário UTC

#print(arq.describe())       # mostra a média, valor mínimo, percentil.... do dataframe
#arq.set_index("time", implace=True)
arq.iplot(figure="candle")

mt5.shutdown()      #encerra o metatrader
