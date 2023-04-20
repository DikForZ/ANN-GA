import json


def layerCalc():
    while True:
        try:
            numberOfHiddenLayer = int(input('Enter amount of hidden layer... '))
            break
        except ValueError:
            print("Please Enter a Number !")
    layerStruct = {
                "hiddenLayer" : numberOfHiddenLayer,
                "totalLayer" : numberOfHiddenLayer + 2
            }
    json_layerStruct = json.dumps(layerStruct)
    with open('layerStruct.json', mode = 'w') as file:
        file.write(json_layerStruct)

def featureCalc():
    with open('layerStruct.json', mode = 'r') as file:
        layerStruct = json.load(file)
    feature = ('Input', 'Output')
    for i in range(int(len(feature))):
        while True:
            try:
                numberOfFeature = int(input('Enter amount of ' + feature[i] +'... '))
                break
            except ValueError:
                print('Plaase Enter a Number!')
        layerStruct.update({
            feature[i] : numberOfFeature
        })
    json_layerStruct = json.dumps(layerStruct)
    with open('layerStruct.json', mode = 'w') as file:
        file.write(json_layerStruct)

def nodesCalc():
    with open('layerStruct.json', mode = 'r') as file:
        layerStruct = json.load(file)
    for i in range(layerStruct['hiddenLayer']):
        while True:
            try:
                hiddenLayerAmount = int(input('Enter amount of nodes in layer ' + str(i + 1) + '... '))
                break
            except ValueError:
                print('Please Enter a Number !')
        layerStruct.update({
            'nodes' + str(i + 1) : hiddenLayerAmount
        })
    json_layerStruct = json.dumps(layerStruct)
    with open('layerStruct.json', mode = 'w') as file:
        file.write(json_layerStruct)