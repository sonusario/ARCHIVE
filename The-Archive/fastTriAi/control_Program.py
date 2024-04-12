from random import randrange as rand
from copy import deepcopy as cpy
import brain as br
import doctor as dr
import ioGenerator as io
import math
import time

def printNode(node, numOfNodes, inData, outData):
    print('\n' * 3)
    #print('inData =', inData)
    #print('outData =', outData)
    print('b = br.brain(', numOfNodes, ')')
    print('b.setStartStateData(', node.getStartStateData(), ')')
    for i in range(numOfNodes):
        print('b.setNodeFunctionIndex(',i,',', node.getNodeFunctionIndex(i),')')
        print('b.setNodeInputIndex(',i,',', node.getNodeInputIndex(i),')')
        #print('b.setNodeData(', i, ',', node.getNodeData(i), ')')
    print('b.setFinalOutputNode(', node.getFinalOutputNode(), ')')
    #print(input('<<< '))
    

def runControlProgram():
    inData, outData = io.inOutArrs(2)
    #inData, outData = io.inOutArrs2()
    
    inData = [[-1,0],[0,0],[1,0]]
    outData = [[0,1],[0,-1],[0,0]]

    numOfNodes = 12
    popSize = 150
    muRate = 0.15
    percentRandPop = 0.80
    printFreq = 15#popSize

    print('#' * 33)
    startTime = time.time()

    bs = dr.brainSurgeon(numOfNodes, popSize, muRate, percentRandPop)
    pop,scores,winner = bs.findFittest(inData, outData, printFreq)

    x = cpy(winner)
    
    print(list(range(numOfNodes + 2)), '<- Index')
    print(x.getStartStateData(), '<- Starting State')
    for i in range(numOfNodes):
        print(x.getNodeData(i), '<- Node', i, 'Data')
    print(x.getFinalOutputNode(), '<- Output Node')
    elapsedTime = time.time() - startTime
    print('Runtime:', elapsedTime)
    print('#' * 33)
    

    #printNode(w, numOfNodes, inData, outData)
    printNode(x, numOfNodes, inData, outData)
    #printNode(y, numOfNodes, inData, outData)

runControlProgram()
