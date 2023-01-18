from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()


lb1 = Label(janela, text="Label 1", bg="yellow")
lb2 = Label(janela, text="Label 2", bg="green")
lb3 = Label(janela, text="Label 3", bg="red")
lb4 = Label(janela, text="Label 4", bg="blue")

lb1.grid(row=1, column=1)      # atribui o gerenciador de layout "grid" ao widget "lb1", posicionando o widget dentro do container pai
lb3.grid(row=1, column=2)
lb2.grid(row=1, column=5)
# o gerenciador de layout "grid" não permite células vazias, deixando todos widgets adjacentes
lb4.grid(row=3, column=7)


# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

