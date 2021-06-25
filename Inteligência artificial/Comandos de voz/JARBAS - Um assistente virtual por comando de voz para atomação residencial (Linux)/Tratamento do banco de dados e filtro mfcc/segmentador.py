import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import os


pasta = '../../Banco_de_palavras'
for comando in range(10):
	if (comando == 0):
		comando_aux = f'{pasta}/10-Jarbas'
	if (comando == 1):
		comando_aux = f"{pasta}/11-Ligue"
	if (comando == 2):
		comando_aux = f"{pasta}/12-Desligue"
	if (comando == 3):
		comando_aux = f"{pasta}/13-Música"
	if (comando == 4):
		comando_aux = f"{pasta}/14-Sala"
	if (comando == 5):
		comando_aux = f"{pasta}/15-Quarto"
	if (comando == 6):
		comando_aux = f"{pasta}/16-Cozinha"
	if (comando == 7):
		comando_aux = f"{pasta}/17-Ar-Condicionado"
	if (comando == 8):
		comando_aux = f"{pasta}/18-TV"
	if (comando == 9):
		comando_aux = f"{pasta}/19-Café"

	for speaker in range(1, 3):		#número de amostras de áudio contida em cada pasta de comando (Ligue, Desligue, Jarbas...)
		audio = f'{comando_aux}/{speaker}.wav'
		[fs,xi] = wav.read(audio)
		#normalização do amplitude de 15 bits. Isso deixa a amplitude entre um intervalo de 1 e -1
		xi = xi / 32768.0
		#Muitos microprocessadores causam um estalo no início da gravação, atingindo a máxima amplitude
		estalo = 100
		xi[0:estalo] = 0   #zera as primeiras 100 amostras do audio

		x = []
		x = np.append(xi[0], xi[1:] - 0.97 * xi[:-1])   #filtro de pre-enfase

		#n = np.arange(0, len(x))

		print('speaker: '+ str(speaker))

		win = 3200
		step = 800	
		#Calcula a energia contida no vetor x 
		energy = np.zeros(int((len(x)-win)/step))	#define o tamanho do vetor energia
		for i in range(len(energy)):
			tmp = 0
			for j in range(i*step, i*step+win):		#calcula a energia dentro da janela definida
				tmp = tmp + x[j]*x[j]				#somatório das amostras ao quadrado, dentro de cada janela
			energy[i] = tmp							#vetor com a energia de cada janela 

		iMax = np.argmax(energy)	#indice  onde foi encontrado o maior valor da amostra energy
		vMax = energy[iMax]			#o maior valor da amostra energy


		#calcula o limiar inferior de energia
		A = 0.01
		lim_inferior = A*vMax

		#a variável silencio verefica se a veriável energy é menor que o lim_inferior 
		silencio = 0
		#para garantir que os vales contidos na regiao falada nao sejam considerados como regiao de silêncio, 
		#foi criado a variável amostras_consecutivas
		amostras_consecutivas = 10
		#verificação do limiar inferior de energia para achar start
		for i in range(iMax, 0, -1):			#varre o sinal do pico de energia até o inicio do sinal
			if(energy[i] >= lim_inferior):	
				if(i == 1):
					start = 0
			else:	#momento em que a energia do quadro analisado é menor que o limiar inferior de energia	
				if(silencio == 0):
					start = i		#marca a amosta onde energy é menor que lim_inferior
				silencio += 1		
				if(silencio == amostras_consecutivas):	# quando ha 10 quadros do áudio pertecentes a região de silencio
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

		som = f'aplay {audio}'
		os.system(som)

		print('indice da energia maxima: '+ str(iMax))
		print('start: '+str(start))
		print('stop: '+str(stop))
		print('limiar inferior de energia: '+str(lim_inferior))
		print('ENERGIA MÁXIMA: '+ str(vMax))
		print('\n')



	#imprime os gŕaficos do vetor de energia, além do audio original, áudio apenas com a regiaão falada, e finalmente o audio segmentado
		plt.subplot(5,1,1)
		plt.plot(energy)
		plt.subplot(5,1,2)
		plt.plot(x)
		plt.subplot(5,1,3)
		plt.plot(y)
		plt.subplot(5,1,4)
		plt.plot(z)
		plt.show()
				


