import MetaTrader5 as mt5       #importa a biblioteca
import pandas as pd

if not mt5.initialize():        #inicia o metatrader 5
    print(f"Não foi possível iniciar o MT5! -> {mt5.last_error()}")
    quit()

#----------inserindo o ativo no meta trader 5-------------
ativo = "WINM23"        # nome do ativo a ser pesquisado
# é importante o ativo estar aberto na plataforma para retornar valores (compra, venda, volume ...) corretos
mt5.symbol_select(ativo, True)        # insere o ativo no meta trader 5 (False remove o ativo)

mt5.shutdown()      #encerra o metatrader