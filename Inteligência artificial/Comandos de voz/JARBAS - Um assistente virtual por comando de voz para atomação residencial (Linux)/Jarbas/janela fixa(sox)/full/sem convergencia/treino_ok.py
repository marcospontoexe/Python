from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure.modules import SigmoidLayer
from pybrain.structure.modules import TanhLayer
from pybrain.structure.modules import BiasUnit
from pybrain.tools.customxml import NetworkWriter
from pybrain.tools.customxml import NetworkReader
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

#rede = buildNetwork(nInputs, hidden_layers, nOutputs, bias=True, hiddenclass=TanhLayer, outclass=SoftmaxLayer)
rede = buildNetwork(nInputs, hidden_layers, nOutputs, bias=True, outclass=SoftmaxLayer)
base = SupervisedDataSet(nInputs, nOutputs)

for i in range(len(X_train)):
	base.addSample(X_train_norm[i],y_train[i])

treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.005, momentum = 0.06, batchlearning=False)
#treinamento.trainUntilConvergence(maxEpochs=250, verbose=None, continueEpochs=30, validationProportion=0.25)
epocas = 200
learning_rate = np.zeros(epocas)
for i in range(1, epocas):
    erro = treinamento.train()
    learning_rate[i-1] = erro
   #if i % 50 == 0:
    print("Erro "+str(i)+": %s" % erro)
      
print('matriz confusao de treino :')
matrizConfusao = np.zeros((10,10))
for i in range(len(X_train)):
	y_certo = np.argmax(y_train[i])
	y_predito = np.argmax(rede.activate(X_train_norm[i]))
	#print(y_certo)
	#print(y_predito)
	#print('---')
	matrizConfusao[y_certo][y_predito] += 1
print(matrizConfusao)

plt.plot(learning_rate)
plt.show()

#class pybrain.tools.neuralnets.saveNetwork('teste.csv')
NetworkWriter.writeToFile(rede, 'model.xml')
#https://stackoverflow.com/questions/12050460/neural-network-training-with-pybrain-wont-converge


