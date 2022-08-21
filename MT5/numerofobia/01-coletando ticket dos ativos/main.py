import MetaTrader5 as mt5       #importa a biblioteca

mt5.initialize()        #inicia o metatrader 5

ticketsTotal  = mt5.symbols_total()      # recebe a quantidade de tickets dos ativos

if ticketsTotal > 0:
    print(f"Quantidade total de tickets de ativos: {ticketsTotal}")
else:
    print("Síbolos não encontrados!")

ticket = mt5.symbols_get()      #a tupla "ticket" recebe o nome dos ativos


for pos, val in enumerate(ticket):
    if pos < 100:
        print(f"{pos}: {val.name}")    # imprime o ticket dos ativos
    else:
        break


mt5.shutdown()      #encerra o metatrader
