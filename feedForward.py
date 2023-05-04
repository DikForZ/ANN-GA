import pandas as pd
import numpy as np
import json

def readJson(myFile):
    with open(myFile, mode = 'r') as file:
        return json.load(file)

def activationFunction(x):
    return 1 / (1 + np.exp(-x))

data = pd.read_csv('trainData.csv')
layerStruct = readJson('layerStruct.json')
fenol = data['Fenol'].tolist()
flavonoid = data['Flavonoid'].tolist()
myInput = list(map(lambda a, b: [a, b], fenol, flavonoid))
print(myInput)
myInnn = list(map(activationFunction, fenol))
print(myInnn)