'''
lanche = () #tupla
lanche = [] #lista
lanche = {} #dicionário
'''

# Tuplas são imutáveis

dados = ('Marcos', 30, 'Masculino', 57.20)  #Diferente de vetores, tuplas aceitam qualquer tipo de variáveia na mesma tupla
print(dados)
del(dados)  #apaga a tupla

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
almoço = 'feijão', 'macarrão', 'arroz', 'carne'
print(f'lanche: {lanche}')
print(f'almoço: {almoço}')
print(f'lanche + almoço: {lanche + almoço}')  #concatena as duas tuplas

print(f'almoço[:2]: {almoço[:2]}')  #mostra do índice 0 até o 1° índice
print(f'almoço[-1]: {almoço[-1]}')  #mostra do ultimo da tupla
print(f'almoço[-2]: {almoço[-2]}')  #mostra do penultimo da tupla
print(f'almoço[:-1]: {almoço[:-1]}')  #mostra do 1° índice da tupla até o -2
#----------------------------------------------------
for comida in lanche:
    print(f'Eu vou comer {comida}')     #imprime os índices da tupla 'lanche'
print(f"{'-'*20}")
for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}, na posição {i}')
print(f"{'-'*20}")
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')   #mostra o valor do índice e o índice
print(f"{'-' * 20}")
#----------------------------------------------------
print(sorted(lanche))   #mostra em ordem alfabética

print(lanche.index('Suco')) #mostra em que ´posição se encontra o 'Suco'. Mostra apenas o primeira ocorrência.
numeros = ('1', '3', '4', '1', '2', '5', '7')
print(numeros.index('1', 1)) #mostra em que posição se encontra o '1', a partir da primeira posição
print(numeros.count('1'))   #mostra quantas vezes o número '1' aparece na tupla

