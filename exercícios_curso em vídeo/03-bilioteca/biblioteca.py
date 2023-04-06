'''import math

num1 = float(input('digite um número: '))
raiz = math.sqrt(num1)
print('a raiz quadrada de {} é {:.3f}' .format(num1, raiz))
print('a raiz arredondada para cima é {}' .format(math.ceil(int(raiz))), end=' ')
print('e a raiz arredondada para baixo é {:.3f}' .format(math.floor(raiz)))'''
#-------------------------------------------------------------------------------------------
import datetime
from datetime import date
import pytz
print('{:-^30}' .format('Ex02'))
atual = date.today().year
nasc = int(input("Digite seu ano de nascimento: "))
idade = atual - nasc
print('ano atual:', atual)
print('idade:', idade)

diaUtc = '010423'  # recebe uma string com o dia fornecida pelo GNSS (exemplo: ddmmyy)
horaUtc = '012950'  # rebe uma string com o horário UTC fornecido pelo GNSS (exemplo: hhmmss.ss)
#----- conversão de data e hora UTC para data e hora local-----------------------------
datetime_obj = datetime.datetime.strptime((f'{diaUtc[:2]}/{diaUtc[2:4]}/20{diaUtc[4:]} {horaUtc[:2]}:{horaUtc[2:4]}:{horaUtc[4:6]}'), '%d/%m/%Y %H:%M:%S')      # converte de string para objeto datetime() (2023-04-05 20:33:51)
fusoLocal = pytz.timezone('America/Sao_Paulo')       # fuso horário local
tempoLocal = datetime_obj.replace(tzinfo=pytz.utc).astimezone(fusoLocal)  # Converte o horário UTC para o timezone local (2023-04-05 17:33:51)
strTempoLocal = str(tempoLocal)             # converte para string

dia = f"{strTempoLocal[8:10]}/{strTempoLocal[5:7]}/{strTempoLocal[:4]}"
hora = f"{strTempoLocal[11:13]}:{strTempoLocal[14:16]}:{strTempoLocal[17:19]}"  # fuso horário -3
data = f"{dia} - {hora}"

print(f"dia: {dia}")
print(f"hora: {hora}")
print(f"data: {data}")
#-------------------------------------------------------------------------------------------

'''
from random import randint
from time import sleep
#-------------Ex01-------------
print('{:-^30}' .format('Ex01'))
numero = int(input('Digite um numero inteiro de 1 a 5: '))
print('Processando...')
sleep(3)
comp = randint(1, 6)
print('O computador pensou no número {}.' .format(comp))
if numero == comp:
    print('Parabéns, vc é foda e acertou o número!')
else:
    print('Otário vc perdeu!')
# -------------------------------------------------------------------------------------------'''