from random import randrange as rand
from copy import deepcopy as cpy

C = [0,1,-1]
def clock(n):
    return C[n+1]

# Will need to be adjusted for varying inputsPerNode
def superNate(gfList, sel):
    return gfList[ sel[0][0]+1 ][ sel[1][0]+1 ][ sel[2][0]+1 ][0]

def brainCycle(n, nodes,nodeOutputsBuffer):
    for i in range(n):
        nodeOutputsBuffer[i+2][0] = superNate(nodes[i][0],nodes[i][1])
    nodeOutputsBuffer[0][0] = clock(nodeOutputsBuffer[0][0])
    return cpy(nodeOutputsBuffer)

### setFunctionIndex ###
def setFI(r,ipn):
    if ipn == 1:
        return [rand(r),rand(r),rand(r)]
    return [setFI(r,ipn-1),setFI(r,ipn-1),setFI(r,ipn-1)]

### setFunctionPointers ###
def setFP(ipn, no, fi):
    if ipn == 1:
        return [no[fi[0]],no[fi[1]],no[fi[2]]]
    return [setFP(ipn-1,no,fi[0]),
            setFP(ipn-1,no,fi[1]),
            setFP(ipn-1,no,fi[2])]

def cpyVals(oL,no,arr):
    for i in range(oL):
        no[i][0] = arr[i][0]
    return

class brain:
    def __init__(self, numberOfNodes):
        n = numberOfNodes
        n2 = n+2
        self.ipn = 3

        self.startState = []
        self.startState.append([-1])
        for i in range(1,n2):
            self.startState.append([rand(3) - 1])
        self.nodeOutputsBuffer = cpy(self.startState)
        self.nodeOutputs = cpy(self.startState)
        self.finalOutputNode = rand(n) + 2
        
        self.nodes = []
        self.nodesFunctionIndex = []
        self.nodesInputIndex = []
        for i in range(n):
            self.nodes.append([])
            self.nodes[i] = [[],[]]
            self.nodesFunctionIndex.append([])
            self.nodesFunctionIndex[i] = setFI(n2,self.ipn)
            self.nodes[i][0] = setFP(self.ipn,
                                     self.nodeOutputs,
                                     self.nodesFunctionIndex[i])
            self.nodesInputIndex.append([])
            for j in range(self.ipn):
                ni = rand(n2)
                self.nodesInputIndex[i].append(ni)
                self.nodes[i][1].append(self.nodeOutputs[ni])

    def compute(self, inList, outputLen):
        self.nodeOutputsBuffer = cpy(self.startState)
        self.nodeOutputs = cpy(self.startState)
        self.refreshFunctionPointers()
        self.refreshInputPointers()
        nodeLen = len(self.nodes)
        n2 = nodeLen+2
        for i in inList:
            self.nodeOutputs[1][0] = i
            arr = brainCycle(nodeLen, self.nodes, self.nodeOutputsBuffer)
            cpyVals(n2,self.nodeOutputs,arr)
            
        self.nodeOutputs[1][0] = 0
        for i in range(nodeLen):
            arr = brainCycle(nodeLen, self.nodes, self.nodeOutputsBuffer)
            cpyVals(n2,self.nodeOutputs,arr)
            
        output = []
        for i in range(outputLen):
            arr = brainCycle(nodeLen, self.nodes, self.nodeOutputsBuffer)
            cpyVals(n2,self.nodeOutputs,arr)
            output.append(self.nodeOutputs[self.finalOutputNode][0])
        return cpy(output)

    def getStartStateData(self):
        return self.startState

    def setStartStateData(self, ssdArr):
        self.startState = cpy(ssdArr)

    def getNodeFunctionIndex(self, indexOfNode):
        return self.nodesFunctionIndex[indexOfNode]

    def setNodeFunctionIndex(self, i, fi):
        self.nodesFunctionIndex[i] = cpy(fi)

    def refreshFunctionPointers(self):
        n = len(self.nodes)
        for i in range(n):
            self.nodes[i][0] = setFP(self.ipn,
                                     self.nodeOutputs,
                                     self.nodesFunctionIndex[i])

    def getNodeInputIndex(self,indexOfNode):
        return self.nodesInputIndex[indexOfNode]

    def setNodeInputIndex(self, i, ii):
        self.nodesInputIndex[i] = cpy(ii)

    def refreshInputPointers(self):
        n = len(self.nodes)
        for i in range(n):
            for j in range(self.ipn):
                ni = self.nodesInputIndex[i][j]
                self.nodes[i][1][j] = self.nodeOutputs[ni]

    def getNodeData(self, indexOfNode):
        return self.nodes[indexOfNode]

    #Can't use this function. Only references are used for node data
    def setNodeData(self, i, nd):
        self.nodes[i] = cpy(nd)

    def getFinalOutputNode(self):
        return self.finalOutputNode

    def setFinalOutputNode(self, index):
        self.finalOutputNode = index

def getBrains(numOfBrains, numOfNodes):
    bList = []
    for i in range(numOfBrains):
        bList.append(brain(numOfNodes))
    return cpy(bList)
