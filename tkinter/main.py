import tkinter as tk

janela = tk.Tk()    # instancia um objeto da classe Tk()

janela.title("Janela principal")    # título da janela
janela["bg"] = "green"      # altera o valor do índice do dicionário "janela"
janela.geometry("500x300+200+100")       # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.mainloop()   # cria um laço de repetição enquanto a janela estiver aberta