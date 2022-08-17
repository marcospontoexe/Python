#pacote (biblioteca) é a junção de vários módulos

from biblioteca.interface import *   #importa todos as funções do módulo interface, do pacote biblioteca
from biblioteca.trat_erros import *
from biblioteca.arquivo import *


arq = "dados.txt"
if not arquivoExiste(arq):  #função do módulo arquivo
    criarArquivo(arq)       #função do módulo arquivo


while True:
    opção = menu(["Ver pessoas cadastradas", "Cadastrar pessoas", "Encerrar"])

    if opção == 1:
        lerArquivo(arq)
        print("--" * 20)
    if opção == 2:
        cabeçalho("Cadastrando...")
        cadastrar(arq, leiaNome("Nome: "), leiaInt("Idade: "))      #função cadastrar do módulo arquivo
    if opção == 3:
        cabeçalho("Saindo... Até logo!")
        break
