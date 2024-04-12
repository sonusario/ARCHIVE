from random import randrange as rand
from copy import deepcopy as cpy
import brain

def crossNI(pa,pb,i,mu,n2):
    nAII = pa.getNodeInputIndex(i)
    nBII = pb.getNodeInputIndex(i)
    nCII = []
    for j in range(3):
        if not rand(mu):
            nCII.append(rand(n2))
        elif rand(2):
            nCII.append(nAII[j])
        else:
            nCII.append(nBII[j])
    return cpy(nCII)

def crossFI(ipn, aF, bF, mu, n2):#
    if ipn == 1:
        subF = []
        for i in range(3):
            if not rand(mu):
                subF.append(rand(n2))
            elif rand(2):
                subF.append(aF[i])
            else:
                subF.append(bF[i])
        return cpy(subF)
    return [crossFI(ipn-1,aF[0],bF[0],mu,n2),
            crossFI(ipn-1,aF[1],bF[1],mu,n2),
            crossFI(ipn-1,aF[2],bF[2],mu,n2)]

def crossNF(pa,pb,i,mu,n2):
    nAFI = pa.getNodeFunctionIndex(i)
    nBFI = pb.getNodeFunctionIndex(i)
    return cpy(crossFI(3,nAFI,nBFI,mu,n2))

def crossSSD(pa, pb, mu, n2):
    ssdA = pa.getStartStateData()
    ssdB = pb.getStartStateData()
    ssdC = []
    for i in range(n2):
        if not rand(mu):
            ssdC.append([rand(3) - 1])
        elif rand(2):
            ssdC.append(ssdA[i])
        else:
            ssdC.append(ssdB[i])
    return cpy(ssdC)

def makeChild(pa, pb, child, n, mu):
    n2 = n+2
    child.setStartStateData(crossSSD(pa,pb,mu,n2))
    for i in range(n):
        child.setNodeFunctionIndex(i,crossNF(pa,pb,i,mu,n2))#
        child.setNodeInputIndex(i,crossNI(pa,pb,i,mu,n2))
    if not rand(mu):
        child.setFinalOutputNode(rand(n) + 2)
    elif rand(2):
      child.setFinalOutputNode(pa.getFinalOutputNode())
    else:
        child.setFinalOutputNode(pb.getFinalOutputNode())
    return child
        
def parentSelector(n):
    if n < 0:
        return 0
    elif rand(2):
        return n
    return parentSelector(n-1)

def parentProvider(scores, maxIndex):
    scoresCopy = cpy(scores)
    for i in range(maxIndex - parentSelector(maxIndex)):
        del scoresCopy[scoresCopy.index(max(scoresCopy))]
    return scoresCopy.index(max(scoresCopy))

def evoPop(n, pop, scores, mr, prp):
    pS = len(pop)
    maxIndex = pS - 1
    nonRPT = pS - (pS * prp) #non Random Population Threshold (nonRPT)
    newPop = []
    for i in range(pS):
        if i > nonRPT:
            newPop.append(brain.brain(n))
        else:
            pai = parentProvider(scores, maxIndex)
            pbi = parentProvider(scores, maxIndex)
            pA = cpy(pop[pai])
            pB = cpy(pop[pbi])
            child = brain.brain(n)
            child = makeChild(pA, pB, child, n, int(1/mr))
            newPop.append(child)
    return cpy(newPop)

def gradeBrains(brainPop, inData, outData):
    pS = len(brainPop)
    iLen = len(inData)
    oLen = len(outData[0])
    scores = [0] * pS
    for i in range(pS):
        for j in range(iLen):
            brOut = brainPop[i].compute(inData[j],oLen)
            scores[i] += sum(brOut[k] == outData[j][k] for k in range(oLen))
    return list(scores)

class brainSurgeon:
    def __init__(self, numOfNodes, popSize, muRate, percentRandPop):
        self.nON = numOfNodes
        self.pS = popSize
        self.mR = muRate
        self.pRP = percentRandPop

        self.popScores = []
        self.generation = 0
        self.population = brain.getBrains(self.pS, self.nON)

    def findFittest(self, inData, outData, printFreq):
        perfectScore = len(outData) * len(outData[0])
        while True:
            self.popScores = gradeBrains(self.population, inData, outData)
            if max(self.popScores) == perfectScore:
                w = self.popScores.index(max(self.popScores))
                print('Winner at index:', w)
                print('Found in generation:', self.generation)
                print('Scores:\n', self.popScores)
                print('=' * 42)
                return self.population, self.popScores, self.population[w]
            if self.generation % printFreq == 0:
                print('=' * 42)
                print('Generation:', self.generation)
                print('Perfect Score:', perfectScore)
                print('Top pop Score:', max(self.popScores))
                print('-' * 21)
                print(self.popScores)
                print('Pop Avg:', sum(self.popScores) / self.pS)
                print('=' * 42)
            self.generation += 1
            self.population = evoPop(self.nON, self.population,
                                     self.popScores, self.mR,
                                     self.pRP)
