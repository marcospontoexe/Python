
#-----------interactive help-----------------------
help(print)         #mostra informações sobre a função "print()"
print("-"*10)
print(print.__doc__)    #mostra informações sobre a função "print()"
#---------------------------------------------

#-----------doc string-----------------------
#a Docstring tras informações sobre a função
def area(altura, largura):
    """
    Essa função calcula o valor da área (em m2) de uma parede
    :param altura: É o valor em metros da altura da parede
    :param largura: É o valor em metros da largura da parede
    :return: Não retorna nada. A própria função imprime o valor da área
    """
    area = float(altura * largura)
    print(f"O valor da área é {area} m²!")
help(area)     #Com a Docstring descrita dentro das aspas triplas, é possível usar o função 'help()'
area(5.5, 10.9)
#---------------------------------------------

#-----------parâmetros opcionais----------------
def soma(a, b, c=0):        #c é um parÂmetro opcional. Caso não receba nenhum argumento para o parâmetro 'C', ele valerá zero.
    s = a + b + c
    print(f"A soma é {s}.")

soma(2, 3)                  #'C' vale zero.
#---------------------------------------------

#-----------escopo de variáveis----------------
def valor():
    global n3
    n3 = 0              #como n3 foi declarada como uma variável global, n3 deixa de valer 8 e passa a valer 0.
    n1 = 5              #o n1 é uma variável local, e esta alocada apenas dentro da função, apesar de já existir uma variável global n1
    print(f"Variável local n1 vale {n1}")
    print(f"Dentro da função n2 vale {n2}")
    print(f"Variável global n3 vale {n3}")

n1 = 2      # o n1 é uma variável global
n2 = 10
n3 = 8
valor()
print(f"Variável global n1 vale {n1}")
print(f"Fora da função n2 vale {n2}")
print(f"Variável global n3 vale {n3}")
#---------------------------------------------


def cabeçalho(msg):
    print("-=" * 20)
    print(f"{msg:^40}")
    print("-=" * 20)


cabeçalho("teste")

#--------------------------------------------------------------------------------
def soma (a, b):
    res = a + b
    return res
num = soma(2, 2)
print(num)

#-------------------multiplos parâmetros----------------------------------------------
lista = [1, 3, 5, 4, 4]
def dobra(lst):     #Aceita multiplos parâmetros de entrada, basta adicionar à lista
    for i in range(0, len(lst)):       #Dobra os elementos da lista
        lst[i] *= 2

print(lista)
dobra(lista)    # 'lista' está ligada a 'lst', e tudo que for alterado em um, é alterado na outra
print(lista)

#-------------------------empacotamento da parâmetros--------------------------------------
def contador(* num):     #o parâmetro de entrada é empacotado e vira uma tupla. Aceita multiplos parâmetros de entrada
    tamanho = len(num)
    return tamanho
print(f"a tupla contém {contador(1, 3, 6, 5)} números")


#--------------empacotamento da parâmetros--------------------------------------------------
def soma(* num):                  #empacota os valores
    soma = int(0)
    for v in num:                   #desempacota os valores
        soma += v
    return num, soma                #retorna uma lista com dois parÂmetros, o 1° parâmetro é uma lista com os valores,
    # e o 2° parâmetro é a soma desses valores

res = (soma(2, 3, 5))
print(f"A soma dos valores {res[0]} é {res[1]}")
#--------------------------------------------------------------------------------

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um inteiro: "))
if par(numero):
    print(f"o numero {numero} é par!")
else:
    print(f"o numero {numero} é ímpar!")

help(str.replace)