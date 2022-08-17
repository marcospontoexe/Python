'''
01 - Crie uma função leiaInt() e LeiaFloat(), incluindo a possibilidade da digitação de um tipo inválido;
02 - Crie um programa que verifique se o site "http://www.pudim.com.br/" está acessível
'''

def leiaInt(i):
    while True:
        try:
            temp = int(input(i))
        except (TypeError, ValueError):
            print("\033[34mERRO! Parâmetro incorreto.\033[m")
            continue  # retorna para o laço do while

        except (KeyboardInterrupt):
            print("Programa interrompido pelo usuário.")

        except Exception as erro:  # mostra qual foi o erro retornado pela exceção
            print(f"A classe do erro encontrado foi {erro.__class__}!")
        else:
            return temp


def leiaFloat(f):
    while True:
        try:
            temp = float(input(f))
        except (TypeError, ValueError):
            print("\033[34mERRO! Parâmetro incorreto.\033[m")
            continue  # retorna para o laço do while

        except (KeyboardInterrupt):
            print("Programa interrompido pelo usuário.")
        else:
            return temp


a = leiaInt("Digite um número inteiro: ")
print(f"{a} é do tipo {type(a)}")
b = leiaFloat("Digite um número Real: ")
print(f"{b} é do tipo {type(b)}")

#----------------------Ex 02-------------------
import urllib
import urllib.request
try:
    site = urllib.request.urlopen("http://www.pudim.com.br/")
except:
    print("O site está inacessível!")
else:
    print("O site está on-line!")
    print(f"Conteúdo da página: {site.read()}")
