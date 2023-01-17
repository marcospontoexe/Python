from tkinter import *
import tkinter as tk

janela = tk.Tk()    # instancia um objeto da classe Tk()

lb = Label(janela, text="teste!")     # cria um widget do tipo Label atribuido ao container pai "janela"
lb.place(x=100, y=100)        # atribui o gerenciador de layout "place" ao widget "lb", posicionando o widget dentro do container pai

janela.title("Janela principal")    # título da janela

janela["bg"] = "grey"      # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")       # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()   # cria um laço de repetição enquanto a janela estiver aberta