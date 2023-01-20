from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()

#-----CRIANDO UM LABEL NA JANELA-----
lb = Label(janela, text="Nome:")     # cria um widget do tipo Label atribuido ao container pai "janela"
lb.place(x=10, y=10)        # atribui o gerenciador de layout "place" ao widget "lb", posicionando o widget dentro do container pai
#-----------------------------------


#-----------ENTRADA DE DADOS---------------------
dt = Entry(janela)  # entrada de texto para apenas um linha
dt.place(x=60, y=10)

#-----CRIANDO UM BOTÃO NA JANELA-----
bt = Button(janela, width=10, text="Cadastrar")        # cria um widget "Button"
bt.place(x=10, y=50)                      # posiciona o widget com o gerenciador de layout
#-----------------------------------

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"

janela.geometry("300x100+300+200")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

