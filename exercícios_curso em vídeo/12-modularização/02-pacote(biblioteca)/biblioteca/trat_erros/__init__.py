

def leiaInt(i):
    while True:
        try:
            while True:
                temp = int(input(i))
                if temp >=0:
                    break
                else:
                    print("Digite uma idade maior doque zero!")

        except (TypeError, ValueError):
            print("\033[34mERRO. Apenas número inteiro!\033[m")
            continue
        except (KeyboardInterrupt):
            print("Programa interrompido pelo usuário.")
        else:
            return temp



def leiaNome(n):
    while True:
        temp = input(n).strip()
        if temp == "" or temp.isalpha() == False:
            print("\033[34mERRO! Escreva algum nome.\033[m")
        else:
            return temp
