from biblioteca.trat_erros import *

def cabeçalho(txt):
    print("-=" * 20)
    print(txt.center(40))
    print("-=" * 20)


def menu(lista):
    cabeçalho("MENU")
    for p, v in enumerate(lista):
        print(f"{p+1:0>2} - {v}")
    print("--" * 20)
    op = leiaInt("Opção: ")
    if op > 0 and op <= len(lista):
        return op
    else:
        while True:
            print("\033[35mOpção inválida!!!\033[m")
            op = leiaInt("Opção: ")
            if op > 0 and op <= len(lista):
                return op
