from biblioteca.interface import *
from biblioteca.trat_erros import *

def arquivoExiste(nome):
    '''
    A função retorna True caso o arquivo exista, False caso não exista.
    :param arq: nome do arquivo
    :return: True ou False
    '''
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        print(f"\033[33mArquivo \033[m{nome}\033[33m não encontrado!\033[m")
        return False
    else:
        print(f"\033[33mArquivo \033[m{nome}\033[33m encontrado.\033[m")
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print(f"\033[33mHouve um erro na criação do arquivo \033[m{nome}.")
    else:
        print(f"\033[33mArquivo \033[m{nome}\033[33m criado com sucesso.\033[m.")

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print(f"\033[33mErro ao ler o arquivo \033[m{nome}")
    else:
        cabeçalho("Lista de cadastrados")
        for linha in a:
            dados = linha.split(";")
            dados[1] = dados[1].replace("\n","")
            print(f"{dados[0]:<30}: {dados[1]:>3} anos")


    finally:
        a.close()           #conseguindo ler ou nao o arquivo, o arquivo será fechado

def cadastrar(arq, nome, idade):
    try:
        a = open(arq, "at")
    except:
        print(f"\033[33m Houve um erro na abertura do arquivo \033[m{arq}")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print(f"\033[33m Houve um erro na ao escrevar no arquivo \033[m{arq}")
        else:
            print(f"Novo registro de {nome} realizado.")
            a.close()

