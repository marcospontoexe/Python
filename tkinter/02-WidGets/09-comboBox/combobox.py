from tkinter import *
from tkinter import ttk    # sub biblioteca para usar o combo box

def escolha():
    print(cbEsp.get())

janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

listEsporte = ["skate", "basquete", "volei"]

lbEsp = Label(janela, text="esportes")
lbEsp.pack()

cbEsp = ttk.Combobox(janela, values=listEsporte)        # cria o combo box
cbEsp.set("skate")                                      #define o valor skate como sendo o padrão do combo box
cbEsp.pack()

bt = Button(janela, text="escolher", command=escolha)
bt.pack()

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta