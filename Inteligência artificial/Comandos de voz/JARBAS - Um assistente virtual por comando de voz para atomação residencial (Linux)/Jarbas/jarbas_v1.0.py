
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import scipy.io.wavfile as wav
import sys
import os
#import math
#import matplotlib.ticker as mticker
import time
import alsaaudio
import pybrain
from python_speech_features import mfcc, delta, logfbank
from pybrain.tools.customxml import NetworkReader

#from functools import partial
from random import randrange, uniform,randint
#from subprocess import call

seed = 176
np.random.seed(0) 
np.random.permutation(seed)
#np.random.seed(seed)

nInputs = 130
hidden_layers = 36
nOutputs = 10
net = NetworkReader.readFrom('model.xml')
limiar = 0.00005
periodo = 70
fs = 8000
grava = 0
jarbas = False
flag_comando = False
cont_gravacao = 0
'''
os.system('sudo service mosquitto restart/')				#iniciar o broker
os.system('sudo chmod 777 -R /sys/class/gpio/')			#da permissao p acessar a pasta gpio
os.system('echo 9 > /sys/class/gpio/export')			#exportar o gpio 9
os.system('echo 10 > /sys/class/gpio/export')			#exportar o gpio 10
os.system('echo 20 > /sys/class/gpio/export')			#exportar o gpio 20
os.system('sudo chmod 777 -R /sys/class/gpio/gpio9')		#permissao para acessar o gpio 9
os.system('sudo chmod 777 -R /sys/class/gpio/gpio10')		#permissao para acessar o gpio 10
os.system('sudo chmod 777 -R /sys/class/gpio/gpio20')		#permissao para acessar o gpio 20
os.system('echo out > /sys/class/gpio/gpio9/direction')		#configurar gpio 20 com saida
os.system('echo out > /sys/class/gpio/gpio10/direction')	#configurar gpio 20 com saida
os.system('echo out > /sys/class/gpio/gpio20/direction')	#configurar gpio 20 com saida
os.system('echo 0 > /sys/class/gpio/gpio9/value')
os.system('echo 0 > /sys/class/gpio/gpio10/value')
os.system('echo 0 > /sys/class/gpio/gpio20/value')
'''
#print(f"fs: {fs}")
while(True):
	# abre a interface de audio para leitura (1 canal, fs: 16KHz, 32 bits em float)
	inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
	inp.setchannels(2)
	inp.setrate(fs)
	inp.setformat(alsaaudio.PCM_FORMAT_FLOAT_LE)
	inp.setperiodsize(periodo)	
	#faz um loop ate gravar, pelo menos, 32000 amostras (2 seg @ 16KHz)
	#os.system('clear')
	if(jarbas == False):
		total_size = fs*0.8
		f = open('tmp.bin', 'wb')
		#os.system('echo 0 > /sys/class/gpio/gpio10/value')
		#os.system('echo 0 > /sys/class/gpio/gpio20/value')
		#os.system('echo 1 > /sys/class/gpio/gpio9/value')
		aux = '****** HIBERNANDO *******'
	else:	
		total_size = fs		
		if(flag_comando == False):
			#os.system('echo 0 > /sys/class/gpio/gpio10/value')
			#os.system('echo 0 > /sys/class/gpio/gpio9/value')	
			f = open('tmp.bin', 'wb')
			aux = 'O que_1?'
			#os.system('echo 1 > /sys/class/gpio/gpio20/value')			
		else:
			f = open('tmp2.bin', 'wb')
			aux = 'O que_2?'
			'''
			os.system('echo 1 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 0 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 1 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 0 > /sys/class/gpio/gpio20/value')
			time.sleep(.05)
			os.system('echo 1 > /sys/class/gpio/gpio20/value')
			'''
	print(aux)
	# abre um arquivo temporario para salvar as amostras do audio captado
	while total_size > 0:	
		#print(f"total_size: {total_size}")			
		#efetua uma leitura da porta de audio
		length, data = inp.read()
		#print(f"length: {length}")
		#print(f"data: {data}")
		#time.sleep(.5)
		# se a leitura trouxer dados, isto eh, l > 0, salva estas amostras no arquivo tmp.bin
		if(length > 0):
			# converte data para float32
			v = np.frombuffer(data, dtype=np.float32)
			# calcula a energia do quadro e, se for maior que o limiar, seta a flag para gravar
			energy = np.dot(v,v) / float(len(v))
			#print(f"energy: {energy}")
			#print(f"grava: {grava}")
			#time.sleep(.5)
			if(energy > limiar and grava == 0):
				grava = 1
			if(grava == 1):
				f.write(data)	#armazena no temp a cada 70 amostras
				total_size = total_size - length	
	#os.system('clear')
	f.close()	
	grava = 0
	
	if(jarbas == False or flag_comando == True):	
		print('Processando audio...')
		#os.system('echo 1 > /sys/class/gpio/gpio9/value')
		#os.system('echo 1 > /sys/class/gpio/gpio10/value')
		#os.system('echo 1 > /sys/class/gpio/gpio20/value')
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
			'''
			plt.subplot(2,1,1)
			plt.plot(xi)
			plt.subplot(2,1,2)
			plt.plot(x)
			plt.show()
			'''
	
			wav.write(f'audio_{str(cont_gravacao)}.wav', 16000, xi)
			cont_gravacao += 1
		
			chunks = 10
			tempo_total = (float)(len(x))/fs			
			mfcc_feat = mfcc(x,fs,winlen=tempo_total/chunks,winstep=tempo_total/chunks,numcep=13,nfilt=26,nfft=16384,lowfreq=50,preemph=0,appendEnergy=True,winfunc=np.hamming)	
			X_train = []
						
			for i in range(0, chunks):
				for j in range(0,13):					
					X_train.append(mfcc_feat[i][j])
			X_train = np.reshape(X_train, nInputs).astype('float32')
			indice = np.argmax(net.activate(X_train))
			activate = net.activate(X_train)
			#os.system('clear')
			if(jarbas == False):
				if(indice == 0):		
					jarbas = True	
					wav.write(f'Jarbas_{str(cont_gravacao)}.wav', 16000, xi)
					cont_gravacao += 1					
				else:
					'''	
					os.system('echo 0 > /sys/class/gpio/gpio9/value')
					os.system('echo 0 > /sys/class/gpio/gpio10/value')
					os.system('echo 0 > /sys/class/gpio/gpio20/value')
					os.system('echo 1 > /sys/class/gpio/gpio10/value')
					time.sleep(.03)
					os.system('echo 0 > /sys/class/gpio/gpio10/value')
					time.sleep(.03)
					os.system('echo 1 > /sys/class/gpio/gpio10/value')
					'''
					print('ops!')
					print('nao entendi, repita por favor!')
					#time.sleep(1)
							
			else:
				#os.system('echo 0 > /sys/class/gpio/gpio9/value')
				#os.system('echo 0 > /sys/class/gpio/gpio10/value')
				#os.system('echo 0 > /sys/class/gpio/gpio20/value')
				if(k == 0):
					N = len(activate)
					labels = ['jarbas','ligue','desligue','musica','sala','quarto','cozinha','ar-condicionado','tv','cafe']
					barra = range(N)
					plt.xticks(barra, labels, rotation='horizontal')
					comando1 = str(labels[np.argmax(activate)])
					wav.write(f"{str(comando1)} {str(cont_gravacao)}.wav", 16000, xi)
					cont_gravacao += 1
				if(k == 1):
					jarbas = False
					flag_comando = False
					N = len(activate)
					labels = ['jarbas','ligue','desligue','musica','sala','quarto','cozinha','ar-condicionado','tv','cafe']
					barra = range(N)
					plt.xticks(barra, labels, rotation='horizontal')
					comando2 = str(labels[np.argmax(activate)])
					if(comando2 == 'ligue' or comando2 == 'desligue'):						
						#comandinho = 'mosquitto_pub -h 192.168.43.142 -t jarbas -m ' + str(comando1) + '_' + str(comando2)
						comando = f"{comando1} + {comando2}"
						print(comando)
						#os.system(comando)
						#time.sleep(1)
						wav.write(f"{comando2} {cont_gravacao}.wav", 16000, xi)
						cont_gravacao += 1
					else:
						'''
						os.system('echo 0 > /sys/class/gpio/gpio9/value')
						os.system('echo 0 > /sys/class/gpio/gpio10/value')
						os.system('echo 0 > /sys/class/gpio/gpio20/value')
						os.system('echo 1 > /sys/class/gpio/gpio10/value')
						time.sleep(.03)
						os.system('echo 0 > /sys/class/gpio/gpio10/value')
						time.sleep(.03)
						os.system('echo 1 > /sys/class/gpio/gpio10/value')
						'''
						print('ops!')
						print('nao entendi, repita por favor!')
			
	else:
		flag_comando = True
