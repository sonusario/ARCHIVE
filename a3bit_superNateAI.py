from random import randrange
import time

def printResults(arr, total):
    d = len(arr)
    print("================")
    for i in range(d):
        print(i, ":", arr[i], "gates")
    print("----------------")
    print("Total  :", total)

def getTotals(arr):
    d = len(arr)
    total = 0
    for i in range(d):
        total += arr[i]
    return total

def gateIdentifier(arr):
    d = len(arr)
    total = 0
    for i in range(d):
        total += (2**(d-i-1)) * arr[i]
    return total

def gateCounter(arr, inLen):
    gfNumCombos = len(arr)
    numOfFunctions = 2**(2**inLen)
    gateCounts = []
    gateLocals = []
    for i in range(numOfFunctions):
        gateCounts.append(0)
        gateLocals.append([])

    for i  in range(gfNumCombos):
        gate = gateIdentifier(arr[i])
        gateCounts[gate] += 1;
        gateLocals[gate].append(i)
    
    printResults(gateCounts, gfNumCombos)
######################
def compare(expectedOutput, brainOutput):
    exOutLen = len(expectedOutput)
    score = 0
    perfect = True
    for i in range(exOutLen):
        if expectedOutput[i] == brainOutput[i]:
            score += 1
        else:
            perfect = False
    if perfect:
        return score * 2
    return score

############################################
def binToDec(arr):
    arrLen = len(arr)
    maxNum = (2**arrLen) / 2
    total = 0
    for i in arr:
        total += i * maxNum
        maxNum /= 2
    return int(total)

def superNate(gfList, inList):
    return gfList[binToDec(inList)]
############################################

def brainCycle(nodeLen, nodes, nodeOutputs, nodeOutputsBuffer):
    for j in range(nodeLen):
        nodeFunction = []
        nodeInputs = []
        for k in nodes[j][0]:
            nodeFunction.append(nodeOutputs[k])
        for k in nodes[j][1]:
            nodeInputs.append(nodeOutputs[k])
        nodeOutputsBuffer[j+2] = superNate(nodeFunction, nodeInputs)
    nodeOutputsBuffer[0] = int(not nodeOutputsBuffer[0])
    return list(nodeOutputsBuffer)

class brain:
    def __init__(self, n):
        self.nodes = []
        for i in range(n):
            self.nodes.append([])#Make n nodes
        for i in range(n):
            self.nodes[i].append([])#Add function array to node i
            self.nodes[i].append([])#Add input array to node i
            for j in range(8):#Add 8 func selectors to the func array of node i
                self.nodes[i][0].append(randrange(n+2))
            for j in range(3):#Add 3 input selector to the input array of node i
                self.nodes[i][1].append(randrange(n+2))
        self.nodeOutputsBuffer = []
        for i in range(n+2):#n+2 means n nodes + clock + input
            self.nodeOutputsBuffer.append(randrange(2))
        self.nodeOutputsBuffer[0] = 0
        self.startState = list(self.nodeOutputsBuffer)#Having a start state is crucial as it prevents excesive 'Zero' functions
        self.finalOutputNode = randrange(n) + 2#Node to be used to collect output

    def compute(self, inList, outputLen):
        self.nodeOutputs = list(self.startState)
        nodeLen = len(self.nodes)
        for i in inList:
            self.nodeOutputs[1] = i
            self.nodeOutputs = brainCycle(nodeLen,
                                          self.nodes,
                                          self.nodeOutputs,
                                          self.nodeOutputsBuffer)
        self.nodeOutputs[1] = 0
        for i in range(nodeLen):
            self.nodeOutputs = brainCycle(nodeLen,
                                          self.nodes,
                                          self.nodeOutputs,
                                          self.nodeOutputsBuffer)
        output = []
        for i in range(outputLen):
            self.nodeOutputs = brainCycle(nodeLen,
                                          self.nodes,
                                          self.nodeOutputs,
                                          self.nodeOutputsBuffer)
            output.append(self.nodeOutputs[self.finalOutputNode])

        return list(output)
###########
def runTest():
    b = brain(12)
    out = b.compute([1,0,1,0], 4)
    #print(b.nodes)
    return out

def timeTest():
    print("==========================================")
    print("Super Nate started")
    startTime = time.time()

    x = []
    for i in range(1000):
        x.append(runTest())

    gateCounter(x, 2)

    endTime = time.time()
    elapsedTime = endTime - startTime
    print("COMPLETED")
    print("Elapsed time:", elapsedTime)
    print("==========================================")

#timeTest()
'' '''
for i in range(100):
    b = brain(12)
    x = 0
    for j in range(10):
        out = b.compute([1,0,1,0], 4)
        out2 = b.compute([1,0,1,0], 4)
        if out == out2:
            x += 1
    print(x)
''' ''' '''
