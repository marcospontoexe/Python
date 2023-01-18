from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()

lb1 = Label(janela, text="Label 1", width=20, height=5, bg="yellow")
lb2 = Label(janela, text="Label 2", bg="green")
lb3 = Label(janela, text="Label 3", bg="red")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0, sticky=E)         # a propriedade "stick" configura o posicionamento do conteudo de cada widget (N, S, W e E)
lb3.grid(row=0, column=1, sticky=S)

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------