from tkinter import *
#from tkinter import ttk


janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

def botaoEsquerdo(retorno):
    print(f"x={retorno.x} | y={retorno.y} | geometria={janela.geometry()}")

janela.bind("<Button-1>", botaoEsquerdo)       # evento para botão esquerdo do mouse

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta