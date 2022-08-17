#pacote (biblioteca) é a junção de vários módulos

from biblioteca.interface import *
from biblioteca.trat_erros import *
from biblioteca.cadastro import *
from biblioteca.arquivo import *

arq = "dados.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    opção = menu(["Ver pessoas cadastradas", "Cadastrar pessoas", "Encerrar"])

    if opção == 1:
        lerArquivo(arq)
        print("--" * 20)
    if opção == 2:
        cabeçalho("Cadastrando...")
        cadastrar(arq, leiaNome("Nome: "), leiaInt("Idade: "))
    if opção == 3:
        cabeçalho("Saindo... Até logo!")
        break
