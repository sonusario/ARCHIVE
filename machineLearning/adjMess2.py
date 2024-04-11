from random import randrange
from time import time
import numpy as np

minRange = -300
maxRange = -minRange + 1

def restring(s):
    return str(len(s) + 1 + len(str(len(s) + 1 + len(str(len(s)+1))))) + ' ' + s

def convertMatMess(nOut):
    s = ''
    for n in nOut:
        x = n%95
        if(x >= 95) or (x < 0):
            s += chr(20)
        else:
            s += chr(x+32)
    return s

def initPop(n, nov):
    p = []
    for i in range(n):
        verts = np.random.randint(minRange, maxRange, nov)
        graph = np.random.uniform(-1,1,(nov,nov))
        edges = np.array(list(map(
            lambda x: list(map(lambda y: 0 if randrange(2) else y, x)),
            graph)))
        p.append([i, 0, verts, edges])
    return p

def getScores(pop):
    scores = []
    for i in range(len(pop)):
        scores.append(pop[i][1])
    return scores

def parentSelector(n):
    if n == 0: return 0
    if randrange(2): return n#######
    return parentSelector(n-1)

def parentProvider(scrs, maxIndex):
    scores = list(np.copy(scrs))
    for i in range(maxIndex - parentSelector(maxIndex)):
        del scores[scores.index(max(scores))]
    return scores.index(max(scores))

def getParentModifiers(nov):
    a = np.ones(nov)
    aa = np.copy(a)
    ab = np.copy(a)
    
    b = np.ones(nov*nov)
    ba = np.copy(b)
    bb = np.copy(b)

    aa[int(aa.size/2):aa.size//1:1] = 0
    ab[:ab.size//2:1] = 0

    ba[int(ba.size/2):ba.size//1:1] = 0
    bb[:bb.size//2:1] = 0

    ba = np.reshape(ba, (-1,nov))
    bb = np.reshape(bb, (-1,nov))
    return [aa, ab, ba, bb]

def mixParents(i, pA, pB, PM, muRate):
    rng = int(1/muRate)
    verts = (pA[2] * PM[0]) + (pB[2] * PM[1])
    edges = (pA[3] * PM[2]) + (pB[3] * PM[3])
    for i in range(len(verts)):
        if not randrange(rng): verts[i] = randrange(minRange,maxRange)
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            if not randrange(rng): edges[i][j] = np.random.uniform(-1,1)
    return [i, 0, verts, edges]

def newPop(pop, nov, PM, muRate, PRP):
    popSize = len(pop)
    maxIndex = popSize - 1
    nonRandPopThreshold = popSize - (popSize * PRP)
    scores = getScores(pop)    
    p = []
    for i in range(popSize):
        if i > nonRandPopThreshold:
            verts = np.random.randint(minRange, maxRange, nov)
            edges = np.random.uniform(-1,1,(nov,nov))
            p.append([i, 0, verts, edges])
        else:
            pai = parentProvider(scores, maxIndex)
            pbi = parentProvider(scores, maxIndex)
            pA = pop[pai]
            pB = pop[pbi]
            child = mixParents(i, pA, pB, PM, muRate)
            p.append(child)
    return p

def getMatMess(arr, messLen):
    nodes = np.copy(arr[2])
    graph = np.copy(arr[3])
    out = []
    for i in range(messLen):
        nodes = np.round(np.matmul(nodes,graph))
        out.append(int(nodes[0]))
    return out

def memScore(output, target):
    score = 0
    for i in range(len(output)):
        x = output[i]%95
        if chr(x+32) == target[i]:
            score += 47
        else:
            n = ord(target[i]) - 32
            diff = abs(x - n)
            score += 47 - min(diff, 95 - diff)
    return score

def findLeader(pop, nov, message, muRate, PRP, itrMax, printFreq):
    PM = getParentModifiers(nov)
    messLen = len(message)
    maxScore = messLen * 47
    bestMem = 0
    winFlag = False
    count = 0
    loopStartTime = time()
    while (count < itrMax) and (not winFlag):
        for i in range(len(pop)):
            output = getMatMess(pop[i], messLen)
            pop[i][1] = memScore(output, message)
            if pop[i][1] >= maxScore: winFlag = True
        arr = getScores(pop)
        bestMem = arr.index(max(arr))
        if count % printFreq == 0:
            print("=" * 42)
            print("Generation:", count)
            print("Perfect Score:", maxScore)
            print("Top Mem Score:", pop[bestMem][1])
            print("-" * 21)
            print("First Ten Scores:", getScores(pop[0:10]))
            print("Elapsed Time:", time() - loopStartTime)
            print("=" * 42)
        
        if (not winFlag) and (count + 1 < itrMax):
            pop = newPop(pop, nov, PM, muRate, PRP)
        count += 1
    if winFlag: print("\nWinner Found!\n")
    return bestMem, pop

popSize = 100
numOfVerts = 2
#message = 'Hello world' #not found
message = 'Hi' #record: 2v
#message = 'Hello world, and all its inhabitants.'
muRate = 0.01
percentRandPop = 0.80
itrMax = 100000
printFreq = popSize * 100

print("#" * 33)
startTime = time()
pop = initPop(popSize, numOfVerts)
message = restring(message)

bestMem, pop = findLeader(pop,
                          numOfVerts,
                          message,
                          muRate,
                          percentRandPop,
                          itrMax,
                          printFreq)
print("Best Member of Pop Index:", bestMem)
print(pop[bestMem][2])
#print(np.round(pop[bestMem][3],2))
output = getMatMess(pop[bestMem], len(message))
print(output)
print("Runtime:", time() - startTime)
print("#" * 33)
print(convertMatMess(output))
