from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.configure(background='#dde')
# ----------------------------------------------------

lsEsporte = ["skate", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei", "basquete", "futebol", "volei"]           # lista
esporte = StringVar()
esporte.set(lsEsporte[0])       # define um valor padrão para a string

lbEsporte = Label(janela, text="Esporte:")
lbEsporte.pack()
#----------criando option menu----------------------
opEsporte = OptionMenu(janela, esporte, *lsEsporte)     #
opEsporte.pack()
#---------------------------------------------------

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta