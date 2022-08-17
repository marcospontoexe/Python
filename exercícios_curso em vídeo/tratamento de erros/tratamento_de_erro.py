'''
try:(tenta executar o código.)
    OPERAÇÃO;

except: (caso aconteça algum erro (falha sintática) ou exceção (erro de semântica) no bloco try, é executado o bloco except)
    FALHOU;

else: (caso não retorne nehuma exceção ou erro no bloco try, é executado o bloco else)
    DEU CERTO;

finally: (o bloco sempre é executado)
    FALHOU ou DEU CERTO;

'''

try:
    a = int(input("Digite um inteiro: "))
    b = int(input("Digite outro inteiro: "))
    r = a / b

except (ValueError, TypeError):  # bloco executado quando as exceções 'ValueError ou TypeError' é gerada no bloco try
    print("Tivemos um problema com os valores digitado!")

except (ZeroDivisionError):  # bloco executado quando a exceção 'ZeroDivisionError' é gerada no bloco try
    print("Este programa não consegue dividor por zero!")

except KeyboardInterrupt:  # bloco executado quando a exceção 'KeyboardInterrupt' é gerada no bloco try
    print("O usuário preferiu não informar os dados!")


except Exception as erro:  # mostra qual foi o erro retornado pela exceção
    print(f"A classe do erro encontrado foi {erro.__class__}!")
    print(f"O erro encontrado foi {erro.__cause__}!")

else:
    print(f"O resutado foi {r:.2f}")

finally:
    print("Volte sempre.")

