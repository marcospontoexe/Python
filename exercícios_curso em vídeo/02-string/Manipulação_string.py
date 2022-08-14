
frase = 'Aula de Python do Youtub'
for i in range (10):
    print(frase[i], end='-')
for i in range (10,int(len(frase))-1):
    print(frase[i], end=' -')
print(frase[int(len(frase))-1])
for i in range (len(frase)):
    print('{}'.format(i),end='-')
print('\n')
# a-u-l-a- -d-e- -p-y-t -h -o -n -  -d -o -  -y -o -u -t -u -b
# 0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23
frase2 = """escrever um texto inteiro de uma só vez 
         escrever um texto inteiro de uma só vez 
         escrever um texto inteiro de uma só vez"""
print('"""escrever um texto inteiro de uma só vez"""=', frase2)
print('frase[:10]=', frase[:10])                #mostra do índice 0 até o 10°
print('frase[10::2]=', frase[10::2])        #mostra do índice 10 até o último índice, pulando de 2 em 2 índices
print('frase[::-1]=', frase[::-1])          #mostra do último índice até o 1°
print("frase.count('a')=", frase.count('a'))
print("frase.count('o',10:)", frase.count('o',10,))
print("frase.find('pyt')=", frase.find('pyt'))
print("frase.find('loucura')", frase.find('loucura'))
print("'aula' in frase=", 'aula' in frase)
print("frase.replace('Youtub','Caraio') =", frase.replace('Youtub', 'Caraio'))
print('frase =', frase)
print("frase = frase.replace('Youtub','Caraio')")
frase = frase.replace('Youtub','Caraio')
print('print(frase)= ',frase)
print('\n')
frase = 'Aula de Python do Youtub'
print("frase.upper()=", frase.upper())
frase = 'Aula de Python do Youtub'
print('frase.lower()', frase.lower())
print('frase.capitalize()=', frase.capitalize())
print('frase.title()=', frase.title())
print('\n')
frase = 'Aula de Python do Youtub'
print('frase.split()=', frase.split())          #quebra a frase em palavras
print('frase.split()[1]=', frase.split()[1])    #mostra a plavra do primeiro índice
print('frase.split()[2][1]=', frase.split()[2][1])      #mostra a segunda letra do segundo índice
print("'-'.join(frase.split())=", '-'.join(frase.split()))
print("'-'.join(frase))=", '-'.join(frase))
print('\n')

frase = '             Aula de Python do Youtub   '
print('frase=', frase)
print('frase.strip()=', frase.strip())          #remove os espaços antes e após a frase
frase = '             Aula de Python do Youtub   '
print('frase=', frase)
print('frase.rstrip()=', frase.rstrip())            #remove os espaços à direita
frase = '             Aula de Python do Youtub   '
print('frase=', frase)
print('frase.lstrip()=', frase.lstrip())


sex = input("Digite o sexo [M/F]:")
print(sex)