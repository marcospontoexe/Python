'''
01 - Leia o nome e peso de várias pessoas e guarde em uma lista. Mostre quantas pessoas foram cadastradas, o nome
dos mais pesados, o nome dos mais leves;
02 - Digite sete números inteiros e guarde dentro de uma lista, que devera separar os pares dos ímpares em duas
sublistas distintas;
03 - Imprima uma matriz 3X3 com os valores lidos pelo teclado,
[1] [2] [3]
[4] [5] [6]
[x] [x] [x]
04 - Aprimore o exercício 3, mostrando a soma de todos os valores pares, a soma de todos os valores da terceira coluna,
o maior valor da segunda linha;
05 - Ajude um jogador da megasena a criar palpites. O programa devera perguntar quantos jogos seram criados, e gerar 6
números não repetidos de 1 a 60 para cada jogo, cadastrando tudo em uma lista composta;
06 - leia o nome e duas notas de vários alunos, e guarde em uma lista composta. Mostre um boletim com a média de cada aluno, e
permita que usuario consulte as notas de qualquer aluno;

#------------------Ex01------------------
print(f"{'Ex01':-^40}")
pessoas = []
dados = []
continuar = "S"
pesado = leve = int(0)
while continuar == "S":
    dados.append(str(input("Nome: ")))
    dados.append((int(input("Peso: "))))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        continuar = str(input("Deseja cadastrar mais uma pessoa? (S/N): ")).upper().strip()[0]
        if continuar not in "SN":
            print("Valor incorreto!")
        else:
            break

print("=-" * 20)
print(f"{'LISTA':^40}")
print("=-" * 20)
print(f"Foram cadastrados {len(pessoas)} pessoas")
print(f"As pessoas mais pesadas, com {pesado} quilos, são:")
for nome in pessoas:
    if nome[1] == pesado:
        print(nome[0])
print(f"As pessoas mais leves, com {leve} quilos, são:")
for nome in pessoas:
    if nome[1] == pesado:
        print(nome[0])
#------------------Ex02------------------
print(f"{'Ex02':-^40}")
numeros = [[], []]
temp = int(0)
print("Digite sete números inteiros:")
print("-" * 40)
for i in range(0, 7):
    temp = int(input(f"Digite o {i+1}° número: "))
    if temp % 2 == 0:
        numeros[0].append(temp)
    if temp % 2 == 1:
        numeros[1].append(temp)
numeros[0].sort()
numeros[1].sort()
print(f"Números pares: {numeros[0]}")
print(f"Números ímpares: {numeros[1]}")

#------------------Ex03------------------
print(f"{'Ex03':-^40}")
matriz = [[], [], []]
temp = int(0)
for i in range(0, 3):           #linhas
    for j in range(0, 3):       #colunas
        temp = int(input("Digite um número: "))
        matriz[i].append(temp)
for i in range(0, 3):           #linhas
    print()
    for j in range(0, 3):       #colunas
        print(f"[{matriz[i][j]:0>3}]", end=" ")

#------------------Ex04------------------
print(f"{'Ex04':-^40}")
matriz = [[], [], []]
temp = pares = coluna = maior = int(0)
for i in range(0, 3):           #linhas
    for j in range(0, 3):       #colunas
        temp = int(input("Digite um número: "))
        matriz[i].append(temp)
print("-=" * 40)
for i in range(0, 3):           #linhas
    for j in range(0, 3):       #colunas
        print(f"[{matriz[i][j]:0>3}]", end=" ")
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if j == 2:
            coluna += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

    print()
print(f"A soma de todos os números pares é: {pares}")
print(f"A soma dos números da terceira coluna é: {coluna}")
print(f"O mairo número da segunda linha é {maior}!")

#------------------Ex05------------------
print(f"{'Ex05':-^40}")
from random import randint
from time import sleep
print("+" * 40)
print(F"{'JOGOS DA MEGA SENA':^40}")
print("+" * 40)
jogo = []
numeros = []
jogadas = temp = cont = int(0)
jogadas = int(input("Número de jogadas: "))
print(f"{'Gerando lista de jogos:':^40}")
print("+" * 40)
for i in range(0, jogadas):
    cont = 0
    while cont <= 5:
        temp = randint(1, 60)
        if temp not in numeros:
            numeros.append(temp)
            cont += 1
    numeros.sort()
    jogo.append(numeros[:])
    numeros.clear()
for i in range(0, jogadas):
    print(f"{i+1:>2}° Jogada: {jogo[i]}")
    sleep(0.5)
print("+" * 40)
print(f"{'BOA SORTE!':^40}")
'''
#------------------Ex06------------------
print(f"{'Ex06':-^40}")
boletim = []
nome = str()
nota1 = nota2 = media = float(0)
continuar = "S"
while continuar == "S":
    nome = (str(input("Nome: ")))
    nota1 = float(input("1° nota: "))
    nota2 = float(input("2° nota: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    while True:
        continuar = str(input("Deseja continua (S/N): ")).upper().strip()[0]
        if continuar not in "NS":
            print("Valor incorreto!")
        else:
            break
print("-" * 40)
print(f"{'BOLETIM':^40}")
print("-" * 40)
print(f"{'N°':<4}{'ALUNO':<10}{'MÉDIA':>8}")
for i, pessoa in enumerate(boletim):
    print(f"{i+1:>2} {pessoa[0]:<10} {pessoa[2]:>8.1f}")

continuar = "S"
while continuar == "S":
    while True:
        continuar = str(input("Deseja consultar uma nota (S/N): ")).upper().strip()[0]
        if continuar not in "NS":
            print("Valor incorreto!")
        else:
            break
    nome = str(input("Digite o nome do aluno: ")).upper()
    for pessoa in boletim:
        if nome in pessoa[0].upper():
            print(f"1° nota: {pessoa[1][0]}")
            print(f"2° nota: {pessoa[1][1]}")
            break
        else:
            print("Nome não encontrado!")
            break

