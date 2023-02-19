import time
import MetaTrader5 as mt5       #importa a biblioteca
from datetime import datetime
import pandas as pd


d = pd.read_csv("WIN$_H1.csv", sep="\t")        # lendo um arquivo csv com separação por tabulação
print(d)
print(d.shape)      # mostra o total de colunas e linhas