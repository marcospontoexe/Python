'''
01 - Crie um programa q peça para o usuário digitar um número inteiro de 0 a 20, e mostre na tela o número
escrito;
02 - Gere cinco números aleatórios e guarde em um tupla, em seguida mostre todos, mostre o maior e mostre o menor;
03 - Leia quatro valores inteiros e guarde em uma tupla. Mostre quantas vezes apareceu o valor 9,
em que posição foi digitado o primeiro 3, e os números pares;

04- Crie uma tupla unica que contenha o nome de vários produtos e seus respectivos valores na posição a frente. Mostre  de forma
tabular todos os produtos e seus valores;
        Lista de produtos
------------------------------
produto 01.................R$  1.50
proutooooooo 02............R$  2.00
protuno n..................R$ 15.20

05 - Crie uma tupla com várias palavras (não usar acentos), e mostre todas vogais contidas em cada palavra da tupla
'''
#------------------Ex01------------------
print(f"{'Ex01':-^40}")
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinto', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezessies', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
user = int(0)
continuar = ' '
while True:

    while True:
        user = int(input('Digite um número inteiro de 0 a 20: '))
        if user not in range(0, 21):
            print('\033[33mValor incorreto!\033[m')
        else:
            break
    print(numeros[user])
    while True:
        continuar = str(input("Deseja continuar (S/N): ")).strip().upper()[0]
        if continuar not in 'SN':
            print('\033[34mValor incorreto!\033[m')
        else:
            break
    if continuar == 'N':
        break
print("\033[32mFim! \nVolte sempre!")

#------------------Ex02------------------
print(f"{'Ex02':-^40}")
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(tupla)

print(f"O maior númeor é {max(tupla)}!")    #mostra o maior número  na tupla
print(f"O menor númeor é {min(tupla)}!")    #mostra o menor número da tupla


#------------------Ex03------------------
print(f"{'Ex03':-^40}")
numeros = (input("Digite um número: "), input("Digite outro número: "), input("Digite mais um número: "), input("Agora o último número: "))
print(numeros)
print(f"O número 9 apareceu {numeros.count('9')} vezes!")
if '3' in numeros:
    print(f"O primeiro 3 aparece na posição {numeros.index('3')+1}!")   # se não for digitado o número três da erro.
else:
    print("Não foi digitado o número 3!")
print("Os números pares são os: ")
for ind in numeros:
    if int(ind) % 2 == 0:
        print(ind)

#------------------Ex04------------------
print(f"{'Ex04':-^40}")
lista = ("Arroz", 5,
         "Açucar", 4.45,
         "Feijão", 3.89,
         "Macarrão", 3.59,
         "Óleo", 12.99,
         "Farinha", 2.42,)
print("*" * 50)
print(f"\033[31m{'LISTA DE PREÇO':^50}\033[m")
print("*" * 50)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<40}R$", end="")
    else:
        print(f'{lista[i]:>7.2f}')
print("*" * 50)

#------------------Ex05------------------
print(f"{'Ex05':-^40}")
palavras = (input('Digite uma palavra: '),
          input('Digite outra palavra: '),
      #  input('Digite outra palavra: '),
      #  input('Digite outra palavra: '),
      #  input('Digite outra palavra: '),
          )
for vogais in palavras:
    print(f"{vogais} contém: ")
    for i in range(0, len(vogais)):
        if vogais[i].upper() in 'AEIOU':
            print(vogais[i], end=", ")
    print("\n")