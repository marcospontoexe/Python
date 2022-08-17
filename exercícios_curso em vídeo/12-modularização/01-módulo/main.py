import soma       #importa a bilioteca (pacote) inteira
from uteis import fat, dobro    #importa funções da biblioteca (pacote)


val = int(input("Digite um inteiro:"))
print(f"O fatorial de {val} é: {fat(val)}")  #chama a função fat

print(f"O dobro de {val} é: {dobro(val)}")          #chama a função dobro

print(f"A soma de {val} com 10 é: {soma.somando(val, 10)}")          #chama a função somando da biblioteca soma