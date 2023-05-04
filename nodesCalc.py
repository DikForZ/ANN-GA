import json

def integerInput(message):
    while True:
        try:
            var = int(input(message))
            break
        except ValueError:
            print('Only receive integer!')
    return var

def readJson(myFile = 'layerStruct.json'):
    with open(myFile, mode = 'r') as file:
        return json.load(file)

def writeJson(rawFile, myFile = 'layerStruct.json'):
    jsonFile = json.dumps(rawFile)
    with open(myFile, mode = 'w') as file:
        file.write(jsonFile)

def layerCalc():
    numberOfHiddenLayer = integerInput('Enter amount of hidden layer... ')
    layerStruct = {
                "hiddenLayer" : numberOfHiddenLayer,
                "totalLayer" : numberOfHiddenLayer + 2
            }
    writeJson(layerStruct)

def featureCalc():
    layerStruct = readJson()
    feature = ('Input', 'Output')
    for i in range(int(len(feature))):
        numberOfFeature = integerInput('Enter amount of ' + feature[i] +'... ')
        layerStruct.update({
            feature[i] : numberOfFeature
        })
    writeJson(layerStruct)

def nodesCalc():
    layerStruct = readJson()
    for i in range(layerStruct['hiddenLayer']):
        hiddenLayerAmount = integerInput('Enter amount of nodes in layer ' + str(i + 1) + '... ')
        layerStruct.update({
            'nodes' + str(i + 1) : hiddenLayerAmount
        })
    writeJson(layerStruct)

layerCalc()
featureCalc()
nodesCalc()