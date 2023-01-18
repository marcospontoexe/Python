from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()


lb1 = Label(janela, text="SIDE 1", bg="white")
lb2 = Label(janela, text="SIDE 2", bg="green")
lb3 = Label(janela, text="ANCHOR 1", bg="white")
lb4 = Label(janela, text="ANCHOR 2", bg="green")

lb1.pack(side=LEFT)     # o atributo "side" vincula uma extremidade a um widget
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)     # o atributo "anchor" vincula uma direção a um widget
lb4.pack(side=BOTTOM, anchor=SW)        # o atributo "side" precede o atributo "anchor"


# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "black"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

