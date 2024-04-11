from random import randrange

def rTriCycle(arr):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] < 2:
            arr[d] += 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1

    return list(arr)

def triToDec(arr):
    arrLen = len(arr)
    maxNum = (3**arrLen) / 3#*#
    total = 0
    for i in arr:
        total += i * maxNum
        maxNum /= 3#*#
    return int(total)

def superNate(gfList, inList):
    #return gfList[triToDec(inList) + 13]#Add 13 to match non-negative index
    i = inList[0] + 1
    j = inList[1] + 1
    k = inList[2] + 1
    return gfList[i][j][k]

def brainCycle(nodeLen, nodes, nodeOutputs, nodeOutputsBuffer):
    for j in range(nodeLen):
        nodeFunction = [[[],[],[]],[[],[],[]],[[],[],[]]]
        nodeInputs = []
        x = [0,0,0]
        for k in range(27):#
            nodeFunction[x[0]][x[1]].append(nodeOutputs[nodes[j][0][x[0]][x[1]][x[2]]])
            x = rTriCycle(x)
        for k in nodes[j][1]:
            nodeInputs.append(nodeOutputs[k])
        nodeOutputsBuffer[j+2] = superNate(nodeFunction, nodeInputs)
    nodeOutputsBuffer[0] = int(not nodeOutputsBuffer[0])
    return list(nodeOutputsBuffer)

class brain:
    def __init__(self, numOfNodes):
        n = numOfNodes
        self.nodes = []
        for i in range(n):
            self.nodes.append([])#Make n nodes
            self.nodes[i].append([])#Add function array to node i
            self.nodes[i].append([])#Add input array to node i
            for j in range(3):#Add 27 func selectors to the func array of node i
                #self.nodes[i][0].append(randrange(n+2))
                self.nodes[i][0] = [[],[],[]]
                for k in range(3):
                    self.nodes[i][0][k] = [[],[],[]]
                    for m in range(3):
                        for p in range(3):
                            self.nodes[i][0][k][m].append(randrange(n+2))
            for j in range(3):#Add 3 input selector to the input array of node i
                self.nodes[i][1].append(randrange(n+2))
        self.nodeOutputsBuffer = []
        for i in range(n+2):#n+2 means n nodes + clock + input
            self.nodeOutputsBuffer.append(randrange(3) - 1)#*#
        self.nodeOutputsBuffer[0] = 0
        self.startState = list(self.nodeOutputsBuffer)#Having a start state is crucial as it prevents excesive 'Zero' functions
        self.finalOutputNode = randrange(n) + 2#Node to be used to collect output

    def compute(self, inList, outputLen):
        self.nodeOutputsBuffer = list(self.startState)
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
    
    def getStartStateData(self):
        return self.startState

    def setStartStateData(self, ssdArr):
        self.startState = list(ssdArr)

    def getNodeData(self, indexOfNode):
        if indexOfNode < len(self.nodes):
            return self.nodes[indexOfNode]

    def setNodeData(self, i, ndArr):
        self.nodes[i] = list(ndArr)

    def getFinalOutputNode(self):
        return self.finalOutputNode

    def setFinalOutputNode(self, index):
        self.finalOutputNode = index

def getBrains(numOfBrains, numOfNodes):
    bList = []
    for i in range(numOfBrains):
        bList.append(brain(numOfNodes))
    return list(bList)
