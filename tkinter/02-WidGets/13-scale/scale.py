from tkinter import *

def escolha():
    print(f"Valor da escala: {sc.get()}")
def escolha1(val):
    print(f"Valor da escala: {sc.get()}")


janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

sc = Scale(janela, from_=0, to=100, orient=HORIZONTAL, resolution=10, command=escolha1)
sc.set(50)

sc.pack()

bt = Button(janela, text="Escolher", command=escolha)
bt.pack()

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta