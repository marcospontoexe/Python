nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
peso = input('digite seu peso: ')

print('seu nome é {}, vc tem {} anos e pesa {} quilos!'.format(nome,idade,peso))

n1 = int(input('Digite um número: '))       #toda variável de entrada é do tipo string. o int() converte para int
print(type(n1))                             #mostra o tipo da variávell
n2 = int(input('Digite outro número: '))
res = n1+n2
print('A soma entre {} e {} vale {}!'.format(n1,n2,res))

print('oi'+'ola')
print('oi'*5)
valor = 'marcos'
print('olá {:<20}.'.format(valor))      #Alinha a string à esquerda, e completa a string com 20 caracteres nulo
print('olá {:20}.'.format(valor))
print('olá {:>20}.'.format(valor))      #Alinha a string à direita, e completa a string com 20 caracteres nulo
print('olá {:^20}.'.format(valor))         #Deixa a string com 20 caracteres, completando com caracteres nulos à esquerda e direita
print('olá {:=^21}.'.format(valor))     #Deixa a string com 21 caracteres, completando com '=' à esquerda e direita

numero = 5.65987445525
print('{:.3f}'.format(numero), end='-')     #formata o float com três números após a vírgula. O "end='-'" concatena o print posterior com o anterior
print('continuação da \nlinha anterior')

