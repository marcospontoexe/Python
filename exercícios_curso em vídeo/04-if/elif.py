'''01 - Leia umnúmero inteiro, e peça para o usuário escolher qual será a base de conversão.
1 - para binário, 2 - para octal, 3 - para hexadecimal;
02 - Leia o ano de nascimento, e informe se ele ainda vai se alistar e quantos anos faltam,
se já esta no ano do alistamento, ou se ja passou do ano de alistamento e quantos anos ja passaram;
03 - FOrneça dois numeros intiros, e diga qual se o primeiro é maior, se o segundo é maior, ou se eles são iguais;
'''
#-------------Ex01-------------
print('{:-^30}' .format('Ex01'))
num = int(input('Digite um numero inteiro: '))
print('''Digite um número para escolher a base de conversão:
[01] - converter para BINÁRIO
[02] - converter para OCTAL
[03] - converter para HEXADECIMAL''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('O número {} convertido para BINÀRIO é {}' .format(num, bin(num)))
elif opção == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)))
else:
    print('opção inválida!')

#-------------Ex02-------------
from datetime import date
print('{:-^30}' .format('Ex02'))
atual = date.today().year
nasc = int(input("Digite sua data de nascimento: "))
idade = atual - nasc
print('ano atual:', atual)
print('idade:', idade)
if idade < 18:
    print('você ainda não tem idade para se alistar. Ainda faltam {} anos' .format(18-idade))
elif idade == 18:
    print('você tem {} anos e ja pode se alistar!'.format(idade))
else:
    print('seu prazo de alistamento já passou de {} anos!'.format(idade-18))

#-------------Ex03-------------
print('{:-^30}' .format('Ex03'))
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
if num1 > num2:
    print('O \033[4;35mprimeiro\033[m valor é maior!')
elif num2 > num1:
    print('O \033[4;35msegundo\033[m valor é maior!')
else:
    print('Os dois valores são iguais!')