'''
lanche = () #tupla
lanche = [] #lista
lanche = {} #dicionário
'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
almoço = ('feijão', 'macarrão', 'arroz', 'carne')
print(lanche)
#----------------------------------------------------
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f"{'-'*20}")
for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}, na posição {i}')
print(f"{'-'*20}")
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {lanche[i]}, na posição {pos}')
print(f"{'-' * 20}")
#----------------------------------------------------
print(sorted(lanche))   #mostra em ordem alfabética
print(lanche + almoço)
print(lanche.index('Suco')) #mostra em que ´posição se encontra o 'Suco'. Mostra apenas o primeira ocorrência.
numeros = ('1', '3', '4', '1', '2', '5', '7')
print(numeros.index('1', 1)) #mostra em que posição se encontra o '1', a partir da primeira posição

dados = ('Marcos', 30, 'Masculino', 57.20)
print(dados)    #Diferente de vetores, tuplas aceitam qualquer tipo de variáveia na mesma tupla
del(dados)  #apaga a tupla
