from tkinter import *
from tkinter import ttk    # sub biblioteca para usar o combo box
import tkinter as tk

def escolha():
    print(f"esporte selecionado: {lbEsp.get(ACTIVE)}")

def adicionar():
    lbEsp.insert(END, valor.get())

janela = Tk()  # instancia um objeto da classe Tk()

# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x200+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
# ----------------------------------------------------

listEsporte = ["skate", "basquete", "volei"]

valor = Entry(janela, width=50)
valor.pack()
btadd = Button(janela, text="Adicionar ao list box", command=adicionar)
btadd.pack()

#-----------cria um ListBox------------------
lbEsp = Listbox(janela)
for esporte in listEsporte:
    lbEsp.insert(END, esporte)      #insere "esporte" na ListBox
#----------------------------------------------

# Cria uma Scrollbar e a vincula ao Listbox
scrollbar = tk.Scrollbar(lbEsp)         # vincula um scrollbar à listbox
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    #posiciona o scroll do lado direito da listbox

lbEsp.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbEsp.yview)

lbEsp.place(x=150, y=45, width=200, height=100)


bt = Button(janela, text="escolher", command=escolha)
bt.place(x=220, y=150)


janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta