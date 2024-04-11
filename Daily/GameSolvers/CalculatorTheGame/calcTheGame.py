from random import randrange
from time import time
import numpy as np
import re

'''
self.score = abs(goal - progress) + (self.move - (self.move-count))
'''

fudi = {'+': (lambda b: lambda a: a+b),
        '-': (lambda b: lambda a: a-b),
        '*': (lambda b: lambda a: a*b),
        '/': (lambda b: lambda a: int(a/b) if a%b is 0 else -666),
        '^': (lambda b: lambda a: a**b),
        'f': (lambda b: lambda a: -a),#negate
        'r': (lambda b: lambda a: int(str(a)[:len(str(a))-1]) if len(str(abs(a))) > 1 else 0),#remove
        'a': (lambda b: lambda a: int(str(a) + str(b))),#append
        '=': (lambda b: lambda a: int(re.sub(str(b[0]),str(b[1]),str(a)))),#replace
        'm': (lambda b: lambda a: int(str(a)[::-1]) if a > 0 else -666)} #reverse

class calcMember:
    def __init__(self, moves, funcCodes, fNums, startVal, goalVal, mxScore):
        self.moves = moves
        self.funcCodes = funcCodes
        self.fNums = fNums
        self.funcIns,self.funcNums = self.getRandFuncIns(moves,funcCodes,fNums)
        self.funcs = self.getFuncs(self.funcIns,self.funcNums)
        self.startVal = startVal
        self.goalVal = goalVal
        self.score = 0
        self.calcScore()
        self.mxScore = mxScore

    def getRandFuncIns(self, moves ,funcs, fNums):
        fsL = len(funcs)
        arr0 = []
        arr1 = []
        for i in range(moves):
            f = randrange(fsL)
            arr0.append(funcs[f])
            arr1.append(fNums[f])
        return arr0, arr1

    def getFuncs(self, funcIns, funcNums):
        arr = []
        #print(funcIns, funcNums)
        for i in range(len(funcIns)):
            arr.append(fudi[funcIns[i]](funcNums[i]))
        return arr

    def calcScore(self, printFlag=None):
        progress = self.startVal
        count = 0
        while count < self.moves and progress is not self.goalVal:
            progress = self.funcs[count](progress)
            if printFlag: print(progress)
            count += 1
        self.score = int(progress == self.goalVal)

    def child(self, pA, pB, muRate):
        rng = int(1/muRate)
        fsL = len(pA.funcCodes)
        newChild = calcMember(pA.moves, pA.funcCodes, pA.fNums,
                              pA.startVal, pA.goalVal, pA.mxScore)
        for i in range(len(pA.funcIns)):
            if not randrange(rng):
                f = randrange(fsL)
                newChild.funcIns[i] = pA.funcCodes[f]# could also use new child
                newChild.funcNums[i] = pA.fNums[f]
            elif randrange(2):
                newChild.funcIns[i] = pA.funcIns[i]
                newChild.funcNums[i] = pA.funcNums[i]
            else:
                newChild.funcIns[i] = pB.funcIns[i]
                newChild.funcNums[i] = pB.funcNums[i]
        newChild.funcs = self.getFuncs(newChild.funcIns,newChild.funcNums)
        return newChild

'''
Non-general Statements above this line with a few exceptions
'''

class popHandler:
    def __init__(self, popSize, muRte, percentRandPop, itrMax, printFreq, spec):
        self.popSize = popSize
        self.muRate = muRte
        self.nonRandPopThreshold = popSize - (popSize * percentRandPop)
        self.itrMax = itrMax
        self.printFreq = printFreq
        self.spec = spec
        self.pop = []
        self.bestMember = None
        self.generation = 0

    def initPop(self):
        best = 0
        for i in range(self.popSize):
            newMember = calcMember(*self.spec)#non-general statement
            self.pop.append(newMember)
            if newMember.score > self.pop[best].score:
                best = i
        self.bestMember = best
        self.generation = 1

    def parentSelector(self, n):
        if n == 0: return 0
        elif randrange(2): return n
        else: return self.parentSelector(n-1)

    def parentProvider(self, scrs, maxIndex):
        scores = list(np.copy(scrs))
        for i in range(maxIndex - self.parentSelector(maxIndex)):
            del scores[scores.index(max(scores))]
        return scores.index(max(scores))
    
    def iteratePop(self):
        scores = []
        maxIndex = self.popSize - 1
        for member in self.pop:
            scores.append(member.score)
        best = 0
        newPop = []
        for i in range(self.popSize):
            if i > self.nonRandPopThreshold:
                newMember = calcMember(*self.spec)
                newPop.append(newMember)
                if newPop[i].score > newPop[best].score:
                    best = i
            else:
                pai = self.parentProvider(scores, maxIndex)
                pbi = self.parentProvider(scores, maxIndex)
                pA = self.pop[pai]
                pB = self.pop[pbi]
                newPop.append(self.pop[0].child(pA, pB, self.muRate))
        self.pop = newPop
        self.bestMember = best
        self.generation += 1

    def searchForSolution(self):
        solFlag = False
        count = 0
        print("Solution search started...")
        loopStartTime = time()
        while (count < self.itrMax) and (not solFlag):
            bestMem = self.pop[self.bestMember]
            solFlag = (bestMem.score >= bestMem.mxScore)
            if count % self.printFreq == 0:
                print("=" * 42)
                print("Generation:", count)
                print("Perfect Score:", bestMem.mxScore)
                print("Top Mem Score:", bestMem.score)
                print("-" * 21)
                print("Elapsed Time:", time() - loopStartTime)
                print("=" * 42)
            if (not solFlag) and (count + 1 < itrMax): self.iteratePop()
            count += 1
        if solFlag: print("\nSolution Found!\n")
        else: print("\nNo Solution Found.\n")

'''
######################################################
'''

popSize = 100
muRate = 0.01
percentRandPop = 0.80
itrMax = 100000
printFreq = popSize * 100
#spec = (4,['*','-','a'],[5,6,4],0,-120,1) #non-general statement
spec = (6,#num of moves
        ['+','a','-','m'],#functions available
        [3,1,2,''],#number associated with functions
        0,#start val
        123,#goal val
        1)#max score

ga = popHandler(popSize, muRate, percentRandPop, itrMax, printFreq, spec)
ga.initPop()
ga.searchForSolution()
x = ga.pop[ga.bestMember]
print(x.funcIns)#
print(x.funcNums)
x.calcScore(1)
