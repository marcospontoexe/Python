from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x500+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------


img = PhotoImage(file="mulher.gif")
lb = Label(janela, image=img)
lb.pack()

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta