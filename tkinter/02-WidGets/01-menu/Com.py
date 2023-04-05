from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Portas disponíveis")  # título da janela
janela.geometry(
    "500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.configure(background='#dde')
# ----------------------------------------------------

lsCom = ["skate", "basquete", "futebol", "volei"]  # lista

portaCom = StringVar()  # string dinâmica
portaCom.set(lsCom[0])  # define um valor padrão para a string

lbCom = Label(janela, text="Portas Com:")
lbCom.pack()
# ----------criando option menu----------------------
opCom = OptionMenu(janela, portaCom, *lsCom)  #
opCom.pack()
# ---------------------------------------------------

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta


