def cabeçalho(txt):
    print("=-" * 20)
    print(f"{txt:^40}")
    print("=-" * 20)

'''
01 - Faça uma função para recebeer as dimensões de uma parede e mostrar o valor da área;
02 - Faça uma função chamada escreva, que receba uma string como parâmetro, e mostre uma mensagem com tamanho adaptável;
03 - Crie uma função chamada contador, que receba como parâmentro "inicio", "fim", "passo" e imprima os números no passo escolhido;
04 - Crie uma função chamada maior que receba vários numeros inteiros, e mostre quantos valores foram recebidos 
e qual é o maior número;
05 - Crie um lista chamada numeros e duas funções chamadas sorteio e somapar. A fução sorteio vai sortear cinco numeros de 0 a 9
e guardar dentro da lista. A segunda função vai somar os numeros pares;
06 - Crie uma função chamada voto, que receba o ano de nascimento, e retorne: "O voto é obrigatório", ou "O voto é opcional", ou
"O voto não é obrigatório"
07 - Crie uma função chamada fatorial(n, show), n é o valor a ser calcula do fatorial, e show(True/False) é uma variável opcional
 que mostra o cálculo.
08 - crie uma função ficha(), que receba dois parâmetros opcionais, o nome do jogador e quantos gols ele fez;
09 - crie uma função leiaint(), que faça uma validação para aceitar apenas números. A função deeve ser parecida com a input();
10 - Crie uma função notas(), que pode receber várias notas, e mostre: a quantidade de notas, a maior nota, a menor nota, a média,
e também um parâmetro opcional para mostrar a situação (ruim, razoavel, boa);
11 - Crie um programa que ultilize o interactive help para imprimir um manual de um comando digitado pelo usuário, 
quando digitado fim o programa se encerrará;
#-------------------Ex01--------------
def area(a, b):
    print(f"O valor da área é {a * b} metros quadrado!")

alt = larg = float(0)
cabeçalho("CÁLCULO DA ÁREA")
alt = float(input("Altura (m): "))
larg = float(input("Largura (m): "))

area(alt, larg)

#-------------------Ex02--------------
def escreva(txt):
    tamanho = int(len(txt) + 6)
    print("~" * tamanho)
    print(f"   {txt}")
    print("~" * tamanho)

escreva("Olá")

#-------------------Ex03--------------
from time import sleep
cabeçalho("CONTADOR")
i = f = p = int(0)
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        if fim < inicio:
            for i in range(inicio, fim, -1):
                print(f"{i}", end=" ")
                sleep(0.5)
        elif fim > inicio:
            for i in range(inicio, fim, 1):
                print(f"{i}", end=" ")
                sleep(0.5)
        else:
            print(inicio)
    elif fim > inicio:
        for i in range(inicio, fim + 1, passo):
            print(f"{i}", end=" ")
            sleep(0.5)

    elif fim < inicio:
        for i in range(inicio, fim - 1, -passo):
            print(f"{i}", end=" ")
            sleep(0.5)
    else:
        print(inicio)

i = int(input("Digite o início: "))
f = int(input("Digite o fim: "))
p = int(input("Digite o passo: "))
contador(i, f, p)

#-------------------Ex04--------------
def maior(lista):
    tamanho = len(lista)
    maior = lista[0]
    for i in range(0, tamanho):
        if lista[i] > maior:
            maior = lista[i]
    print(f"Dentre os {tamanho} números, o maior foi o número {maior}.")


cabeçalho("MAIOR VALOR")
valores = []
continuar = "S"
while continuar == "S":
    valores.append(int(input("Digite um inteiro: ")))
    while True:
        continuar = str(input("Continuar (S/N): ")).upper().strip()[0]
        if continuar not in "SN":
            print("Valor incorreto!")
        else:
            break
maior(valores)
#-------------------Ex05--------------
from random import randint
from time import sleep
lista = []
def sortear(num):
    print(f"Sorteando {num} números")
    print("-"*40)
    sleep(0.5)
    for i in range(0, num):
        lista.append(randint(0, 9))
        print(f"{lista[i]}", end=" ", flush=True)           #limpa o buffer de memória para q o sleep funcione em tempo real
        sleep(0.3)
    print()

def somapar (lst):
    soma = int(0)
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f"A soma dos valores pares é {soma}.")

sortear(5)
somapar(lista)

#-------------------Ex06--------------
cabeçalho(f"VOTAÇÃO")
def voto(n):
    from datetime import date           #A importação da biblioteca é feita apenas localmente, e não globalmente.
    # Economiza memória já qua a datetime será usada apenas dentro da função
    atual = date.today().year
    idade = atual - n
    if idade < 18:
        return f"idade {idade} anos. Voto não obrigatório!"
    elif idade >= 65:
        return f"idade {idade} anos. Voto opcional!"
    else:
        return f"idade {idade} anos. Voto obrigatório!"


print(voto(int(input("Ano de nascimento: "))))

#-------------------Ex07--------------
cabeçalho(f"Cálculo do fatorial")
num = int(0)
mostrar = str("")
def fatorial(n, show = False):
    fator = int(n)
    if show:
        f = []
        f.append(fator)
        for i in range(fator-1, 0, -1):
            f.append("*")
            fator *= i
            f.append(i)
        return f, fator
    else:
        for i in range(fator-1, 0, -1):
            fator *= i
        return fator


num = int(input("Digite um número para calcular o fatorial: "))
while True:
    mostrar = str(input("Deseja mostrar o cálculo (S/N): ")).strip().upper()[0]
    if mostrar not in "SN":
        print("Valor incorreto!")
    else:
        if mostrar == "S":
            retorno = fatorial(num, True)
            for v in retorno[0]:
                print(f"{v}", end=" ")
            print(f" = {retorno[1]}")
        else:
            print(fatorial(num))
        break

#-------------------Ex08--------------
cabeçalho("Ficha do jogar")
n = g = ""
def ficha(nome = "<desconhecido>", gol =0):
    print(f"O jogador {nome} fez {gol} gols")

n = str(input("Nome do jogador: "))
g = str(input("Gols feito: "))
if g.isnumeric():
    g = int(g)
else:
    g= int(0)
if n.strip() == "":
    ficha(gol = g)
else:
    ficha(n, g)

#-------------------Ex09--------------
cabeçalho("Validação numérica")
n = int(0)
def leiaint(num):
    valor = str(input(num))
    if valor.isnumeric():
        valor = int(valor)
        return valor
    else:
        while True:
            print(f"Valor incorreto!")
            valor = input("\033[33mERRO! Digite um número inteiro: \033[m")
            if valor.isnumeric():
                valor = int(valor)
                return valor


n = leiaint("Digite um número inteiro: ")
print(f"Você digitou {n}.")

#-------------------Ex10--------------
cabeçalho("Situação da média")
def notas(*notas, sit=False):
    dic = {}
    dic["Total"] = len(notas)
    dic["Maior"] = max(notas)
    dic["Menor"] = min(notas)
    dic["Média"] = sum(notas) / len(notas)
    print(notas)
    if sit:
        if dic["Média"] < 5:
            dic["Situação"] = str("RUIM")
        elif dic["Média"] > 6:
            dic["Situação"] = str("BOA")
        else:
            dic["Situação"] = str("RAZOÁVEL")
    return dic

info = notas(5.2, 3, 2, sit=True)
print(info)
'''
#-------------------Ex11--------------
continuar = ""
while True:
    comando = str(input("Digite um comando python (FIM para encerrar): "))
    if comando.upper() in "FIM":
        print("Até logo")
        break
    else:
        cabeçalho(f"\033[34mManual do comando {comando}\033[m")
        print("\033[35m")
        print(help(comando))
        print("\033[m")
