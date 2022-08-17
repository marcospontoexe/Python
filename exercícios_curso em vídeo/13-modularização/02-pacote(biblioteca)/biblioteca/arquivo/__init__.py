from biblioteca.interface import *
from biblioteca.trat_erros import *

def arquivoExiste(nome):
    '''
    A função retorna True caso o arquivo exista, False caso não exista.
    :param arq: nome do arquivo
    :return: True ou False
    '''
    try:
        a = open(nome, "rt")    #Abre o arquivo txt no modo de leitura (r) e tipo de arquivo texto (t)
        a.close()               #fecha o arquivo
    except FileNotFoundError:   #arquivo não encontrado
        print(f"\033[33mArquivo \033[m{nome}\033[33m não encontrado!\033[m")
        return False
    else:
        print(f"\033[33mArquivo \033[m{nome}\033[33m encontrado.\033[m")
        return True

def criarArquivo(nome):
    try:
        # abre o arquivo 'nome', no modo escrita (w) e tipo de arquivo texto (t). Caso o arquivo não exista o '+' cria o arquivo
        a = open(nome, "wt+")
        a.close()       #fecha o arquivo
    except:
        print(f"\033[33mHouve um erro na criação do arquivo \033[m{nome}.")
    else:
        print(f"\033[33mArquivo \033[m{nome}\033[33m criado com sucesso.\033[m.")

def lerArquivo(nome):
    try:
        a = open(nome, "rt") #Abre o arquivo tex no modo de leitura (r) e tipo de arquivo texto (t)
    except:
        print(f"\033[33mErro ao ler o arquivo \033[m{nome}")
    else:
        cabeçalho("Lista de cadastrados")
        #para passar cada linha do arquivo txt para uma lista: a.readlines()
        for linha in a:
            dados = linha.split(";")    #a lista dados recebe dois índices (nome e idade)
            dados[1] = dados[1].replace("\n","")        #substitui a quebra de linha por espaço vazio
            print(f"{dados[0]:<30}: {dados[1]:>3} anos")
    finally:
        a.close()           #conseguindo ler ou não o arquivo, o arquivo será fechado

def cadastrar(arq, nome, idade):
    try:
        a = open(arq, "at")     #Abre o arquivo txt no modo escrita (append) e tipo de arquivo texto (t)
    except:
        print(f"\033[33m Houve um erro na abertura do arquivo \033[m{arq}")
    else:
        try:
            a.write(f"{nome};{idade}\n")    #tenta escrever (append) no arquivo txt
        except:
            print(f"\033[33m Houve um erro na ao escrevar no arquivo \033[m{arq}")
        else:
            print(f"Novo registro de {nome} realizado.")
            a.close()

