'''
dados = ["marcos", 30]
pessoas = []
pessoas.append(dados)        #Faz uma ligação entre as duas lista. Alterar uma sublista tb altera a outra
dados[0] = "maria"
dados[1] = 18
pessoas.append(dados)
print(pessoas)          #as duas listas "pessoas", que estão condidas na lista ""dados, serão identicas
#------------------------------------------------------------------
dados = ["marcos", 30]
pessoas = []
pessoas.append(dados[:])        #Faz uma copia de uma lista para outra lista. Alterar uma sublista não altera a outra
dados[0] = "maria"
dados[1] = 18
pessoas.append(dados[:])
print(pessoas)          #as duas listas "pessoas", que estão condidas na lista ""dados, serão diferentes
#------------------------------------------------------------------
pessoas = [["marcos", 30], ["Maria", 28], ["Jose", 25]]     #tres listas dentro de uma lista
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])

#------------------------------------------------------------------
galera = [["marcos", 30], ["joana", 50], ["joaquin", 7], ["rosana", 9]]
for pessoa in galera:
    print(f"{pessoa[0]} tem {pessoa[1]} anos de idade.")
'''
#------------------------------------------------------------------
galera = []
dados = []
for i in range(0, 3):
    dados.append(input("Nome: "))
    dados.append(input("Idade: "))
    galera.append(dados[:])         #Adiciona uma sublista a uma lista
    dados.clear()               #limpa os índices 0 e 1 da sublista
print(galera)