# -*- coding: utf-8 -*-
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
import numpy as np
import scipy.io.wavfile as wav
import sys
import os
#from python_speech_features import mfcc
#from python_speech_features import delta
#from python_speech_features import logfbank



for speaker in range(1, 123):
	comando = f"{str(speaker)}.wav"
	[fs,xi] = wav.read(comando)
	xi = xi / 32768.0
	estalo = 100
	xi[0:estalo] = 0   #zera as primeiras amostras do audio

	x = []
	x = np.append(xi[0], xi[1:] - 0.97 * xi[:-1])   #filtro de pre-enfase

	n = np.arange(0, len(x))

	print('speaker: '+ str(speaker))

	win = 3200
	step = 800 
	print(f"win: {type(win)}")
	print(f"step: {type(step)}")
	print(f"x: {type(x)}")
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
	A = 0.1
	lim_inferior = A*vMax

	#verificação do limiar inferior de energia para achar start
	energia_menor = 0
	amostras_consecutivas = 10
	for i in range(iMax, 0, -1):	#varre o sinal do pico de energia até o inicio do sinal
		if(energy[i] >= lim_inferior):	
			energia_menor = 0
			if(i == 1):
				start = 0	#marca a amosta onde ocorreu o evento
				print('start energia_2 :'+str(start))
		else:	#momento em que a energia do sinal é menor que o limiar inferior de energia	
			if(energia_menor == 0):
 				start = i		#marca a amosta onde ocorreu o evento
				#print(f"start energia_1: {start}")
			energia_menor += 1
			if(energia_menor == amostras_consecutivas):	#interrompe a verificação quando a energia é muito baixa
				break
	if(iMax == 0):
		start = 1


	if(start == 0):	
		start = 0
	else: 
		start = (start*step)+win
	stop = start+17600
	if (stop >32000):
		stop = 32000

	
	y = np.zeros(len(x))
	for i in range(start, stop):
		y[i] = x[i]
		

	z = np.zeros(stop-start)
	
	for i in range(0,len(z)):
		z[i] = y[i+start]

	som = "aplay "+str(comando)
	os.system(som)

	print('indice da energia maxima: '+ str(iMax))
	print('start: '+str(start))
	print('stop: '+str(stop))
	print('média de ZC: '+str(zc_med))
	print('limiar inferior de energia: '+str(lim_inferior))
	print('limiar do zc: '+str(lim_zc))
	print('ENERGIA MÁXIMA: '+ str(vMax))
	print('\n')

'''
	plt.subplot(5,1,1)
	plt.plot(energy)
	plt.subplot(5,1,2)
	plt.plot(taxa_zc)
	plt.subplot(5,1,3)
	plt.plot(x)
	plt.subplot(5,1,4)
	plt.plot(y)
	plt.subplot(5,1,5)
	plt.plot(z)
	plt.show()
			
'''	


'''
	print('start: '+str(start))
	print('stop: '+str(stop))

	for i in range(len(energy)):
		print('energia no quadro ' + str(i) + ':' + str(energy[i]))

	for i in range(len(taxa_zc)):
		print('cruzamento por zero no quadro ' + str(i) + ':' + str(taxa_zc[i]))

	vmaxi = float(z.max())
	vmin = float(z.min())
	z_norm = np.zeros(len(z))
	for i in range(0, len(z)):
		z_norm[i] = (2*((z[i]-vmin)/(vmaxi-vmin)))-1

'''


