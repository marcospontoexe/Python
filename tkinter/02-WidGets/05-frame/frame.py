from tkinter import *

janela = Tk()  # instancia um objeto da classe Tk()

#-------------cria o frame----------------------------
fr = Frame(janela, borderwidth=1, relief="solid", width=200, height=200)
''' outras opções para relief:
flat, raised, sunken, solid
'''
fr.pack()
#-------------------------------------------------------

lb1 = Label(fr, text="Label 1", bg="yellow")     # cria um widget do tipo Label atribuido ao container pai "fr"
lb2 = Label(fr, text="Label 2", bg="green")


lb1.place(x=10, y=10)        # a propriedade "expand" deixa todos os widgets com o mesmo tamanho
lb2.place(x=50, y=30)





# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela["bg"] = "grey"  # altera o valor do índice do dicionário "janela"
janela.geometry("500x500+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta
# ----------------------------------------------------

