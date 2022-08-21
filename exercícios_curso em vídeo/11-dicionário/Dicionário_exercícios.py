'''
01 - Leia o nome, média e situaçõa de um aluno, guarde em um dicionário e imprima;
02 - Crie um programa onde 4 jogadores jogem um trat_erro e tenham resultados aleatórios, guarde em um dicionário,
e mostre os resultados em ordem decrescente;
03 - Leia nome, ano de nascimento (cadastre a idade), e CTPS, e guarde tudo em um dicionário. Se o CTPS for
diferente de zero, o dicionário receberá tb o ano de contratação do primeiro emprego e o salário. Calcule e acrescente no dicionário
além da idade, com quantos anos a pessoa ira se aposentar (considerar apenas 35 anos de registro);
04 - Gerencie o aproveitamento de vários jogadores de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols em cada partida. Tudo deverá ser guardado em um dicionário, incluindo o total
de gols feito durante o campeonato. Cada dicionário devera ser guardado em um lista. Após cadastrar todos os jogadores deverá
ser impressa uma tabela com todos os dados:
Código  -  Jogador   -   Gols     -    Total
-------------------------------------------------
01         Marcos        [0,1,2,3]     6
O programa deverá perguntar ao final de tudo isso: Qual o código do jogador para fazer uma consulta
detalhada (999 para finalizar);

05 - Leia nome, sexo  e idade de várias pessoas, guarde os dados de cada pessoa em um dicionário,
e todos os dicionários em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas.
b) a média de idade do grupo.
c) Uma lista com todas as mulheres
d) uma lista com todos q tem idade acima da média
'''
#------------------Ex01------------------
print(f"{'Ex01':-^40}")
info = {}
info["Nome"] = str(input("Nome: "))
info["Média"] = float(input(f"Digite a média do aluno {info['Nome']}: "))
if info["Média"] >= 7:
    info["Situação"] = str("APROVADO!")
elif 5 <= info["Média"] < 7:
    info["Situação"] = str("EM RECUPERAÇÃO!")
else:
    info["Situação"] = str("REPROVADO!")
print("-"*40)
for k, v in info.items():
    print(f"{k}: {v}")      #mostra o nome do aluno e (aprovado, em recuperação ou reprovado)

#------------------Ex02------------------
print(f"{'Ex02':-^40}")
from random import randint
from time import sleep
from operator import itemgetter
trat_erro = {}
ranking = {}
jogador = ""
for i in range(0, 4):
    jogador = str(f"Jogador {i+1}")
    trat_erro[jogador] = randint(1, 6)

for k, v in trat_erro.items():
    print(f"{k} tirou {v}")     # mostra a ordenação do jogador e o número sorteado
    sleep(0.3)
ranking = sorted(trat_erro.items(), key=itemgetter(1), reverse=True)       #itemgetter=0 organiza pela KEY, itemgetter=1 organiza pelo Value
print("-" *40)
print(f"{'COLOCAÇÃO':^40}")
print("-" *40)
for jogadores, jogo in enumerate(ranking):       #ranking é tratado com uma tupla
    print(f"{jogadores+1}° colocado é o {jogo[0]}: {jogo[1]}")
    sleep(0.5)

#------------------Ex03------------------
print(f"{'Ex03':-^40}")
from datetime import datetime
atual = int(datetime.now().year)
nascimento = idade = int(0)
dados = {}
dados["Nome"] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
dados["Idade"] = atual - nascimento
dados["CTPS"] = int(input("CTPS (apenas números), 0 caso não tenha: "))
if dados["CTPS"] != 0:
    dados["Contrato"] = int(input("Ano do 1° emprego: "))
    dados["Salário"] = str(input("Salário do 1° emprego: "))
    dados["Ano da aposentadoria"] = dados["Idade"] + ((dados["Contrato"] + 35)-atual)
    print("-=" * 40)
    print(f"{'DADOS':^20}")
    print("-=" * 40)
    for k, v in dados.items():
        print(f"{k}: {v}")
else:
    print("Você não tem direito à aposentadoria!")

#------------------Ex04------------------
print(f"{'Ex04':-^40}")
dados = []
jogador = {}
partidas = cont = cod = int(0)
gols = []
continuar = consultar = "S"
while continuar == "S":
    jogador.clear()
    jogador["Jogador"] = str(input("Nome do jogador: "))
    partidas = int(input("Quantas partidas foram jogadas: "))
    for i in range(0, partidas):
        gols.append(int(input(f"N° de gols feitos na {i+1}° partida: ")))
    jogador["Gols"] = gols[:]
    jogador["Total"] = sum(gols)      #soma os itens da lista
    gols.clear()
    dados.append(jogador.copy())
    while True:
        continuar = str(input("Continuar cadastro (s/n): ")).upper().strip()[0]
        if continuar not in "SN":
            print("\033[33mVALOR INCORRETO!\033[m")
        else:
            break

print("-=" * 37)
print("\033[33m", end='')
print(f"{'TABELA DE APROVEITAMENTO':^74}")
print("\033[m", end='')
print("-=" * 37)
print("| CÓDIGO :", end="")
for i in jogador.keys():
    if i == "Jogador":
        print(f"{i:<15}", end="")
    else:
        print(f":{i:<15}", end="")
print()
print("--" * 37)
for k, v in enumerate(dados):
    print(f"|{k+1:>8}", end="")
    for d in v.values():
        print(f":{str(d):<15}", end="")
    print()
print("--" * 37)

while True:
    cod = int(input("Digite o código para realizar a consulta do jogador (999 para encerrar): "))
    if cod == 999:
        print("Programa encerrado!")
        break
    elif cod <= len(dados) and cod >= 1:
        print(f"O jogador {dados[cod-1]['Jogador']} jogol {len(dados[cod-1]['Gols'])} partidas;")
        for i in range(0, len(dados[cod-1]['Gols'])):
            print(f"{dados[cod-1]['Gols'][i]} gols na {i + 1}° partida.")
        print((f"Com total de {dados[cod-1]['Total']} gols"))
    else:
        print("Valor incorreto!")




#------------------Ex05------------------
print(f"{'Ex05':-^40}")
pessoas = {}
dados = []
continuar = "S"
soma = int(0)
media = float(0)
while continuar == "S":
    pessoas["Nome"] = str(input("Nome: "))
    while True:
        pessoas["Sexo"] = str(input("Sexo: ")).upper().strip()[0]
        if pessoas["Sexo"] not in "MF":
            print("Valor incorreto!")
        else:
            break
    pessoas["Idade"] = int(input("Idade: "))
    soma += pessoas["Idade"]
    dados.append(pessoas.copy())
    pessoas.clear()
    while True:
        continuar = str(input("Cadastrar mais alguém (s/n)? ")).upper().strip()[0]
        if continuar not in "SN":
            print("Valor incorreto!")
        else:
            break
print("=-" * 20)
print(f"{'DADOS':^40}")
print("=-" * 20)
print(f"Foram cadastradas {len(dados)} pessoas.")
media = float(soma/len(dados))
print(f"A média de idade das pessoas cadastras é {media:.2f}")
print(f"Mulheres cadastradas:")
for p in dados:
    if p["Sexo"] == "F":
        print(p["Nome"])
print(f"Pessoas com idade acima da média:")
for p in dados:
    if p["Idade"] > media:
        print(f"{p['Nome']} com {p['Idade']} anos")
