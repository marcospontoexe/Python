from tkinter import *

def imprimir():
    print(sb2.get())

janela = Tk()  # instancia um objeto da classe Tk()
valores = ["1", "10", "20", "30", "40", "50"]
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

sb1 = Spinbox(janela, from_=0, to=10)
sb1.pack()

sb2 = Spinbox(janela, values=valores)
sb2.pack()

bt = Button(janela, text="imprimir valor", command=imprimir)
bt.pack()

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta