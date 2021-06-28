import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import scipy.io.wavfile as wav
import sys
import os
import math
import matplotlib.ticker as mticker
import time
import pyalsaaudio		#(https://stackoverflow.com/questions/23190348/alsaaudio-library-not-working)
from python_speech_features import mfcc, delta, logfbank
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer, SigmoidLayer
from pybrain.tools.customxml import NetworkWriter, NetworkReader
from functools import partial
from random import randrange, uniform,randint
from subprocess import call

seed = 143
np.random.seed(seed)

nInputs = 130
hidden_layers = 36
nOutputs = 10
net = NetworkReader.readFrom('model.xml')

periodo = 70
fs = 16000
limiar = 0.001
win = 3200
step = 800 
amostras_consecutivas = 10
grava = 0
jarbas = False
flag_comando = False
os.system('sudo service mosquitto start/')					#iniciar o broker
os.system('sudo chmod 777 -R /sys/class/gpio/')				#da permissao p acessar a pasta gpio
os.system('echo 9 > /sys/class/gpio/export')				#exportar o gpio 9
os.system('echo 10 > /sys/class/gpio/export')				#exportar o gpio 10
os.system('echo 20 > /sys/class/gpio/export')				#exportar o gpio 20
os.system('sudo chmod 777 -R /sys/class/gpio/gpio9')		#permissao para acessar o gpio 9
os.system('sudo chmod 777 -R /sys/class/gpio/gpio10')		#permissao para acessar o gpio 10
os.system('sudo chmod 777 -R /sys/class/gpio/gpio20')		#permissao para acessar o gpio 20
os.system('echo out > /sys/class/gpio/gpio9/direction')		#configurar gpio 20 com saida
os.system('echo out > /sys/class/gpio/gpio10/direction')	#configurar gpio 20 com saida
os.system('echo out > /sys/class/gpio/gpio20/direction')	#configurar gpio 20 com saida
os.system('echo 0 > /sys/class/gpio/gpio9/value')
os.system('echo 0 > /sys/class/gpio/gpio10/value')
os.system('echo 0 > /sys/class/gpio/gpio20/value')

