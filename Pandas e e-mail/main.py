import pandas as pd
import win32com.client as win32   #necessário instalar (pip install pywin32 ou pip install pywin32==227 ou pip install pypiwin32)

#importando a planilha em excel (necessário instalr o openpyxl)
try:
    tabelaVendas = pd.read_excel('Vendas.xlsx')         
except Exception as erro:
    print("Não foi possível importar a planilha. Verefique se o arquivo está na pasta correta.")
    print(f"A classe do erro encontrado foi: {erro.__class__}!")
    print(f"O erro encontrado foi: {erro.__cause__}!")
else:
    print("planilha importada com sucesso")

#visualizar a base de dados 
#pd.set_option('display.max_columns', None)     #define a visualização da tabela para mostrar todas as colunas, sem restrição de tamanho (None)
#print(tabelaVendas[["ID Loja", "Valor Final"]])        #mostra apenas as colunas "ID Loja" e "Valor Final"

#tabelaVendas.groupby("ID Loja").sum()   #na coluna "ID Loja", todas as linhas que tem o mesmo valor são agrupadas. 
                                        #Para as de mais colunas, os valores numéricos de cada linha são somados.

#filtrar o faturamento de cada loja
faturamento = tabelaVendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()

#filtrar a quantidade total de produtos vendidos de cada loja
quantidade = tabelaVendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()

#filtrar tick médio de cada loja
media = (faturamento["Valor Final"]/quantidade["Quantidade"]).to_frame()    #to_frame = transforma o resutado da divisão 
                                                                            #dos elementos de cada lista, em uma tabela.
media = media.rename(columns={0: 'Ticket Médio'})                           #renomeia a coluna "0" para "icket Médio"

#enviar para e-mail via outlook
try:
    outlook = win32.Dispatch('outlook.application')     #usa o outlook como aplicativo para enviar o email
    mail = outlook.CreateItem(0)
except Exception as erro:
    print("Não foi possível iniciar o Outlook.")
    print(f"A classe do erro encontrado foi: {erro.__class__}!")
    print(f"O erro encontrado foi: {erro.__cause__}!")
else:
    mail.To = 'marcos.daniel1990@hotmail.com'           #endereço do destinatário
    mail.Subject = 'faturamento das lojas de curitiba'  #assunto do e-mail
    #corpo do e-mail
    mail.HTMLBody = f"""                                     
    <p>Olá, seguem a baixo as tabelas das lojas de Curitiba.</p>

    <p>faturamento de cada loja:</p>
    {faturamento.to_html(formatters={"Valor Final":"R$ {:,.2f}".format})}\n  


    <p>quantidade total de produtos vendidos de cada loja:</p>
    {quantidade.to_html()}\n


    <p>tick médio de cada loja:</p>
    {media.to_html(formatters={"Ticket Médio":"R$ {:,.2f}".format})}\n


    <p>Atenciosamente.
    """
    #o parâmetro "formatters={"Valor Final":"R$ {:,.2f}".format}" formata os valores da coluna "Valor Final"

    try:
        mail.Send()
    except Exception as erro:
        print("Não foi possível enviar o e-mail.")
        print(f"A classe do erro encontrado foi: {erro.__class__}!")
        print(f"O erro encontrado foi: {erro.__cause__}!")
    else:
        print("e-mail enviado com sucesso")

