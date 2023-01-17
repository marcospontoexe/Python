from tkinter import *

def clique():
    lb["text"] = "BOTÃO CLICADO!"   # altera o valor da chave "text" do dicionário "lb"


janela = Tk()    # instancia um objeto da classe Tk()

#-----CRIANDO UM LABEL NA JANELA-----
lb = Label(janela, text="teste!")     # cria um widget do tipo Label atribuido ao container pai "janela"
lb.place(x=100, y=200)        # atribui o gerenciador de layout "place" ao widget "lb", posicionando o widget dentro do container pai
#-----------------------------------

#-----CRIANDO UM BOTÃO NA JANELA-----
bt = Button(janela, width=10, text="ok")        # cria um widget "Button"
bt.place(x=100, y=10)                      # posiciona o widget com o gerenciador de layout
#-----------------------------------

#-------VINCULANDO UM BOTÃO À UMA FUNÇÃO----
bt1 = Button(janela, width=20, text="CLIQUE AQUI!", command=clique)        # o "command" cria um evento vinculado à uma função
bt1.place(x=100, y=50)
#------------------------------------------
janela.title("Janela principal")    # título da janela

janela["bg"] = "grey"      # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")       # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()   # cria um laço de repetição enquanto a janela estiver aberta