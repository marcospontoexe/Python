#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1 - QUantas letras tem, sem considerar os espaçoes;
#2 - quantas vezes aparece a letra 'a';
#3  --Em que posição o 'a' aparece pela primeira vez;
#4 - Em que posição o 'a' aparece pela ultima vez;
#5 - Leai o nome completo da pessoa e mostre apenas o priemiro e ultimo nome

#------------Ex 01-------------
print('{:-^30}' .format('Ex 01'))
frase = input('Digite seu nome completo! ').strip()
#frase = 'marcos daniel santana'
print(frase)
nome1 = frase.split()
len1 = int(len(nome1))

print('Seu nome completo, sem contar o espaçamento, tem {} caracteres!\n' .format(len(frase)-frase.count(' ')))

#------------Ex 02-------------
print('{:-^30}' .format('Ex02'))
frase = frase.upper()
print("A letra 'a' aparece {} vezes no seu nome completo!" .format(frase.count('A')))

#------------Ex 03-------------
print('{:-^30}' .format('Ex03'))
print("A letra 'a' aparece pela primeira vez na posição {}!" .format(frase.find('A')))

#------------Ex 04-------------
print('{:-^30}' .format('Ex04'))
print("A letra 'a' aparece pela ultima vez na posição {}!" .format(frase.rfind('A')))

#------------Ex 05-------------
print('{:-^30}' .format('Ex05'))
print('O primeiro nome é {}, e o ultimo nome é {}:' .format(nome1[0], nome1[len1-1]))