while(True):
	# abre a interface de audio para leitura (1 canal, fs: 16KHz, 32 bits em float)
	inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
	inp.setchannels(1)
	inp.setrate(16000)
	inp.setformat(alsaaudio.PCM_FORMAT_FLOAT_LE)
	inp.setperiodsize(periodo)	

	# faz um loop ate gravar, pelo menos, 32000 amostras (2 seg @ 16KHz)

	os.system('clear')
	if(jarbas == False):
		total_size = fs*1
		f = open('tmp.bin', 'wb')
		os.system('echo 0 > /sys/class/gpio/gpio10/value')
		os.system('echo 0 > /sys/class/gpio/gpio20/value')
		os.system('echo 1 > /sys/class/gpio/gpio9/value')
		aux = '****** HIBERNANDO *******'
	else:	
		total_size = fs		
		if(flag_comando == False):
			os.system('echo 0 > /sys/class/gpio/gpio10/value')
			os.system('echo 0 > /sys/class/gpio/gpio9/value')	
			f = open('tmp.bin', 'wb')
			aux = 'O que_1?'
			os.system('echo 1 > /sys/class/gpio/gpio20/value')			
		else:
			f = open('tmp2.bin', 'wb')
			aux = 'O que_2?'
			os.system('echo 1 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 0 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 1 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 0 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 1 > /sys/class/gpio/gpio20/value')	
	print(aux)
	
	while total_size > 0:		
		# efetua uma leitura da porta de audio
		length, data = inp.read()
		# se a leitura trouxer dados, isto eh, l > 0, salva estas amostras no arquivo tmp.bin
		if(length > 0):
			# converte data para float32
			v = np.frombuffer(data, dtype=np.float32)
			# calcula a energia do quadro e, se for maior que o limiar, seta a flag para gravar
			energy = np.dot(v,v) / float(len(v))
			if(energy > limiar and grava == 0):
				grava = 1
			#print('energia: '+str(energy))
			#print(v)
			#print(len(v))
			#time.sleep(.5)
			if(grava == 1):
				f.write(data)
				#time.sleep(.001)
				total_size = total_size - length
	os.system('clear')
	f.close()	
	grava = 0

	if(jarbas == False or flag_comando == True):	
		print('Processando audio...')
		os.system('echo 1 > /sys/class/gpio/gpio9/value')
		os.system('echo 1 > /sys/class/gpio/gpio10/value')
		os.system('echo 1 > /sys/class/gpio/gpio20/value')
		if(jarbas == False):
			lim = 1
		else:
			lim = 2		
		for k in range(0, lim):
			# abre o arquivo temporario pra leitura
			if(k == 0):
				f = open('tmp.bin', 'rb')
			if(k == 1):
				f = open('tmp2.bin', 'rb')
			# carrega as amostras do audio (direto em float) para o vetor xi
			xi = np.fromfile(f, dtype=np.float32)
			# fecha o arquivo
			f.close()

			x = []
			x = np.append(xi[0], xi[1:] - 0.97 * xi[:-1])   #filtro de pre-enfase
			#python_speech_features.sigproc.preemphasis(xi, coeff=0.97)	#filtro de pre-enfase
			n = np.arange(0, len(x))

			#Calcula a energia contida no vetor x
			energy = np.zeros((len(x)-win)/step)	#define o tamanho do vetor energia
			for i in range(len(energy)):
				tmp = 0
				for j in range(i*step, i*step+win):	#calcula a energia dentro da janela definida
					tmp = tmp + x[j]*x[j]	
				energy[i] = tmp	#vetor com a energia a cada janela de amostras (600) no tempo, pulando em step por step(50).

			iMax = np.argmax(energy)	#indice  onde foi encontrado a maior valor da amostra(energy)
			vMax = energy[iMax]	#o valor da amostra

			#Cria um vetor com a taxa de cruzamento por zero
			taxa_zc = np.zeros((len(x)-win)/step)	#define o tamanho do vetor com a taxa de ZC (zero crossing)
			for i in range(len(taxa_zc)):
				crossing = 0
				for j in range((i*step)-1, i*step+win):	#verifica se houve cruzamento no zero
					if ((x[j] * x[j-1]) < 0):	
						crossing = crossing + 1	#quantidade de vezes que cruzou o zero
				taxa_zc[i] = crossing	#vetor com a quntidade de cruzamento no zero 
			# media de zc
			zc_med = (taxa_zc[len(taxa_zc)-2]+taxa_zc[len(taxa_zc)-1])/2

			#calcula o limiar inferior de energia
			A = 0.15
			lim_inferior = A*vMax

			#calcula o limiar da taxa de cruzamento por zero
			B = 0.75
			lim_zc = B*zc_med

			#verificacao do limiar inferior de energia para achar stop
			energia_menor = 0
			stop = len(energy)-1
			for i in range(iMax, len(energy)):	#varre o sinal do start ate o final do sinal (50 quadros)
				if (energy[i] >= lim_inferior):	
					energia_menor = 0
					if(i == len(energy)-1):
						stop = len(energy)	#marca a amosta onde ocorreu o evento
				else:	#momento em que a energia do sinal e menor que o limiar inferior de energia
					if(i == len(energy)-1):
						stop = len(energy)	#marca a amosta onde ocorreu o evento
					if (energia_menor == 5):
						stop = i	#marca a amosta onde ocorreu o evento
					energia_menor += 1
					if (energia_menor == amostras_consecutivas):	#interrompe a verificacao quando a energia e muito baixa
						energia_menor = 0		
						break 
			#verificacao do limiar de cruzamento por zero para achar stop
			for i in range(stop, len(taxa_zc)):
				if((taxa_zc[i] > lim_zc) and (energy[i] < lim_inferior)):#momento em que a taxa de CZ e maior que o limiar de CZ
					stop = i	#marca a amosta onde ocorreu o evento 
					break
				if(i == len(taxa_zc)-1):
					stop = len(taxa_zc)	#marca a amosta onde ocorreu o evento
			start = 0
			stop = (stop*step)+win
			
			y = np.zeros(len(x))
			for i in range(start, stop):
				y[i] = x[i]
				
			z = np.zeros(stop-start)
			
			for i in range(0,len(z)):
				z[i] = y[i+start]

			chunks = 10
			tempo_total = (float)(len(z))/fs
			
			mfcc_feat = mfcc(z,fs,winlen=tempo_total/chunks,winstep=tempo_total/chunks,numcep=13,nfilt=26,nfft=16384,lowfreq=50,preemph=0,appendEnergy=True,winfunc=np.hamming)	
			X_train = []
						
			for i in range(0, chunks):
				for j in range(0,13):					
					X_train.append(mfcc_feat[i][j])
			X_train = np.reshape(X_train, nInputs).astype('float32')
			indice = np.argmax(net.activate(X_train))
			activate = net.activate(X_train)
			os.system('clear')
			#print(indice)

			if(jarbas == False):
				N = len(activate)
				labels = ['jarbas','ligue','desligue','musica','sala','quarto','cozinha','ar-condicionado','tv','cafe']
				barra = range(N)
				plt.xticks(barra, labels, rotation='horizontal')
				comando1 = str(labels[np.argmax(activate)])
				print(comando1)
				time.sleep(1)
					
			else:				
				if(k == 0):
					N = len(activate)
					labels = ['jarbas','ligue','desligue','musica','sala','quarto','cozinha','ar-condicionado','tv','cafe']
					barra = range(N)
					plt.xticks(barra, labels, rotation='horizontal')
					comando1 = str(labels[np.argmax(activate)])
				if(k == 1):
					jarbas = False
					flag_comando = False
					N = len(activate)
					labels = ['jarbas','ligue','desligue','musica','sala','quarto','cozinha','ar-condicionado','tv','cafe']
					barra = range(N)
					plt.xticks(barra, labels, rotation='horizontal')
					comando2 = str(labels[np.argmax(activate)])
											
					comandinho = 'mosquitto_pub -h 192.168.43.142 -t jarbas -m ' + str(comando1) + '_' + str(comando2)
					print(comandinho)
					os.system(comandinho)
					time.sleep(1)
					
	else:
		flag_comando = True
