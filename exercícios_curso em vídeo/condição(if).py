#01 - Faça o computador pensar nem número inteiro de 1 a 5, e digite um numero de 1 a 5. Diga
# se vc acertou o numero que o comp. pensou ou não;
#02 - Se o carro ultrapassar 80 km/h. mostre o valor da multa, q custa 7r$ a mais
# para cada 1 km/h maior de 80 km/h;
#03 - programa q digase o numero é par ou impar;
#04 - calcule o valor da viagem, se a distancia for menor q 200 km o preço é R$ 0,50 por km,
# se for mair q 200 km o valor é de R$0,45 por km;
#05 - leia um ano qualquer e diga se ele é bissexto;
#06 - Leia três números e mostre qual é o maior e qual é o menor;


from random import randint

#-------------Ex01-------------
print('{:-^30}' .format('Ex01'))
numero = int(input('Digite um numero inteiro de 1 a 5: '))
comp = randint(1, 6)
print('O computador pensou no número {}.' .format(comp))
if numero == comp:
    print('Parabéns, vc é foda e acertou o número!')
else:
    print('Otário vc perdeu!')

#-------------Ex02-------------
print('{:-^30}' .format('Ex02'))
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado em {}!" .format(multa))

#-------------Ex03-------------
print('{:-^30}' .format('Ex03'))
num = int(input('Digite um número inteiro: '))
print(num%2)
if (num%2) == 0:
    print('O numero é par!')
else:
    print('o numero é impar!')

#-------------Ex04-------------
print('{:-^30}' .format('Ex04'))
viagem = float(input('Digite a distancia da viagem: '))
if viagem <= 200:
    valor = viagem * 0.45
    print('O valor da viagem é de {}!' .format(valor))
else:
    valor = viagem * 0.5
    print('O valor da viagem é de {}!' .format(valor))

#-------------Ex05-------------
print('{:-^30}' .format('Ex05'))
ano = int(input('Digite um ano: '))
if (ano % 4 == 0 and ano%100 != 0 or ano % 400 == 0):
    print('O ano {} é bissexto' .format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

#-------------Ex06-------------
print('{:-^30}' .format('Ex06'))
var1 = int(input("Digite um número: "))
var2 = int(input("Digite mais um número: "))
var3 = int(input("Digite outro número: "))

if var1 > var2 and var1 >var3:
    print('O maior númeor é {}' .format(var1))
if var2 > var1 and var2 > var3:
    print('O maior númeor é {}' .format(var2))
if var3 > var1 and var3 > var2:
    print('O maior númeor é {}' .format(var3))
if var1 < var2 and var1 < var3:
    print('O menor númeor é {}' .format(var1))
if var2 < var1 and var2 < var3:
    print('O menor númeor é {}' .format(var2))
if var3 < var1 and var3 < var2:
    print('O menor númeor é {}' .format(var3))

