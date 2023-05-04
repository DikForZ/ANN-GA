import random as rd
import json

def readJson(myFile = 'layerStruct.json'):
    with open(myFile, mode = 'r') as file:
        return json.load(file)

def initialize():
    layerStruct = readJson()
    networkStruct = [layerStruct['Input']]
    for i in range(layerStruct['hiddenLayer']):
        networkStruct.append(layerStruct['nodes' + str(i + 1)])
    networkStruct.append(layerStruct['Output'])
    return networkStruct

def weightGenerator():
    networkStruct = initialize()
    weights = {}
    for i in range(len(networkStruct) - 1):
        myWeights =  {'weights_' + str( i + 1): [rd.random() for i in range(networkStruct[i] * networkStruct[i + 1])]}
        weights.update(myWeights)
    weightsJson = json.dumps(weights)
    with open('weight.json', mode = 'w') as file:
        file.write(weightsJson)

def transfer_derivative(output):
	return output * (1.0 - output)



weightGenerator()