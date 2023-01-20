from tkinter import *
from tkinter import messagebox

janela = Tk()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("Janela principal")  # título da janela
janela.geometry("500x300+200+100")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.configure(background='#dde')
# ----------------------------------------------------

#----------messagebox de alertas---------------------------
messagebox.showinfo(title="menssagem", message="usando showINFO")
messagebox.showwarning(title="menssagem", message="usando showWARNING")
messagebox.showerror(title="menssagem", message="usando showERROR")
#--------------------------------------------------------------

lb = Label(janela, text="CONTINUAR:")
lb.pack()

#----------messagebox de iteração---------------------------
resposta = messagebox.askyesno("continuar", "deseja continuar?")
lb["text"] = resposta
''' outros tipos de messagebox:
messagebox.askokcancel() - mostra OK e CANCELAR
messagebox.askquestion() - mostra SIM e NÂO
messagebox.askretrycancel() - mostra REPETIR e CANCELAR
messagebox.askyesnocancel() - mostra SIM, NÃO  e CANCELAR
'''
#--------------------------------------------------------------



janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta