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
if idade < 18:
    print('você ainda não tem idade para se alistar. Ainda faltam {} anos' .format(18-idade))
elif idade == 18:
    print('você tem {} anos e ja pode se alistar!'.format(idade))
else:
    print('seu prazo de alistamento já passou de {} anos!'.format(idade-18))