import math

num1 = float(input('digite um número: '))
raiz = math.sqrt(num1)
print('a raiz quadrada de {} é {:.3f}' .format(num1, raiz))
print('a raiz arredondada para cima é {}' .format(math.ceil(int(raiz))), end=' ')
print('e a raiz arredondada para baixo é {:.3f}' .format(math.floor(raiz)))