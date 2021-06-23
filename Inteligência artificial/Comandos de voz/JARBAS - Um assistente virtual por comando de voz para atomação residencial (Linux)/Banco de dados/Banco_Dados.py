import numpy as np
import os

speaker = input("Digite o nome do voluntário: ")
comandos = ["JARBAS", "LIGUE", "DESLIGUE", "MÚSICA", "SALA", "QUARTO", "COZINHA", "AR-CONDICIONADO", "TV", "CAFE"]
repeticoes = 3

for i in range(0, len(comandos)):
    for rodada in range (0, repeticoes):    #grava os comandos têrs vezes
        print(f"\nDIGA {comandos[i]}...\n")
        os.system(f"arecord -D hw:0,0 -f dat -d 2 -c 2 -r 16000 {speaker}-{comandos[i]}-{rodada}.wav")
