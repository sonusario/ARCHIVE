from random import randrange
import a3bit_superNateAI as nate

def crossND(pa, pb, i):
    ndAF = pa.getNodeData(i)[0]
    ndAI = pa.getNodeData(i)[1]
    ndBF = pb.getNodeData(i)[0]
    ndBI = pb.getNodeData(i)[1]
    ndCF = []
    ndCI = []
    for j in range(8):
        if randrange(2):
            ndCF.append(ndAF[j])
        else:
            ndCF.append(ndBF[j])
    for j in range(3):
        if randrange(2):
            ndCI.append(ndAI[j])
        else:
            ndCI.append(ndBI[j])
    ndC = []
    ndC.append(ndCF)
    ndC.append(ndCI)
    return list(ndC)

def crossSSD(pa, pb):
    ssdA = pa.getStartStateData()
    ssdB = pb.getStartStateData()
    ssdC = []
    ssdLen = len(ssdA)
    for i in range(ssdLen):
        if randrange(2):
            ssdC.append(ssdA[i])
        else:
            ssdC.append(ssdB[i])
    return list(ssdC)

def makeChild(pa, pb, child, numOfNodes):
    child.setStartStateData(crossSSD(pa,pb))
    for i in range(numOfNodes):
        child.setNodeData(i,crossND(pa,pb,i))
    if randrange(2):
        child.setFinalOutputNode(pa.getFinalOutputNode())
    else:
        child.setFinalOutputNode(pb.getFinalOutputNode())
    return child

def parentSelector(n):
    if n < 0:
        return 0
    elif randrange(2):
        return n
    return parentSelector(n-1)

def parentProvider(scores, maxIndex):
    scoresCopy = list(scores)
    for i in range(maxIndex - parentSelector(maxIndex)):
        del scoresCopy[scoresCopy.index(max(scoresCopy))]
    return scoresCopy.index(max(scoresCopy))

def evoPop(numOfNodes, population, scores, mRate, PRP):
    popSize = len(population)
    maxIndex = popSize - 1
    nonRandPopThreshold = popSize - (popSize * PRP)
    newPop = []
    for i in range(popSize):
        if i > nonRandPopThreshold:
            newPop.append(nate.brain(numOfNodes))
        else:
            pai = parentProvider(scores, maxIndex)
            pbi = parentProvider(scores, maxIndex)
            pA = population[pai]
            pB = population[pbi]
            child = nate.brain(numOfNodes)
            child = makeChild(pA, pB, child, numOfNodes)
            newPop.append(child)
    return list(newPop)

def gradeBrains(brainPop, inData, outData):
    popSize = len(brainPop)
    inDataLen  = len(inData)
    outLen = len(outData[0])
    scores = [0] * popSize
    for i in range(popSize):
        for j in range(inDataLen):
            brOutput = brainPop[i].compute(inData[j], outLen)
            scores[i] += sum(brOutput[k] == outData[j][k] for k in range(outLen))
    return list(scores)

class brainSurgeon:
    def __init__(self, numOfNodes, popSize, muRate, percentRandPop):
        self.numOfNodes = numOfNodes
        self.popSize = popSize
        self.muRate = muRate
        self.percentRandPop = percentRandPop
        
        self.popScores = []
        self.generation = 0
        self.population = nate.getBrains(self.popSize, self.numOfNodes)

    def findFittest(self, inData, outData, printFreq):
        perfectScore = len(outData) * len(outData[0])
        while True:
            self.popScores = gradeBrains(self.population, inData, outData)
            if max(self.popScores) == perfectScore:
                wIndex = self.popScores.index(max(self.popScores))
                print('Winner at index:', wIndex)
                print('Found in generation:', self.generation)
                print('Scores:\n', self.popScores)
                print('=' * 42)
                return self.population, self.popScores#[wIndex]
            if self.generation % printFreq == 0:
                print('=' * 42)
                print('Generation:', self.generation)
                print('Perfect Score:', perfectScore)
                print('Top pop Score:', max(self.popScores))
                print('-' * 21)
                print(self.popScores)
                print('Pop Avg:', sum(self.popScores) / self.popSize)
                print('=' * 42)
            self.generation += 1
            self.population = evoPop(self.numOfNodes, self.population, self.popScores, self.muRate, self.percentRandPop)
