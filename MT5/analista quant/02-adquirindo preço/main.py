import MetaTrader5 as mt5       #importa a biblioteca
from datetime import datetime
import pandas as pd

mt5.initialize()        #inicia o metatrader 5

#----------COLETANDO PREÇO-------------
ativo = "WINJ23"        # nome do ativo a ser pesquisado
flag = mt5.COPY_TICKS_ALL   # combinação de sinalizadores que definem o tipo de ticks solicitados
qntd = 50         # número de ticks solicitados
dia = datetime(2022,12,14)      # data a partir da qual são solicitados os ticks

dados = mt5.copy_ticks_from(ativo, dia, qntd, flag)       # a Array "dados" recebe as informações do "ativo"


arq = pd.DataFrame(dados)
print(arq)





mt5.shutdown()      #encerra o metatrader


