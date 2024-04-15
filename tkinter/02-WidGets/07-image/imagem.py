from tkinter import *
import os

janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
# define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.geometry("500x500+200+100")
# ----------------------------------------------------

diretorio_script = os.path.dirname(os.path.realpath(
    __file__))  # caminho do diretório do script
foto = f"{diretorio_script}/mulher.gif"   # nome do arquivo

# img = PhotoImage(file="mulher.gif")        # para linux
img = PhotoImage(file=foto)        # para windows

lb = Label(janela, image=img)
lb.pack()

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
