from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()


lb1 = Label(janela, text="Label 1", bg="yellow")     # cria um widget do tipo Label atribuido ao container pai "janela"
lb2 = Label(janela, text="Label 2", bg="green")
lb3 = Label(janela, text="Label 3", bg="blue")
lb4 = Label(janela, text="Label 4", bg="red")

lb1.pack(fill=BOTH, expand=True)        # a propriedade "expand" deixa todos os widgets com o mesmo tamanho
lb2.pack(fill=BOTH, expand=True)
lb3.pack(fill=BOTH, expand=True)
lb4.pack(fill=BOTH, expand=True)


# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

