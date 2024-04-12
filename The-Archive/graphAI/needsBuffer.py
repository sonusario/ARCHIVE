from random import random, randrange
from time import time

def n121():
    return random() - randrange(2)

class node():
    def __init__(self, actFuncs):
        self.val = None
        actHyp = n121()
        afCode = randrange(len(actFuncs))
        self.activationFunction = actFuncs[afCode](actHyp)
        self.derivativeFunction = devFuncs[afCode](actHyp)
        self.outgoingConnections = []
    def connect(self, nodeArray):
        self.incommingNodes = []
        self.weights = []
        lenNA = len(nodeArray)
        for i in range(randrange(lenNA)):
            randNodeCode = randrange(lenNA)
            self.incommingNodes.append(nodeArray[randNodeCode])
            self.weights = n121()
            nodeArray[randNodeCode].outgoingConnections.append(self)
        self.incommingCount = len(self.incommingNodes)
    def itrt(self):
        total = 0
        for i in range(self.incommingCount):
            if self.incommingNodes[i].val == "End":
                self.val = "End"
                return
            elif self.incommingNodes[i].val == None:
                continue
            total += self.incommingNodes[i].val * self.weights[i]
        self.val = activationFunction(total)

#rrelu, elu
actFuncs = [lambda a: lambda x: (a * x) if (x < 0) else (x),
            lambda a: lambda x: (a * ((e**x) - 1)) if (x <= 0) else (x)]

devFuncs = [lambda a: lambda x: (a) if (x < 0) else (1),
            lambda a: lambda x: ((a * ((e**x) -1)) + a) if (x <= 0) else (1)]
