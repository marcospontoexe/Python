from tkinter import *
import tkinter as tk
import serial
import serial.tools.list_ports
import pytz            # para conversão de data hora UTC para local


ser = serial.Serial()
janela = Tk()  # instancia um objeto da classe Tk()
#janela = Toplevel()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("AJUSTES")  # título da janela
janela.geometry("330x330+220+50")  # define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.configure(background='#dde')
# ----------------------------------------------------

lsCom = []  # lista
# -------Listando as portas COM na interface
# Lista todas as portas disponíveis
ports = serial.tools.list_ports.comports()
# Imprime os nomes das portas COM disponíveis
for port in ports:
    lsCom.append(port.device)  # Adiciona no final da lista

# -----------------------------------

portaCom = StringVar()  # string dinâmica
portaCom.set(lsCom[0])  # define um valor padrão para a string
fuso = StringVar()



lbCom = Label(janela, text="Portas COM:", background='#7d8aa1', font=('Comic Sans MS', 10))
lbCom.place(x=32, y=10)
lbFuso = Label(janela, text="Fuso horário:", background='#7d8aa1', font=('Comic Sans MS', 10))
lbFuso.place(x=178, y=10)
# ----------criando option menu----------------------
opCom = OptionMenu(janela, portaCom, *lsCom)
opCom.place(x=30, y=40)
# ---------------------------------------------------

#------criando radio buttons para fuso horário----------------------
rbMenos12 = Radiobutton(janela, text='UTC-12', value="Etc/GMT+12", variable=fuso)
rbMenos12.place(x=150, y=40)
rbMenos12 = Radiobutton(janela, text='UTC-11', value="Etc/GMT+11", variable=fuso)
rbMenos12.place(x=150, y=60)
rbMenos12 = Radiobutton(janela, text='UTC-10', value="Etc/GMT+10", variable=fuso)
rbMenos12.place(x=150, y=80)
rbMenos12 = Radiobutton(janela, text='UTC-9', value="Etc/GMT+9", variable=fuso)
rbMenos12.place(x=150, y=100)
rbMenos12 = Radiobutton(janela, text='UTC-8', value="Etc/GMT+8", variable=fuso)
rbMenos12.place(x=150, y=120)
rbMenos12 = Radiobutton(janela, text='UTC-7', value="Etc/GMT+7", variable=fuso)
rbMenos12.place(x=150, y=140)
rbMenos12 = Radiobutton(janela, text='UTC-6', value="Etc/GMT+6", variable=fuso)
rbMenos12.place(x=150, y=160)
rbMenos12 = Radiobutton(janela, text='UTC-5', value="Etc/GMT+5", variable=fuso)
rbMenos12.place(x=150, y=180)
rbMenos12 = Radiobutton(janela, text='UTC-4', value="Etc/GMT+4", variable=fuso)
rbMenos12.place(x=150, y=200)
rbMenos12 = Radiobutton(janela, text='UTC-3', value="Etc/GMT+3", variable=fuso)
rbMenos12.place(x=150, y=220)
rbMenos12 = Radiobutton(janela, text='UTC-2', value="Etc/GMT+2", variable=fuso)
rbMenos12.place(x=150, y=240)
rbMenos12 = Radiobutton(janela, text='UTC-1', value="Etc/GMT+1", variable=fuso)
rbMenos12.place(x=150, y=260)
rbMenos12 = Radiobutton(janela, text='UTC+0', value="Etc/GMT", variable=fuso)
rbMenos12.place(x=180, y=280)
rbMenos12 = Radiobutton(janela, text='UTC+1', value="Etc/GMT-1", variable=fuso)
rbMenos12.place(x=230, y=40)
rbMenos12 = Radiobutton(janela, text='UTC+2', value="Etc/GMT-2", variable=fuso)
rbMenos12.place(x=230, y=60)
rbMenos12 = Radiobutton(janela, text='UTC+3', value="Etc/GMT-3", variable=fuso)
rbMenos12.place(x=230, y=80)
rbMenos12 = Radiobutton(janela, text='UTC+4', value="Etc/GMT-4", variable=fuso)
rbMenos12.place(x=230, y=100)
rbMenos12 = Radiobutton(janela, text='UTC+5', value="Etc/GMT-5", variable=fuso)
rbMenos12.place(x=230, y=120)
rbMenos12 = Radiobutton(janela, text='UTC+6', value="Etc/GMT-6", variable=fuso)
rbMenos12.place(x=230, y=140)
rbMenos12 = Radiobutton(janela, text='UTC+7', value="Etc/GMT-7", variable=fuso)
rbMenos12.place(x=230, y=160)
rbMenos12 = Radiobutton(janela, text='UTC+8', value="Etc/GMT-8", variable=fuso)
rbMenos12.place(x=230, y=180)
rbMenos12 = Radiobutton(janela, text='UTC+9', value="Etc/GMT-9", variable=fuso)
rbMenos12.place(x=230, y=200)
rbMenos12 = Radiobutton(janela, text='UTC+10', value="Etc/GMT-10", variable=fuso)
rbMenos12.place(x=230, y=220)
rbMenos12 = Radiobutton(janela, text='UTC+11', value="Etc/GMT-11", variable=fuso)
rbMenos12.place(x=230, y=240)
rbMenos12 = Radiobutton(janela, text='UTC+12', value="Etc/GMT-12", variable=fuso)
rbMenos12.place(x=230, y=260)


fuso.set("Etc/GMT+3")             # inicia o radiobutton com o valor definido pela string

#---------------------------------------------------------------------------


btFechar = Button(janela, bd=0, command=janela.destroy)
btFechar.place(x=20, y=200, width=110, height=80)
btFechar.config(background='#7d8aa1', foreground='#dde', borderwidth=2, text='Fechar', font=('Comic Sans MS', 20, 'bold'))

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta

# --------Usando a porta com selecionada------
ser.port = portaCom.get()  # recebe o endereço da porta com a ser usada
ser.baudrate = 115200       # muda o baud de 9600 (padrão) para 115200
print(f"PORTA USADA: {ser.name}")
ser.open()  # abre uma porta serial
print(f"Porta aberta: {ser.is_open}")  # verifica se a porta abriu
# ---------------------------------------------

#--------Configurando o fuso horário---------------
fusoLocal = pytz.timezone(fuso.get())       # fuso horário local
#--------------------------------------------------

