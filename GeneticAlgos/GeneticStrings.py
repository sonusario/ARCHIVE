from random import randrange
from time import time
import numpy as np
import re

'''
######################################################
'''

class messengerBoi:
    def __init__(self, goalMessage):
        self.goal = goalMessage
        self.mxScore = len(goalMessage)
        self.message = ''.join(list(map(
            lambda x: chr(randrange(32,127)),self.goal)))
        self.score = 0
        self.updateScore()

    def updateScore(self):
        self.score = sum(list(map(
                    lambda a,b: 1 if a == b else 0,
                    self.goal,
                    self.message)))

    def child(self, pA, pB, muRate):
        rng = int(1/muRate)
        newChild = messengerBoi(pA.goal)
        childMessage = ''
        for i in range(pA.mxScore):
            if not randrange(rng):
                childMessage += chr(randrange(32,127))
            elif randrange(2):
                childMessage += pA.message[i]
            else:
                childMessage += pB.message[i]
        newChild.message = childMessage
        newChild.updateScore()
        return newChild

'''
######################################################
'''

class popHandler:
    def __init__(self, popSize, muRte, PRP, itrMax, printFreq, species, spec):
        self.popSize = popSize
        self.muRate = muRte
        self.PRP = PRP
        self.nonRandPopThreshold = popSize - (popSize * PRP)
        self.itrMax = itrMax
        self.printFreq = printFreq
        self.species = species
        self.spec = spec
        self.pop = []
        self.bestMember = None
        self.generation = 0

    def updateNonRandPopThreshold(self):
        self.nonRandPopThreshold = self.popSize - (self.popSize * self.PRP)
        
    def initPop(self):
        best = 0
        for i in range(self.popSize):
            newMember = self.species(*self.spec)
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
        newPop = [self.pop[self.bestMember]]
        for i in range(1,self.popSize):
            if i > self.nonRandPopThreshold:
                newMember = self.species(*self.spec)# * hmmm
                newPop.append(newMember)
                if newPop[i].score > newPop[best].score: best = i
            else:
                pai = self.parentProvider(scores, maxIndex)
                pbi = self.parentProvider(scores, maxIndex)
                pA = self.pop[pai]
                pB = self.pop[pbi]
                newPop.append(self.pop[0].child(pA, pB, self.muRate))
                if newPop[i].score > newPop[best].score: best = i
        self.pop = newPop
        self.bestMember = best
        self.generation += 1

    def searchForSolution(self, printFlag):
        solFlag = False
        count = 0
        if printFlag: print("Solution search started...")
        loopStartTime = time()
        while (count < self.itrMax) and (not solFlag):
            bestMem = self.pop[self.bestMember]
            solFlag = (bestMem.score >= bestMem.mxScore)
            if count % self.printFreq == 0 and printFlag:
                print("=" * 42)
                print("Generation:", count)
                print("Perfect Score:", bestMem.mxScore)
                print("Top Mem Score:", bestMem.score)
                print("-" * 21)
                print("Elapsed Time:", time() - loopStartTime)
                print("=" * 42)
            if (not solFlag) and (count + 1 < itrMax): self.iteratePop()
            count += 1
        if solFlag:
            if printFlag: print("\nSolution Found in Generation",
                                str(count) + "!\n")
        else:
            if printFlag: print("\nNo Solution Found.\n")

'''
######################################################
'''

popSize = 20
muRate = 0.01
PRP = 0.50 #percent of population that is random
itrMax = 10000
printFreq = itrMax/10

species = messengerBoi #non-general statement
spec = ('He!',) #

ga = popHandler(popSize, muRate, PRP, itrMax, printFreq, species, spec)
ga.initPop()
ga.searchForSolution(True)
x = ga.pop[ga.bestMember]
print(x.message) #

'''
######################################################
'''

class paramHandler:
    def __init__(self, mxPopSize, mxItr,species,spec,searchFlag):
        if mxPopSize == 1: mxPopSize += 1
        self.mxPopSize = mxPopSize
        popSiz = randrange(1,mxPopSize)
        muRte = randrange(1,101)/100
        PRP = randrange(1,101)/100
        prntFreq = mxItr-1
        self.ph = popHandler(popSiz, muRte, PRP, mxItr, prntFreq, species, spec)
        self.ph.initPop()
        if searchFlag: self.ph.searchForSolution(False)
        self.mxScore = mxItr
        self.score = 0
        self.updateScore()

    def updateScore(self):
        self.score = self.mxScore - self.ph.generation

    def child(self, pA, pB, muRate):
        rng = int(1/muRate)
        newChild = paramHandler(pA.ph.popSize, pA.mxScore,
                                pA.ph.species, pA.ph.spec,False)
        prp = randrange(101)/100
        options = [[randrange(1,self.mxPopSize),pA.ph.popSize,pB.ph.popSize],
                   [randrange(1,101)/100,pA.ph.muRate,pB.ph.muRate],
                   [randrange(1,101)/100,pA.ph.PRP,pB.ph.PRP]]
        traits = []
        for i in range(3):
            if not randrange(rng):
                traits.append(options[i][0])
            elif randrange(2):
                traits.append(options[i][1])
            else:
                traits.append(options[i][2])
        newChild.ph.popSize = traits[0]
        newChild.ph.muRate = traits[1]
        newChild.ph.PRP = traits[2]
        newChild.ph.updateNonRandPopThreshold()
        newChild.ph.initPop()
        newChild.ph.searchForSolution(False)
        newChild.updateScore()
        return newChild

'''
######################################################
'''

speciesA = messengerBoi #non-general statement
specA = ('He',) #

speciesB = paramHandler #
specB = (10,100,speciesA,specA,True) #


popSize = 100
muRate = 0.01
PRP = 0.50 #percent of population that is random
itrMax = 10000
printFreq = itrMax/10

gb = popHandler(popSize, muRate, PRP, itrMax, printFreq, speciesB, specB)
gb.initPop()
gb.searchForSolution(True)
y = gb.pop[gb.bestMember]
y.ph.printFreq = itrMax/10
print("The End!")
