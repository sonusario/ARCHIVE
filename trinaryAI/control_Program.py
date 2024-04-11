from random import randrange
import math
import time
import TrinaryAI as nate#*#
import geneticBrain as gb
import ioGenerator as io

def printNode(node, numOfNodes, inData, outData):
    print('\n' * 3)
    print('inData =', inData)
    print('outData =', outData)
    print('b = nate.brain(', numOfNodes, ')')
    print('b.setStartStateData(', node.getStartStateData(), ')')
    for i in range(numOfNodes):
        print('b.setNodeData(', i, ',', node.getNodeData(i), ')')
    print('b.setFinalOutputNode(', node.getFinalOutputNode(), ')')
    #print(input('<<< '))
    
def runControlProgram():
    inData, outData = io.inOutArrs(1)

    inData = [[-1,0],[0,0],[1,0]]
    outData = [[0,1],[0,-1],[0,0]]
    #inData = [[0,0],[0,1],[1,0],[1,1]]
    #inData = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
    #outData = [[-1,1],[0,-1],[0,0],[0,-1],[0,0],[0,1],[0,0],[0,1],[1,-1]]
    #outData = [[0,0,0,1],[1,1,1,0],[0,1,1,1],[1,0,0,0]]
    #outData = [[0,1,0],[1,0,1],[0,0,0],[1,1,1]]
    #outData = [[0,1],[1,0],[1,1],[0,0]]
    #outData = [[1],[0],[0],[1]]
    #outData = [[0],[1],[1],[0]]

    numOfNodes = 12
    popSize = 150
    muRate = 0.15
    percentRandPop = 0.80 #70 seconds at 80%(g475), 120 at 90%(g786), 280 at 50% & 100%(g1810 & g1935)
    printFreq = 15#popSize

    print('#' * 33)
    startTime = time.time()
    bs = gb.brainSurgeon(numOfNodes, popSize, muRate, percentRandPop)
    pop,scores = bs.findFittest(inData, outData, printFreq)

    wIndex = scores.index(max(scores)) 

    #w = pop[wIndex-1]
    x = pop[wIndex]
    #y = pop[wIndex+1]

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
