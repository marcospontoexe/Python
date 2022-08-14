'''
01 - Mostre a tabuada de um número escolhido pelo usuário:
02 - MOstre na tela uma contagem regressiva de 10 até 0, com intervalo de um segundo;
03 - Mostre todos os números pares num intervalo de 0 a 50;
04 - Calcule a soma entre todos os numeros ímpares, que são multiplos de trÊs e que se encontram
num intervalo de 1 até 500
05- Leia uma frase qualquer e diga se é um palíndromo:
06 - Leia o peso de cinco pessoas e diga qual é o maior e o menor peso:
'''
#=============Ex01=============
print('{:=^30}' .format('Ex04'))
tabuada = int(input('Digite a tabuada desejada: '))
for i in range (0, 11):                                 #repete de 0 até 10, incrementando de 1 em 1
    print("{} X {} = {}" .format(tabuada, i, tabuada*i))

print('O \033[35mTiago\033[m da o boga!!!')

#=============Ex02=============
from time import sleep
print('{:=^30}' .format('Ex01'))
for i in range (10, -1, -1):        #repete de 10 até 0, decrementando de um em um
    print(i, end=" ")
    sleep(1)

#=============Ex03=============
print('{:=^30}' .format('Ex02'))
for i in range (0, 51, 2):          ##repete de 0 até 50, incrementando de 2 em 2
    print(i, end=" ")

#=============Ex04=============
print('{:=^30}' .format('Ex03'))
soma = int(0)
for i in range (1, 501, 2): #o incremento em dois em dois, só incrementa os números ímpares
    if i%3 == 0:            #se for multiplo de 3
        soma += i
print("A soma dos números é {}!" .format(soma))

#=============Ex05=============
print('{:=^30}' .format('Ex05'))
frase = str(input('Digite uma frase: ')).strip().upper()
split = frase.split()
juntar = ''.join(split)
inverso = ''
for i in range (len(juntar)-1, -1, -1):
    inverso += juntar[i]
if juntar == inverso:
    print('A frase {} é um palíndromo!' .format(frase))
else:
    print('A frase {} não é um palíndromo!'.format(frase))

#=============Ex05=============alternativa menor
print('{:=^30}' .format('Ex05'))
frase = str(input('Digite uma frase: ')).strip().upper()
split = frase.split()
juntar = ''.join(split)
inverso = juntar[::-1]      #recebe do último índice até o 1°

if juntar == inverso:
    print('A frase {} é um palíndromo!' .format(frase))
else:
    print('A frase {} não é um palíndromo!'.format(frase))


#=============Ex06=============
print('{:=^30}' .format('Ex06'))
for i in range (1, 6):
    peso = float(input('Digite o peso da {}° pessoa: ' .format(i)))
    if i == 1:
        maior = float(peso)
        menor = float(peso)
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O \033[34mmenor\033[m peso é {:.2f}!' .format(menor))
print('O \033[34mmaior\033[m peso é {:.2f}!' .format(maior))