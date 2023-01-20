from tkinter import *

def semComando():
    print("contato adicionado!")

janela = Tk()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

barraMenu = Menu(janela)    #widget menu
menuContato = Menu(barraMenu, tearoff=0)    #Cria um item da barra de menu
#opções do item "menuContato"
menuContato.add_command(label="novo", command=semComando)
menuContato.add_command(label="pesquisar")
menuContato.add_command(label="apagar")
menuContato.add_separator()     #adiciona uma barra horizontal
menuContato.add_command(label="fechar", command=janela.quit)
menuContato.add_cascade(label="contatos", menu=menuContato)

janela.config(menu=barraMenu)

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta


