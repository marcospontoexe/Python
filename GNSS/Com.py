from tkinter import *
import serial
import serial.tools.list_ports
import pytz            # para conversão de data hora UTC para local


ser = serial.Serial()
janela = Tk()  # instancia um objeto da classe Tk()
# janela = Toplevel()  # instancia um objeto da classe Tk()
# ----------CONFIGURAÇÕES DA JANELA-------------------
janela.title("AJUSTES")  # título da janela
# define o posicionamento e tamanho da tela (largura X altura + distância à esqueda + dist topo) em pixel
janela.geometry("300x200+200+100")
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
lsFuso = [
    'UTC-12',
    'UTC-11',
    'UTC-10',
    'UTC-9',
    'UTC-8',
    'UTC-7',
    'UTC-6',
    'UTC-5',
    'UTC-4',
    'UTC-3',
    'UTC-2',
    'UTC-1',
    'UTC 0',
    'UTC+1',
    'UTC+2',
    'UTC+3',
    'UTC+4',
    'UTC+5',
    'UTC+6',
    'UTC+7',
    'UTC+8',
    'UTC+9',
    'UTC+10',
    'UTC+11',
    'UTC+12'
]
fuso.set(lsFuso[9])

lbCom = Label(janela, text="Portas COM:",
              background='#7d8aa1', font=('Comic Sans MS', 8))
lbCom.place(x=14, y=15)
lbFuso = Label(janela, text="Fuso horário:",
               background='#7d8aa1', font=('Comic Sans MS', 8))
lbFuso.place(x=150, y=15)
# ----------criando option menu----------------------
opCom = OptionMenu(janela, portaCom, *lsCom)
opCom.place(x=10, y=40)
opFuso = OptionMenu(janela, fuso, *lsFuso)
opFuso.place(x=150, y=40)
# ---------------------------------------------------

btFechar = Button(janela, bd=0, command=janela.destroy)
btFechar.place(x=100, y=100, width=110, height=50)
btFechar.config(background='#7d8aa1', foreground='#dde', borderwidth=2,
                text='Concluir', font=('Comic Sans MS', 20, 'bold'))

janela.mainloop()  # cria um laço de repetição enquanto a janela estiver aberta

# --------Usando a porta com selecionada------
ser.port = portaCom.get()  # recebe o endereço da porta com a ser usada
ser.baudrate = 115200       # muda o baud de 9600 (padrão) para 115200
print(f"PORTA USADA: {ser.name}")
ser.open()  # abre uma porta serial
print(f"Porta aberta: {ser.is_open}")  # verifica se a porta abriu
# ---------------------------------------------

# --------Configurando o fuso horário---------------
# recebe apenas os dois u´ltimos índices da string convertido para int
fusoInt = int(fuso.get()[-2:])

if (fusoInt > 0):
    fusoStr = f'Etc/GMT-{abs(fusoInt)}'
elif (fusoInt < 0):
    fusoStr = f'Etc/GMT+{abs(fusoInt)}'
else:
    fusoStr = f'Etc/GMT'

fusoLocal = pytz.timezone(fusoStr)       # fuso horário local
# --------------------------------------------------
