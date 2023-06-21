from tkinter import *



janela = Tk()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.configure(background='#dde')
# ----------------------------------------------------

def rbEsporte():
    lbResutadoE["text"] = vEsporte.get()

def rbCor():
    lbResutadoC["text"] = vCor.get()

def teste():
    print('teste')

lbEsportes = Label(janela, text="Esportes: ")
lbEsportes.pack(anchor=NW)

vCor = StringVar()
vEsporte = StringVar()

#------criando radio buttons para esporte, associado a StringVar() "vEsporte"----------------------
rbSkate = Radiobutton(janela, text="Skate", value="sk8", variable=vEsporte)       # "value" é o valor passado para o banco de dados por exemplo
rbSkate.pack(anchor=NW)
rbFutebol = Radiobutton(janela, text="Futebol", value="fut", variable=vEsporte)    # "vEsporte" recebe o valor de "value"
rbFutebol.pack(anchor=NW)
rbBasquete = Radiobutton(janela, text="Basquete", value="baskt", variable=vEsporte)
rbBasquete.pack(anchor=NW)
rbVolei = Radiobutton(janela, text="Volei", value="vol", variable=vEsporte)
rbVolei.pack(anchor=NW)

vEsporte.set("sk8")             # inicia o radiobutton com o valor 'sk8'

#---------------------------------------------------------------------------
btnE = Button(janela, text="Selecionar Esporte",command=rbEsporte)
btnE.pack(anchor=NW)
lbResutadoE = Label(janela, width=30)
lbResutadoE.pack(anchor=NW)

#------criando radio buttons para cor, associado a StringVar() "vCor"----------------------
rbVerde = Radiobutton(janela, text="Verde", value="#0f0", variable=vCor)       # "value" é o valor passado para o banco de dados por exemplo
rbVerde.pack(anchor=NE)
rbVermelho = Radiobutton(janela, text="Vermelho", value="#f00", variable=vCor)    # "vEsporte" recebe o valor de "value"
rbVermelho.pack(anchor=NE)
#---------------------------------------------------------------------------
btnC = Button(janela, text="Selecionar cor",command=rbCor)
btnC.pack(anchor=NE)
lbResutadoC = Label(janela, width=30)
lbResutadoC.pack(anchor=NE)


janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta


