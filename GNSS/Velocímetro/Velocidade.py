from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import threading  # para criar uma thread paralela ao tkinter
import datetime
import serial
#import pandas as pd
import os       # para abrir um arquivo no windows
import subprocess, sys  # para abrir um arquivo no linux
import serial.tools.list_ports  #para listar as portas COM
import Com
import datetime     # para conversão de data hora UTC para local
import pytz            # para conversão de data hora UTC para local
import subprocess, sys  #para abrir arquivos do linux




SET_RATE_1 = b'\xb5\x62\x06\x08\x06\x00\x64\x00\x01\x00\x01\x00\x7a\x12'
SET_RATE_2 = b'\xb5\x62\x06\x08\x00\x00\x0e\x30'
dia = "DIA"
data = 'DATA'
hora = "HORA"
speed_str = ""
flag = 0


''' COORDENADAS DA VELSIS (GRAU DECIMAL)
-25 25.7960, -49 19.7240

'''
# Função para lidar com o evento de pressionar a barra de espaço
def on_space(event):
    global hora
    global speed_str
    if (speed_str == '0 km/h'):
        speed_str = 'Sem sinal'

    log_line = f"{hora} --- {speed_str}\r"
    flog = open('log.txt', 'at')  # Abre o arquivo txt no modo escrita (append) e tipo de arquivo texto (t)
    flog.writelines(log_line)
    flog.close()  # fecha o arquivo de log
    lstVel.insert(END, log_line)  # insere o valor no listBox
    print(f"velocidade capturada")


def vel():  #botão "btVel" pressionado (para capturar velocidade manualmente)
    global hora
    global speed_str
    if(speed_str == '0 km/h'):
        speed_str = 'Sem sinal'

    log_line = f"{hora} --- {speed_str}\r"
    flog = open('log.txt', 'at')  # Abre o arquivo txt no modo escrita (append) e tipo de arquivo texto (t)
    flog.writelines(log_line)
    flog.close()  # fecha o arquivo de log
    lstVel.insert(END, log_line)       # insere o valor no listBox
    #print(f"velocidade capturada")

def rstBtn():           # botão para limpar as coordenadas de captura de velocidade automática
    lstVel.delete(0, tk.END)
    lstVel.insert(END, 'últimos registros')  # insere o valor no listBox
    lstVel.insert(END, ' HORA   --- VELOCIDADE')  # insere o valor no listBox
    #print("RESET")


def read_serial():
    flag = 0  # flag para escrever o cabeçalho no documento de log
    global hora
    global dia
    global data
    global speed_str

    #----configurando uma taxa de atualização de 10Hz--------
    Com.ser.write(SET_RATE_1)  
    time.sleep(0.5)
    Com.ser.write(SET_RATE_2)
    #------------------------------------------------

    for i in range(1, 100):         # loop para descartar dados recebidos durante o 'cold start' do GNSS
        byte_data = Com.ser.readline()
        barra.set(i)                # incrementa a barra de carregamento
        #time.sleep(0.05)
        window.update()  # atualiza a janela
    pb.destroy()      # fecha a janela de carregamento


    while True:
        byte_data = Com.ser.readline()  # recebe o protocolo NMEA
        str_data_ln = byte_data.decode('ASCII')  # decodifica a classe do typo BYTES para STRING (em "ASCII")
        lista = str_data_ln.split(",")

        if (lista[0] == "$GNVTG"):
            velocidade = lista[7]
            if(velocidade == ''):
                lblVel.configure(text='Sem sinal') 
                velocidade = 0
            else:
                lblVel.configure(text=speed_str)  # atualiza a label
            
            speed_str = f"{velocidade} km/h"  # recebe a velocidade
            # --------------verifica se a velocidade medida está próxima da velocidade a ser calibrada (+-1 Km/h)---------
            if (((int(float(velocidade))) <= (sc.get() + 1)) and ((int(float(velocidade))) >= (sc.get() - 1))):
                lblVel["bg"] = "green"  # altera o back ground da Label de velocidade para verde (velocidade iguais)
            else:
                lblVel["bg"] = "red"  # altera o back ground da Label de velocidade para vermelho  (velocidades diferentes
            # --------------------------------------------------------------------------------------------
            

        if ((lista[0] == "$GNRMC") and (lista[2] == "A")):  # quando a lista recebe dados no protocolo GNRMC e A (effective positioning)
            diaUtc = lista[9]  # recebe uma string com o dia fornecida pelo GNSS (exemplo: ddmmyy)
            horaUtc = lista[1]  # rebe uma string com o horário UTC fornecido pelo GNSS (exemplo: hhmmss.ss)
            # ----- conversão de data e hora UTC para data e hora local-----------------------------
            datetime_obj = datetime.datetime.strptime((f'{diaUtc[:2]}/{diaUtc[2:4]}/20{diaUtc[4:]} {horaUtc[:2]}:{horaUtc[2:4]}:{horaUtc[4:6]}'), '%d/%m/%Y %H:%M:%S')  # converte de string para objeto datetime() (2023-04-05 20:33:51)
            tempoLocal = datetime_obj.replace(tzinfo=pytz.utc).astimezone(Com.fusoLocal)  # Converte o horário UTC para o timezone local (2023-04-05 17:33:51)
            strTempoLocal = str(tempoLocal)  # converte para string

            dia = f"{strTempoLocal[8:10]}/{strTempoLocal[5:7]}/{strTempoLocal[:4]}"
            hora = f"{strTempoLocal[11:13]}:{strTempoLocal[14:16]}:{strTempoLocal[17:19]}"  # fuso horário -3
            data = f"{dia} - {hora}"
            # ---------------------------------------------------------------------

            if (flag == 0):         # execulta apenas na inicialização do programa
                flog = open('log.txt', 'at')  # Abre o arquivo txt no modo escrita (append) e tipo de arquivo texto (t)
                log_line = f"Início do teste - {data}\n\r"
                flog.writelines(log_line)
                flog.close()  # fecha o arquivo de log
                flag = 1


def abrirLog():    # ação do menu
    diretorio = 'log.txt'
    if sys.platform == "win32":
        os.startfile(diretorio)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, diretorio])
    
def rstLog():    # ação do menu
    global data
    flog = open('log.txt', 'wt')  # Abre o arquivo txt no modo escrita (write) e tipo de arquivo texto (t)
    log_line = f"Início do teste - {data}\n\r"
    flog.writelines(log_line)
    flog.close()  # fecha o arquivo de log


#--------função para saber a posição do mouse na tela (para ajustar o widget Bind ("place") )---
def botaoEsquerdo(retorno):
    print(f"x={retorno.x} | y={retorno.y} | geometria={window.geometry()}")
#------------------------------------------------------------------------------



window = Tk()
window.title("GPS SPEED")
#window.attributes('-fullscreen',True)
window.geometry('800x480+0+0')          # tamanho da tela
window.resizable(height=0, width=0)  # desabilita o ajuste manual do tamanho da janela

#window.bind("<Button-1>", botaoEsquerdo)       # evento para botão esquerdo do mouse (usado apenas para mostrar a posição (X,Y) do clique do mouse na tela)

#-------------funação chamada a partir da barra e espaço-----
window.bind("<space>", on_space)
#------------------------------------------------------------

#--------Imagens usadas-----------------------------
imgMain = PhotoImage(file="imagens/main.png")
imgRst = PhotoImage(file="imagens/reset.png")
imgVel = PhotoImage(file="imagens/vel.png")
imgLog = PhotoImage(file="imagens/log.png")
#----------------------------------------------------


lblMain = Label(window, image=imgMain)      # carrega a imagem em tela cheia
lblMain.pack()

#-----------barra de progresso----------------------------
barra = DoubleVar()
barra.set(0)
pb = ttk.Progressbar(window, variable=barra, maximum=100)
pb.place(x=144, y=14, width=615)
#----------------------------------------------------

#----------Label para mostra valores na tela-------------
lblVel = Label(window, font=('Comic Sans MS', 20, 'bold'))          # velocidade
lblVel.place(x=198, y=159, width=255, height= 65)
lblVel.configure(text='CARREGANDO...')
#------------------------------------------------------------

#------Botões-----------------------------------------------
btRst = Button(window, bd=3, relief=tk.RIDGE, image=imgRst, command=rstBtn)  # botão de para limpar valores
btRst.place(x=525, y=300, width=150, height=80)
btVel = Button(window, bd=3, relief=tk.RIDGE, image=imgVel, command=vel)     # botão para capturar a velocidade
btVel.place(x=525, y=150, width=150, height=80)
btnLog = Button(window, bd=3, relief=tk.RIDGE, image=imgLog, command=abrirLog)     # botão para abrir os registros salvos
btnLog.place(x=300, y=300, width=150, height=80)
#------------------------------------------------------------





#---------------- Configurando o menu------------------
barraMenu = Menu(window)    #widget menu
#---------------SUB MENU----------------------
menuMain = Menu(barraMenu, tearoff=1)    #Cria um menu que fica dentro da barra de menu
#itens do menu "menuMain"
#menuMain.add_separator()     #adiciona uma barra horizontal
menuMain.add_command(label="Fechar", command=window.destroy)
barraMenu.add_cascade(label="FECHAR", menu=menuMain)       # nome do menu visível na barra de menu, que herda os itens do "menuMain"
#---------------SUB MENU----------------------
limparRegistro = Menu(barraMenu, tearoff=1)    #Cria outro menu que ficara dentro da barra de menu
#itens do menu registro
limparRegistro.add_command(label="Apagar tudo", command=rstLog)
barraMenu.add_cascade(label="APAGAR REGISTROS", menu=limparRegistro)

window.config(menu=barraMenu)   #adiciona a barra de menu
#--------------------------------------------------

#----adicionando um Scale----------------------
sc = Scale(window, from_=10, to=120, orient=HORIZONTAL, resolution=10)
sc.set(80)
sc.place(x=357, y=57, width=415, height=50)
#--------------------------------------------------

#-----------cria um ListBox------------------
#lbVel = Listbox(window, text="ÚLTIMOS REGISTROS", borderwidth=1, relief="solid", width=200, height=200, bg="#B0C4DE")
lstVel = Listbox(window)
lstVel.place(x=60, y=270, width=200, height=150)
lstVel.insert(END, 'últimos registros')  # insere o valor no listBox
lstVel.insert(END, ' HORA   --- VELOCIDADE')  # insere o valor no listBox
#----------------------------------------------

#---Cria uma Scrollbar e a vincula ao Listbox------
scrollbar = tk.Scrollbar(lstVel)   # vincula um scrollbar à listbox
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)        #posiciona o scroll do lado direito da listbox

lstVel.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lstVel.yview)
#----------------------------------------------

t1 = threading.Thread(target=read_serial, name=1)

t1.start()
window.mainloop()       # o código fica travado nessa linha, até que a janela do tkinter seja fechada



