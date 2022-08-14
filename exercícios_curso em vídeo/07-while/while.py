'''
01 - Faça um programa que leia o sexo de uma pessoa, mas so aceita M ou F, caso esteja errado peça
a digitação novamente;
02 - Faça o computador pensar num número de 1 a 10, e pergunte um número para o usuário até acertar o
número escolhido pela computador;
03 - Crie um programa que leia dois números e mostre o seguinte menu:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS VALORES
[5] PARA SAIR
o programa deverá realizar a ação solicitada;

04 - Mostre o fatorial de um número lido pelo usuário;
'''

#------------------Ex01------------------
print('{:-^40}' .format('Ex01'))
sexo = input("Digite seu sexo: ").strip().upper()[0]    #retira o espaço antes e depois da frase, e pega apenas o primeiro caractere digitado em maiúsculo
while sexo not in 'MF':
    sexo = input("Dados inválidos, digite seu sexo: ").strip().upper()[0]
    print(sexo)
if sexo == "M":
    print("Masculino!")
else:
    print("Feminino!")

#------------------Ex02------------------
print('{:-^40}' .format('Ex02'))
from random import randint
user = int(0)
comp = int(1)
cont = int(0)
while comp != user:
    comp = randint(0, 9);
    user = int(input('Digite um número inteiro de 0 a 10: '))
    if user < 0 or user > 10:
        while user < 0 or user > 10:
            print('Você digitou um número \033[4;33minválido\033[m!')
            user = int(input('Digite um número inteiro de 0 a 10: '))
    print('O Computador pensou no número \033[34m{}\033[m'. format(comp))
    if comp != user:
        print('\033[33mERROU\033[m!')
        cont += 1
print('Ufa finalmente acertou né!')
print('Você \033[33merrou\033[m {} vezes!' .format(cont))


#------------------Ex03------------------
print('{:-^40}' .format('Ex03'))
import math
num1 = int(0)
num2 = int(0)
res = int(0)
opção = ''
while opção != 'S':
    num1 = int(input('Digite um valor inteiro: '))
    num2 = int(input('Digite outro valor inteiro: '))
    opção = input("""Digite uma das opções!
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS VALORES
    [5] PARA SAIR\n""").strip().upper()
    if opção == '5':
        opção = 'S'
    elif opção == '1':
        res = num1 + num2
        print('A soma dos números é {}!'.format(res))
    elif opção == '2':
        res = num1 * num2
        print('A multiplicação dos números é {}!'.format(res))
    elif opção == '3':
        if num1 > num2:
            print('{} é maior do que {}!'.format(num1, num2))
        else:
            print('{} é maior do que {}!'.format(num2, num1))
    elif opção == '4':
        print('Digite os valores novamente!')
    else:
        while int(opção) < 1 or int(opção) > 5:
            print('Valor invélido!')
            opção = input("""Digite uma das opções!
                [1] SOMAR
                [2] MULTIPLICAR
                [3] MAIOR
                [4] NOVOS VALORES
                [5] PARA SAIR\n""").strip().upper()

#------------------Ex04------------------
print('{:-^40}' .format('Ex04'))
valor = int(input('Digite um número inteiro: '))
cont = int(valor - 1)
fat = int(valor)
while cont != 0:
    fat = fat * cont
    cont = cont - 1
print('O fatorial de {} é {}!' .format(valor, fat))
