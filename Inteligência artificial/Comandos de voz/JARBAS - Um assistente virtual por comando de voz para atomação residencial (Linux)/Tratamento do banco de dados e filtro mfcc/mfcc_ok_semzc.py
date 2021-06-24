# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import scipy.io.wavfile as wav
import sys
import os
import math
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank


for comando in range(10):
	if (comando == 0):
		comando_aux = '10-Jarbas' 
	if (comando == 1):
		comando_aux = '11-Ligue' 
	if (comando == 2):
		comando_aux = '12-Desligue' 
	if (comando == 3):
		comando_aux = '13-Música'
	if (comando == 4):
		comando_aux = '14-Sala'
	if (comando == 5):
		comando_aux = '15-Quarto' 
	if (comando == 6):
		comando_aux = '16-Cozinha' 
	if (comando == 7):
		comando_aux = '17-Ar-Condicionado' 
	if (comando == 8):
		comando_aux = '18-TV'
	if (comando == 9):
		comando_aux = '19-Café'

	#for speaker in range(1, 491):
	for speaker in range(1, 1591):
		audio = str(comando_aux)+str('/')+str(speaker)+'.wav'
		[fs,xi] = wav.read(audio)
		xi = xi / 32768.0
		estalo = 100
		xi[0:estalo] = 0   #zera as primeiras amostras do audio
		
		x = []
		x = np.append(xi[0], xi[1:] - 0.97 * xi[:-1])   #filtro de pre-enfase

		n = np.arange(0, len(x))

		win = 3200
		step = 800 
		#Calcula a energia contida no vetor x
		energy = np.zeros((len(x)-win)/step)	#define o tamanho do vetor energia
		for i in range(len(energy)):
			tmp = 0
			for j in range(i*step, i*step+win):	#calcula a energia dentro da janela definida
				tmp = tmp + x[j]*x[j]	#somatório das amostras ao quadrado dentro da janela
			energy[i] = tmp	#vetor com a energia a cada janela de amostras (600) no tempo, pulando em step por step(50).

		iMax = np.argmax(energy)	#indice  onde foi encontrado a maior valor da amostra(energy)
		vMax = energy[iMax]	#o valor da amostra

		
		#calcula o limiar inferior de energia
		A = 0.07
		lim_inferior = A*vMax

		if(iMax == 0):
			start = 0
		if(iMax == len(energy)-1):
			stop = len(energy)

		#verificação do limiar inferior de energia para achar start
		energia_menor = 0
		amostras_consecutivas = 10
		for i in range(iMax, 0, -1):	#varre o sinal do pico de energia até o inicio do sinal
			if (energy[i] >= lim_inferior):	
				energia_menor = 0
				if(i == 1):
					start = 0	#marca a amosta onde ocorreu o evento			
			else:	#momento em que a energia do sinal é menor que o limiar inferior de energia	
				if(energia_menor == 0):
	 				start = i	#marca a amosta onde ocorreu o evento
					start = (start*step)+win
				energia_menor += 1
				if (energia_menor == amostras_consecutivas):	#interrompe a verificação quando a energia é muito baixa
					break
		
		#verificação do limiar inferior de energia para achar stop
		energia_menor = 0
		for i in range(iMax, len(energy)):	#varre o sinal do start até o final do sinal (50 quadros)
			if (energy[i] >= lim_inferior):	
				energia_menor = 0
				if(i == len(energy)-1):
					stop = len(energy)	#marca a amosta onde ocorreu o evento
			else:	#momento em que a energia do sinal é menor que o limiar inferior de energia
				if (energia_menor == 0):
					stop = len(energy)	#marca a amosta onde ocorreu o evento
				if (energia_menor == 3):
					stop = i	#marca a amosta onde ocorreu o evento
				energia_menor += 1
				if (energia_menor == amostras_consecutivas):	#interrompe a verificação quando a energia é muito baixa
					energia_menor = 0		
					break 

		stop = (stop*step)+win
		
		y = np.zeros(len(x))
		for i in range(start, stop):
			y[i] = x[i]
		

		z = np.zeros(stop-start)
	
		for i in range(0,len(z)):
			z[i] = y[i+start]

		## tratamento do sinal pos segmentacao
		## normalizacao de cada uma das amostras, deixando-as sempre com o valor entre -1 e 1
		## e deixando suas componentes sempre proporcionais a isso
		z_norm = z / np.max(np.abs(z))
		############
		## extracao de caracteristicas de cada sinal
		## aqui o sinal passa pelo algoritmo da MFFC, que faz o sinal passar por 13 filtros da escala MEL 
		## que extrai caracteristicas desse sinal
		## o sinal foi dividido chunks (10) pedacos do mesmo tamanho e cada um desses pedacos passram pela MFCC
		## eu dou como entrada o sinal normalizado e extraio as 13 caracteristicas de cada uma das partes
		## sendo que no fim, na verdade, cada sinal tera 130 caracteristicas que o definem como sinal
			
		chunks = 10
		tempo_total = (float)(len(z_norm))/fs
	
#		mfcc_feat = mfcc(z_norm,fs,winlen=tempo_total/chunks,winstep=tempo_total/#chunks,numcep=13,nfilt=40,nfft=16384,lowfreq=100,preemph=0,appendEnergy=True)
		mfcc_feat = mfcc(z_norm,fs,winlen=tempo_total/chunks,winstep=tempo_total/chunks,numcep=13,nfilt=26,nfft=16384,lowfreq=50,preemph=0,appendEnergy=True,winfunc=np.hamming)	

		for i in range(0, chunks):
			for j in range(0,13):					
				sys.stdout.write(str(mfcc_feat[i][j]))
				sys.stdout.write(';')

		if(comando == 0):
			sys.stdout.write('1;0;0;0;0;0;0;0;0;0;')
		if(comando == 1):
			sys.stdout.write('0;1;0;0;0;0;0;0;0;0;')
		if(comando == 2):
			sys.stdout.write('0;0;1;0;0;0;0;0;0;0;')
		if(comando == 3):
			sys.stdout.write('0;0;0;1;0;0;0;0;0;0;')
		if(comando == 4):
			sys.stdout.write('0;0;0;0;1;0;0;0;0;0;')
		if(comando == 5):
			sys.stdout.write('0;0;0;0;0;1;0;0;0;0;')
		if(comando == 6):
			sys.stdout.write('0;0;0;0;0;0;1;0;0;0;')
		if(comando == 7):
			sys.stdout.write('0;0;0;0;0;0;0;1;0;0;')
		if(comando == 8):
			sys.stdout.write('0;0;0;0;0;0;0;0;1;0;')
		if(comando == 9):
			sys.stdout.write('0;0;0;0;0;0;0;0;0;1;')
	
		print('')	




