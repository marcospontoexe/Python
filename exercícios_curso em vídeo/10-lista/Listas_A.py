'''
lanche = () #tupla
lanche = [] #lista
lanche = {} #dicionário
'''

#lista é parecido com Tupla, porem pode adicionar e apagar índices e também os valores dos índices

lanche = ["Hamburger", "Suco", "Pizza", "Pudim"]
lanche.append("Chocolate")  #Adiciona no final da lista
lanche.insert(0, "Cerveja") #Adiciona na posição 0
del lanche[0]   #apaga o item da posição 0
lanche.pop(1)   #apaga o item da posição 1
lanche.pop()    #apaga o ultimo elemento
lanche.remove("Pizza")   #Apaga pelo conteudo encontrado na primeira ocorrência
if "Pizza" in lanche:   #para evitar erros
    lanche.remove("Pizza")  #erro de sintaxe caso não encontre a string "Pizza"

lanche.clear()  #apaga os dados da lista
valores = list(range(5,11))     #cria um lista com valores do 5 até o 10
valores.sort(reverse=True)      #organiza os valores de trás pra frente
#***********************************************
lista = []
for i in range(0,3):
    lista.append(input("Digite um valor: "))
print(lista)

#********************************************
a = [1, 2, 3, 4]
b = a           #faz uma ligação entre as duas lista. Alterar uma, altera a outra tb
b[2] = 9
print(f"Lista a: {a}")
print(f"Lista b: {b}")
#********************************************

a = [1, 2, 3, 4]
b = a [:]          #faz uma cópia de uma lista. Alterar uma, não altera a outra
b[2] = 9
print(f"Lista a: {a}")
print(f"Lista b: {b}")