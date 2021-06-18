'''
01 - Leia 5 valores numéricos e guarde um uma lista. Mostre qual é o miaor valor, o menor valor, e suas respectivas
posições;
02 - Digite vários valores numéricos e cadastre em uma lista. Caso o número ja exita na lista, não deverá ser gravado na lista.
Nofinal devera mostrar todos os números unicos em ordem crescente;
03 - Adicione 5 valores numericos em um lista, e imprima em ordem crescente. sem usar o método sort();
04 - Leia vários valores inteiros e guarde em uma lista. Mostre quantos números foram armazenados, lista com os valores ordenados
em ordem decrescente, se o valor 5 esta na lista;
05 - Leia vários numeros de uma lista, depois crie mais duas listas para receber os valores pares e outra para receber os
ímpares, e imprima as três listas;
06 - Digite uma expressão matemática contendo parenteses. O programa deverá informa se faltou algum parenteses na expressão;
#------------------Ex01------------------
print(f"{'Ex01':-^40}")
valores = []
maior = menor = int(0)
for i in range(0, 5):
    valores.append(input("Digite um valor: "))
    if i == 0:
        maior = menor = valores[0]
    else:
        if valores[i] < menor:
            menor = valores[i]
        if valores[i] > maior:
            maior = valores[i]
print("-=" * 20)
print(f"Lista de valores: {valores}")
print("-=" * 20)
print(f"O maior valore foi: {maior}")
for i in range(0, len(valores)):
    if valores[i] == maior:
        print(f"na posição {i+1}")
print("-=" * 20)
print(f"O menor valore foi: {menor}")
for i in range(0, len(valores)):
    if valores[i] == menor:
        print(f"na posição {i+1}")
print("-=" * 20)

print(F"{'Ex02':-^40}")
#------------------Ex02------------------
lista = []
continuar = str("S")
flag = repetido = False
numero = i = int()
while continuar == 'S':
    numero = int(input("Digite um número inteiro: "))
    while numero in lista:  #verifica se o numero digitado não está repetido na 'lista'
        numero = int(input("O valor digitado ja existe, digite outro! "))
    while True:
        continuar = str(input("Deseja continuar (s/n): ")).upper().strip()[0]
        if continuar not in 'SN':
            print("Valor incorreto!")
        else:
            break
    lista.append(numero)
    flag = True
lista.sort()
print(lista)

#------------------Ex03------------------
print(f"{'Ex03':-^40}")
lista = []
num = int()
for i in range(0, 5):
    num = int(input("Digite um valor inteiro: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        for j in range(0 , len(lista)):
            if num < lista[j]:
                lista.insert(j, num)
                break
print(f"Lista em ordem crescente: {lista}")

#------------------Ex04------------------
print(f"{'Ex04':-^40}")
lista = []
continuar = "S"
cont = int(0)
while continuar == "S":
    lista.append(int(input("Digite um número inteiro: ")))

    while True:
        continuar = str(input("Deseja continuar (S/N): ")).upper().strip()[0]
        if continuar not in "NS":
            print("Valor incorreto!")
        else:
            break
    cont += 1
print(f"Foram armazenados {cont} valores")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}")
if 5 in lista:
    print("O número cinco foi armazenado!")
else:
    print("O número 5 não foi armazenado!")

#------------------Ex05------------------
print(f"{'Ex05':-^40}")
lista = []
pares = []
impares = []
contin = "S"
while contin == "S":
    lista.append(int(input("Digite um número inteiro: ")))
    while True:
        contin = str(input("Deseja continuar (S/N): ")).upper().strip()[0]
        if contin not in "SN":
            print("Valor incorreto!")
        else:
            break
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    if lista[i] % 2 == 1:
        impares.append(lista[i])
print("=-" * 20)
print(f"Lista contendo todos os números: {lista}")
print(f"Lista com os números pares: {pares}")
print(f"Lista com os números ímpares: {impares}")
'''
#------------------Ex06------------------
print(f"{'Ex06':-^40}")
matem = ""
abre = fecha = int(0)
matem = str(input(("Digite uma expressão matemática com parenteses: ")))
for i in range(0, len(matem)):
    if matem[i] == "(":
        abre += 1
    if matem[i] == ")":
        fecha += 1
if abre == fecha:
    print(f"a expressão {matem} é válida! ")
else:
    print(f"Falta parenteses na expressão {matem} ! ")