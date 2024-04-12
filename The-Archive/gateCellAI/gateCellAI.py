from random import randrange as rand
#from copy import deepcopy as cpy

C = [0,1,-1]
def clock(n):
    return C[n+1]

def superNate(gfList, sel):
    return gfList[ sel[0]+1 ][ sel[1]+1 ][ sel[2]+1 ]

def nSuperNate(gfList, sel, ipn):
    selLen = len(sel)
    if ipn == 1:
        return gfList[ sel[selLen - ipn]+1 ]
    return nSuperNate(gfList[ sel[selLen - ipn]+1 ], sel, ipn-1)

def onzno():
    if rand(2):
        return 1
    return -1

class gate:
    def __init__(self,n2):
        self.function = self.makeFunc()
        self.inputIndex = self.makeInputIndex(n2)
        self.inputs = []

    def recFun(self,ipn):
        if ipn == 1:
            return [rand(3)-1,rand(3)-1,rand(3)-1]
        return [self.recFun(ipn-1),self.recFun(ipn-1),self.recFun(ipn-1)]
        
    def makeFunc(self):
        return self.recFun(3)

    def nMakeFunc(self,ipn):
        return self.recFun(ipn)

    def makeInputIndex(self,n2):
        inputIndex = []
        for i in range(3):
            inputIndex.append(rand(n2))
        return inputIndex

    def nMakeInputIndex(self,n2):
        inputIndex = []
        for i in range(n2):
            inputIndex.append(rand(n2))
        return inputIndex

    def refresh(self, nodes):
        for i in self.inputIndex:
            self.inputs.append(nodes[i].nodeCell)

    def printGateData(self):
        print('--Gate Data--')
        print('Function:',self.function)
        print('Input Index:',self.inputIndex)
        print('Input Cells:',self.inputs)

class cell:
    def __init__(self):
        self.cellVal = 0
        self.threshold = rand(33)
        self.fireVal = onzno()
        self.fireBuf = 0
        self.fireOut = 0
        self.cooldownLimit = rand(33)#play with this
        self.cooldownTimer = 0

    def refresh(self):
        self.celVal = 0
        self.fireBuf = 0
        self.fireOut = 0
        self.cooldownTimer = 0

    def printCellData(self):
        print('--Cell Data--')
        print('Cell Val:',self.cellVal)
        print('Threshold:',self.threshold)
        print('Fire Val:',self.fireVal)
        print('Fire Buf:',self.fireBuf)
        print('Fire Out:',self.fireOut)
        print('CDL:',self.cooldownLimit)
        print('CDT:',self.cooldownTimer)

class node:
    def __init__(self, n):
        self.nodeGate = gate(n)
        self.nodeCell = cell()

    def refresh(self, nodes):
        self.nodeGate.refresh(nodes)
        self.nodeCell.refresh()

class brain:
    def __init__(self, numberOfNodes):
        self.n = numberOfNodes + 2
        self.nodes = self.makeNodes(self.n)
        self.outNode = rand(numberOfNodes) + 2
        #self.ipn = 3

    def makeNodes(self, n):
        arr = []
        arr.append(node(n))
        arr[0].nodeCell.fireOut = -1
        for i in range(1,n):
            arr.append(node(n))
        return arr

    def refreshNodes(self):
        self.nodes[0].nodeCell.fireOut = -1
        for i in range(1,self.n):
            self.nodes[i].refresh(self.nodes)

    def printNodeData(self,i):
        nCell = self.nodes[i].nodeCell
        nGate = self.nodes[i].nodeGate
        print('==== Node ' + str(i) + ' Data ====')
        nCell.printCellData()
        nGate.printGateData()
        print('== End Node ' + str(i) + ' Data ==\n')
        

    def brainCycle(self):
        for i in range(2,self.n):
            self.printNodeData(i)
            nCell = self.nodes[i].nodeCell
            if nCell.cooldownTimer == 0:
                nGate = self.nodes[i].nodeGate
                gfList = nGate.function
                sel = [nGate.inputs[0].fireOut,
                       nGate.inputs[1].fireOut,
                       nGate.inputs[2].fireOut]
                addVal = superNate(gfList,sel)
                nCell.cellVal += addVal
                if nCell.cellVal >= nCell.threshold:
                    nCell.cooldownTimer = nCell.cooldownLimit
                    nCell.fireBuf = nCell.fireVal
                    nCell.cellVal = 0
                else:
                    nCell.fireBuf = 0
            else:
                nCell.cooldownTimer -= 1
                nCell.fireBuf = 0
                nCell.cellVal = 0
        for i in range(2,self.n):
            nCell = self.nodes[i].nodeCell
            nCell.fireOut = nCell.fireBuf
    
    def compute(self, inList, outputLen):
        self.refreshNodes()
        for i in inList:
            self.nodes[1].nodeCell.fireOut = i
            self.brainCycle()
            cfo = self.nodes[0].nodeCell.fireOut
            self.nodes[0].nodeCell.fireOut = clock(cfo)

        self.nodes[1].nodeCell.fireOut = 0
        for i in range(self.n**2):#play with this
            self.brainCycle()
            cfo = self.nodes[0].nodeCell.fireOut
            self.nodes[0].nodeCell.fireOut = clock(cfo)

        output = []
        outCell = self.nodes[self.outNode].nodeCell
        for i in range(outputLen):
            self.brainCycle()
            cfo = self.nodes[0].nodeCell.fireOut
            self.nodes[0].nodeCell.fireOut = clock(cfo)
            output.append(outCell.fireOut)
        return output
