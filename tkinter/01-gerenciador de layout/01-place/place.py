from tkinter import *
from functools import partial # para invocar uma função e apontar uma lista de parâmetros de outro objeto a esta função invocada
def clique():
    lb["text"] = "BOTÃO CLICADO!"   # altera o valor da chave "text" do dicionário "lb"

def clique2(botao):
    lb["text"] = f"BOTÃO {botao['text']} CLICADO!"   # altera o valor da chave "text" do dicionário "lb"

def btCopiar():
    lb2["text"] = dt.get()


janela = Tk()  # instancia um objeto da classe Tk()


#-----CRIANDO UM LABEL NA JANELA-----
lb = Label(janela, text="teste!")     # cria um widget do tipo Label atribuido ao container pai "janela"
lb.place(x=10, y=180)        # atribui o gerenciador de layout "place" ao widget "lb", posicionando o widget dentro do container pai
#-----------------------------------

#-----CRIANDO UM BOTÃO NA JANELA-----
bt = Button(janela, width=10, text="ok")        # cria um widget "Button"
bt.place(x=10, y=10)                      # posiciona o widget com o gerenciador de layout
#-----------------------------------

#-------VINCULANDO UMA FUNÇÃO A UM BOTÃO----
bt1 = Button(janela, width=20, text="CLIQUE AQUI!", command=clique)        # o "command" cria um evento vinculado à uma função
bt1.place(x=10, y=40)
#------------------------------------------

#------USANDO VÁRIOS BOTÕES PARA INVOCAR A MESMA FUNÇÃO----------
bt2 = Button(janela, width=20, text="bt2")
# A função "partial" passa os atributos de "bt2" como atributo de entrada para a função "clique2"
bt2["command"] = partial(clique2, bt2)       # altera a chave "command" da instância "bt2".
bt2.place(x=10, y=70)

bt3 = Button(janela, width=20, text="bt3")
bt3["command"] = partial(clique2, bt3)
bt3.place(x=10, y=100)
#----------------------------------------------------------------

#-----------ENTRADA DE DADOS---------------------
dt = Entry(janela)
dt.place(x=200, y=10)
bt4 = Button(janela, width=20, text="Copiar", command=btCopiar)
bt4.place(x=200, y=40)
lb2 = Label(janela, text="              ")
lb2.place(x=200, y=70)
#------------------------------------------------

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
bt3["bg"] = "blue"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

