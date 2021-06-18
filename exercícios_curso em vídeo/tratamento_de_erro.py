


try:
    a = int(input("Digite um inteiro: "))
    b = int(input("Digite outro inteiro: "))
    r = a/b

except (ValueError, TypeError):
    print("Tivemos um problema com o tipo de trat_erro digitado!")

except (ZeroDivisionError):
    print("Este programa não consegue dividor por zero!")

except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")


except Exception as erro:
    print(f"A classe do erro encontrado foi {erro.__class__}!")
    print(f"O erro encontrado foi {erro.__cause__}!")

else:
    print(f"O resutado foi {r:.2f}")

finally:
    print("Volte sempre.")