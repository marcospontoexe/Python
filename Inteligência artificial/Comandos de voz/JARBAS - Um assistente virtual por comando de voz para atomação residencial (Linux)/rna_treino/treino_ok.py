
from pybrain3.tools.shortcuts import buildNetwork  
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer
from pybrain3.structure.modules import SoftmaxLayer
from pybrain3.structure.modules import SigmoidLayer
from pybrain3.structure.modules import TanhLayer
from pybrain3.structure.modules import BiasUnit
from pybrain.tools.customxml import NetworkWriter	#necessário pybrain v0.3.3

#import pybrain3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

seed = 143
np.random.seed(seed)

nInputs = 130
hidden_layers = 36
nOutputs = 10
#importacao dos dados para aprendizado
df = pd.read_csv('treino.csv', header=None, sep=';')
X_train = df.iloc[:, 0:nInputs].values
y_train = df.iloc[:, nInputs:(nInputs+nOutputs)].values

#normalizacao do csv de treino
X_train_norm = X_train/np.max(np.abs(X_train))

# Construcao da rede neural
#rede = buildNetwork(nInputs, hidden_layers, nOutputs, bias=True, hiddenclass=TanhLayer, outclass=SoftmaxLayer)
rede = buildNetwork(nInputs, hidden_layers, nOutputs, bias=True, outclass=SoftmaxLayer)
base = SupervisedDataSet(nInputs, nOutputs)

# insere os dados na rede neuraloftmax
for i in range(len(X_train)):
	base.addSample(X_train_norm[i],y_train[i])

# treinamento da rede neural pelo metodo back propagation
treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.04, momentum = 0.01, batchlearning=False)
#treinamento.trainUntilConvergence(maxEpochs=250, verbose=None, continueEpochs=30, validationProportion=0.25)
epocas = 80

learning_rate = np.zeros(epocas)
for i in range(1, epocas):
    erro = treinamento.train()
    learning_rate[i-1] = erro
   #if i % 50 == 0:
    print("Erro "+str(i)+": %s" % erro)
      
# imprime a matriz confusao de treinamento
print('matriz confusao de treino: ')
matrizConfusao = np.zeros((10,10))
for i in range(len(X_train)):
	y_certo = np.argmax(y_train[i])
	y_predito = np.argmax(rede.activate(X_train_norm[i]))
	#print(y_certo)
	#print(y_predito)
	#print('---')
	matrizConfusao[y_certo][y_predito] += 1
print(matrizConfusao)

# importacao dos dados CSV para o aprendizado
df2 = pd.read_csv('teste.csv', header=None, sep=';')
X_train2 = df2.iloc[:, 0:nInputs].values
y_train2 = df2.iloc[:, nInputs:(nInputs+nOutputs)].values

#normalizacao do csv de teste
X_teste_norm = X_train2/np.max(np.abs(X_train2))

# imprime a matriz confusao de teste
print('matriz confusao de teste :')
matrizConfusao2 = np.zeros((10,10))
y_certo2 = 0
y_predito2 = 0
for i in range(len(X_train2)):
	y_certo2 = np.argmax(y_train2[i])
	y_predito2 = np.argmax(rede.activate(X_teste_norm[i]))
	#print(y_certo)
	#print(y_predito)
	#print('---')
	matrizConfusao2[y_certo2][y_predito2] += 1
print(matrizConfusao2)

#mostra a curva da taxa de aprendizagem
plt.plot(learning_rate)
plt.show()

# gera um arquivo XML
#class pybrain.tools.neuralnets.saveNetwork('teste.csv')
NetworkWriter.writeToFile(rede, 'model.xml')
#https://stackoverflow.com/questions/12050460/neural-network-training-with-pybrain-wont-converge

'''
for i in range(1, 60):
    erro = treinamento.train()
    if i % 50 == 0:
        print("Erro: %s" % erro)
0,01 taxa
36 hidden
'''

