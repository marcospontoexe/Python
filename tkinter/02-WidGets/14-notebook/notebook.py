from tkinter import *
from tkinter import ttk


janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

#------------criando um notebook-----------------------
nb = ttk.Notebook(janela)
nb.place(x=10, y=10, width=400, height=200)
#------------------------------------------------------

tb1 = Frame(nb)
tb2 = Frame(nb)
#----------------adicionando abas ao notebook-----------
nb.add(tb1, text="aba principal")
nb.add(tb2, text="arquivos")
#------------------------------------------------------

lb1 = Label(tb1, text="nome:")          # adiciona um label no frame "tb1"
lb1.pack()

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta