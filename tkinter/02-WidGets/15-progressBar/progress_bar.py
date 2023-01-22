from tkinter import *
from tkinter import ttk
import time

def carregar():
    for i in range (0, 100):
        barra.set(i)
        time.sleep(0.05)
        janela.update()         # atualiza a janela 

janela = Tk()  # instancia um objeto da classe Tk()

barra = DoubleVar()
barra.set(0)

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

pb = ttk.Progressbar(janela, variable=barra, maximum=100)
pb.pack()

bt = Button(janela, text="Iniciar", command=carregar)
bt.pack()

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta