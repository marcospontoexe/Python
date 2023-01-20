from tkinter import *


def cadastrar():
    exec(open("cadastar.py").read())


janela = Tk()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.configure(background='#dde')
# ----------------------------------------------------

barraMenu = Menu(janela)    #widget menu

#---------------- menu de contatos------------------
menuContato = Menu(barraMenu, tearoff=0)    #Cria um menu que fica dentro da barra de menu
#itens do menu "menuContato"
menuContato.add_command(label="novo", command=cadastrar)
menuContato.add_command(label="pesquisar")
menuContato.add_command(label="apagar")
menuContato.add_separator()     #adiciona uma barra horizontal
menuContato.add_command(label="fechar", command=janela.quit)
barraMenu.add_cascade(label="CONTATOS", menu=menuContato)       # nome do menu visível na barra de menu, que herda os itens do "menuContato"
#--------------------------------------------------

#---------------- menu de edição------------------
menuEditar = Menu(barraMenu, tearoff=0)    #Cria outro menu que ficara dentro da barra de menu
#itens do menu
menuEditar.add_command(label="copiar")
menuEditar.add_command(label="recortar")
menuEditar.add_command(label="colar")
menuEditar.add_command(label="desfazer")
barraMenu.add_cascade(label="EDITAR", menu=menuEditar)
#--------------------------------------------------

janela.config(menu=barraMenu)   #adiciona a barra de menu

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta


