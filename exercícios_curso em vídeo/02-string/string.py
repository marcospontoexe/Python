valor = input('Digite um valor: ').strip()      # retira o espaço antes e depois da frase
print('O tipo primitivo da variável é:',type(valor))    #mostra o tipo de variável
print("É isnumeric()?", valor.isnumeric())
print("É alfabético?", valor.isalpha())
print("É alfanumérico?", valor.isalnum())
print("É isalnum()?", valor.isalnum())
print("É isdigit()?", valor.isdigit())              #numero inteiro
print("É isdecimal()?", valor.isdecimal())           #numero inteiro
print("É isidentifier()?", valor.isidentifier())
print("É istitle()?", valor.istitle())              #Primeira letra maiúscula


sex = input("Digite o sexo [M/F]:")
print(sex)

if sex in "Mm" or sex in "masculino":       #verifica se contem as letras dentro da string
    print("É homem!")
elif sex in "Ff" or sex in "feminino":
    print("É Mulher!")
else:
    print("Sexo inválido!")


print('{:-^40}'.format('Ex01'))
sexo = input("Digite seu sexo: ").strip().upper()[0]  # retira o espaço antes e depois da frase, e pega apenas o primeiro caractere digitado em maiúsculo
while sexo not in 'MF':
    sexo = input("Dados inválidos, digite seu sexo: ").strip().upper()[0]
    print(sexo)
if sexo == "M":
    print("Masculino!")
else:
    print("Feminino!")

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
nome1 = frase.split()                   #cria um vetor com as frases, sem o espaço.
print('nome.split(): {}'. format(nome1))
len1 = int(len(nome1))

print('Seu nome completo, sem contar o espaçamento, tem {} caracteres!\n' .format(len(frase)-frase.count(' ')))

#------------Ex 02-------------
print('{:-^30}' .format('Ex02'))
frase = frase.upper()               #transforma tudo em maiúsculo
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