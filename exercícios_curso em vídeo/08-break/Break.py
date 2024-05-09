'''
01 - Leia vários números inteiros, e só pare o programa quando o usuário digitar o número 999. No
final mostres quantos números foram digitados e qual foi a soma entre eles, desconsiderendo o número 999;
02- Faça um programa que mostre a tabuada de um número digitado pelo usuário. O programa só deve encerrar quando
o usuário digitar um número negativo;
03 - jogue par ou ímpar com o computador. O jogo será finalizado quando o jogador perder.
Mostre quantas vezes o jogar ganhou;
04 - Leia a idade e sexo de várias pessoas.A cada pessoa cadastrada o programa deverá perguntar
se quer encerrar ou não, quantas pessoas são maior de idade, quantos homens foram cadastrados, e quantas mulheres tem menos 
de 20 anos;
05 - Leia o nome e valor de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. Mostre
o Total gasto na compra, quantos produtos custam mais de 100 reais, e qual o nome do item mais barato;
06 - Simule o funcionamento de um caixa eletrônico. Pergunte ao usuário o total a ser sacado, e o programa deverá
mostrar quantas cédular de 50, 20, 10, 5, 2 e 1 reais seram entregues;

#------------------Ex01------------------
while True:
    numero = int(input("Digite um número interio [999 para sair]: "))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f"Você digitou \033[35m{cont}\033[m números, e a soma desses \033[35m{cont}\033[m números é \033[33m{soma}\033[m!")

#------------------Ex02------------------
print(f"{'Ex02':-^40}")
tabuada = int(0)
while True:
    tabuada = int(input("Digite qual tabuada deseja saber! Digite um número negativo para encerrar o programa: "))
    if tabuada < 0:
        print("\033[33mPROGRAMA ENCERRADO, VOLTE SEMPRE!\033[m")
        break
    cont = int(0)
    print(f"{'TABUADA DO ' + str(tabuada):-^40}")
    while cont < 11:
        print(f'{tabuada} X {cont} = {tabuada*cont}')
        cont += 1

#------------------Ex03------------------
from random import randint
from time import sleep
print(f"{'Ex03':-^40}")
res = comp_valor = user_opcão = user_valor = cont = int(0)
while True:
    while True:
        user_opcão = int(input("""Digite:
        [1] para ÍMPAR
        [0] para PAR\n"""))
        if user_opcão < 0 or user_opcão > 1:
            print('você digitou um opção inválida!')
        else:
            break
    while True:
        user_valor = int(input(f'Digite um valor de 0 a 10: '))
        if user_valor < 1 or user_valor > 10:
            print('você digitou um valor fora do range!')
        else:
            break
    comp_valor = randint(0, 11)
    print(f'O computador jogou : \033[33m{comp_valor}\033[m')
    res = comp_valor + user_valor
    print(f'O resultado foi {res}!', end=" ")
    print("deu PAR!" if res % 2 ==0 else "Deu ÍMPAR!")

    if res % 2 == user_opcão:
        print('Ganhou!')
        break
    else:
        cont += 1

print(f'Você perdeu {cont} vezes!')

#------------------Ex04------------------
print(f"{'Ex04':-^40}")
print(f"{'CADASTRO':=^40}")
sexo = sair = ' '
idade = pessoas = homen = mulheres = int(0)
while True:
    print(f"{'Cadastre um cliente':^20}")
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Digite o sexo (masc. ou fem.): ").strip().upper()[0])
        if sexo not in 'MF'
            print("Sexo inválido, digite novamente!")
    if sexo == 'M':
        homen += 1
    if idade <= 20 and sexo == 'F':
        mulheres += 1
    pessoas += 1
    while True:
        sair = input("Deseja cadastrar mais um cliente - S/N: ").strip().upper()[0]
        if sair not in 'SN':
            print("Você digitou um valor errado, digite novamente!")
        else:
            break
    if sair == 'N':
        break
print(f"O total de clientes cadastrados foi {pessoas}, sendo {homen} homens e {mulheres} mulheres menores de 20 anos!")


#------------------Ex05------------------
print(f"{'Ex05':-^40}")
barato = continuar = nome = ''
valor = caro = menor = total = float(0)
print(f"{'LISTA DOS DESEJOS':+^40}")
while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    if total == 0 or valor < menor:
        menor = valor
        barato = nome       #nome do produto mais barato
    total += valor
    if valor >= 100:
        caro += valor
    while True:
        continuar = str(input("Deseja continuar (S/N): ").strip().upper()[0])
        if continuar not in 'SN':
            print("Valor incorreto!")
        else:
            break
    if continuar == 'N':
        break
print(f"total da compra foi de {total} R$.")
print(f"O produto mais barato foi o {barato}.")
print(f"O total dos produtos acima de 100 R$ foi {caro}.")
'''
#------------------Ex06------------------
print(f"{'Ex06':-^40}")
print("\033[33mBanco Ricão\033[m")
total = qntd = int(0)
cédula = int(100)
total = int(input("Digite o total a ser sacado: "))
while True:
    if total >= cédula:
        total -= cédula
        qntd += 1
    else:
        if qntd >= 1:
            print(f"{qntd} notas de {cédula} R$")
        qntd = 0
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 2
        elif cédula == 2:
            cédula = 1
        else:
            break
#------------------usando continue-----------------

counter = 0

while counter < 10:
    counter += 1
    if counter == 3:
        continue    # pula para para a próxima iteração do loop (vai para o início do loop)
    print (counter)
    
print ("Outside the loop!")
