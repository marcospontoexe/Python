import math

num1 = float(input('digite um número: '))
raiz = math.sqrt(num1)
print('a raiz quadrada de {} é {:.3f}' .format(num1, raiz))
print('a raiz arredondada para cima é {}' .format(math.ceil(int(raiz))), end=' ')
print('e a raiz arredondada para baixo é {:.3f}' .format(math.floor(raiz)))

from datetime import date
print('{:-^30}' .format('Ex02'))
atual = date.today().year
nasc = int(input("Digite sua data de nascimento: "))
idade = atual - nasc
print('ano atual:', atual)
print('idade:', idade)


from random import randint
from time import sleep
#-------------Ex01-------------
print('{:-^30}' .format('Ex01'))
numero = int(input('Digite um numero inteiro de 1 a 5: '))
print('Processando...')
sleep(3)
comp = randint(1, 6)
print('O computador pensou no número {}.' .format(comp))
if numero == comp:
    print('Parabéns, vc é foda e acertou o número!')
else:
    print('Otário vc perdeu!')