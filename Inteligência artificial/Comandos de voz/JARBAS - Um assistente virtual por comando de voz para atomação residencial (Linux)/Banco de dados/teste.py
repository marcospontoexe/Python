
import numpy as np
import os

speaker = input('Digite o nome do speaker: ')

comandos = ['ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','JARBAS','LIGUE','DESLIGUE','MUSICA','SALA','QUARTO','COZINHA',' AR-CONDICIONADO','TV','CAFE']
repetitions = 3

for icomando in range(0, len(comandos)):
	for repeats in range (0, repetitions):
		print('')
		print('DIGA ' + str(comandos[icomando]) + '...')
		print(' ') 
		cmd = 'arecord -D hw:audiocodec,0 -f dat -d 2 -c 1 -r 16000 ' + str(speaker) + str('-') + str(icomando) + str('-') + str(repeats) + str('.wav')
		os.system(cmd)