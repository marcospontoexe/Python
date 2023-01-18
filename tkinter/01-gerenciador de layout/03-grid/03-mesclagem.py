from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()

lb1 = Label(janela, width=20, height=6, bg="yellow")
lb2 = Label(janela, width=20, height=6,  bg="green")
lb3 = Label(janela, width=20, height=6,  bg="red")
lb4 = Label(janela, width=20, height=6,  bg="blue")
lb5 = Label(janela, width=5, bg="white")
lb6 = Label(janela, height=3,  bg="purple")

lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=1, column=0)
lb4.grid(row=1, column=1)
lb5.grid(row=0, column=2, rowspan=3, sticky=N+S)        # mescla 3 linhas no sentido norte-sul
lb6.grid(row=2, column=0, columnspan=2, sticky=W+E)     # mescla 2 colunas no sentido leste-oeste

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

