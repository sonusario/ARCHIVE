import random

def nand(a, b):
    return not(a and b)

def gateNet(numOfGates):
    gatePool = []
    for i in range(numOfGates):
        gatePool[i] = i

    
    aInputs = []
    bInputs = []
    outputs = []
