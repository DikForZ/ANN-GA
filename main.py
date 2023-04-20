import numpy as np
import pandas as pd
import json


with open('layerStruct.json', mode = 'r') as file:
    layerStruct = json.load(file)
trainData = pd.read_csv('trainData.csv')
"""
fenol = trainData['Fenol'].tolist()
flavonoid = trainData['Flavonoid'].tolist()
neuralNetworkInput = list(map(lambda a, b : [a, b], fenol, flavonoid))
print(neuralNetworkInput)

def activationFunc(x):
    return 1 / (1 + np.exp(-x))

def feedForward():


Test = list(map(activationFunc, fenol))
print(Test)
"""