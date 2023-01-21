from tkinter import *

def futClick():
    print(f"futebol: {futebol.get()}")

def volClick():
    print(f"futebol: {volei.get()}")

def basqClick():
    print(f"futebol: {basquete.get()}")

janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

futebol = StringVar()
basquete = StringVar()
volei = StringVar()

#--------criando check button---------------
cbFut = Checkbutton(janela, text="futebol", variable=futebol, onvalue="sim", offvalue="nao", command=futClick)
cbFut.pack(side=LEFT, padx=10)
cbVol = Checkbutton(janela, text="volei", variable=volei, onvalue="sim", offvalue="nao", command=volClick)
cbVol.pack(side=LEFT, padx=10)
cbBasq = Checkbutton(janela, text="basquete", variable=basquete, onvalue="sim", offvalue="nao", command=basqClick)
cbBasq.pack(side=LEFT, padx=10)
#-------------------------------------------

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta