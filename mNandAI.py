from random import randrange

def mNand(arr):
    for i in arr:
        if i == 0:
            return 1
    return 0

class brain:
    def __init__(self, n):
        self.nodes = []
        for i in range(n):
            self.nodes.append([])
        for i in range(n):
            for j in range(randrange(n+2)):
                self.nodes[i].append(randrange(n+2))
        self.nodeOutputsBuffer = []
        for i in range(n+2):
            self.nodeOutputsBuffer.append(0)
        self.nodeOutputs = list(self.nodeOutputsBuffer)
        self.finalOutputNode = randrange(n) + 2

    def compute(self, inList, outputLen):
        nodeLen = len(self.nodes)
        for i in inList:
            self.nodeOutputs[1] = i
            for j in range(nodeLen):
                nodeInputs = []
                for k in self.nodes[j]:
                    nodeInputs.append(self.nodeOutputs[k])
                self.nodeOutputsBuffer[j+2] = mNand(nodeInputs)
            self.nodeOutputsBuffer[0] = not self.nodeOutputsBuffer[0]
            self.nodeOutputs = list(self.nodeOutputsBuffer)

        self.nodeOutputs[1] = 0
        for i in range(nodeLen):
            for j in range(nodeLen):
                nodeInputs = []
                for k in self.nodes[j]:
                    nodeInputs.append(self.nodeOutputs[k])
                self.nodeOutputsBuffer[j+2] = mNand(nodeInputs)
            self.nodeOutputsBuffer[0] = not self.nodeOutputsBuffer[0]
            self.nodeOutputs = list(self.nodeOutputsBuffer)

        output = []
        for i in range(outputLen):
            for j in range(nodeLen):
                nodeInputs = []
                for k in self.nodes[j]:
                    nodeInputs.append(self.nodeOutputs[k])
                self.nodeOutputsBuffer[j+2] = mNand(nodeInputs)
            self.nodeOutputsBuffer[0] = not self.nodeOutputsBuffer[0]
            self.nodeOutputs = list(self.nodeOutputsBuffer)
            output.append(self.nodeOutputs[self.finalOutputNode])

        return list(output)

def runTest():
    b = brain(100)
    out = b.compute([1,0,1,0], 4)
    #print(b.nodes)
    return out

for i in range(100000):
    x = runTest()
    if x[1] and not x[3]:
        print(x)
print('Done')
