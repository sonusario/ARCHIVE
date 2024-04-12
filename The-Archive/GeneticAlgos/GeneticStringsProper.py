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
        t = time() - loopStartTime
        return solFlag, count, t

'''
######################################################
'''

popSize = 20
muRate = 0.01
PRP = 0.50 #percent of population that is random
itrMax = 2000
printFreq = itrMax/10

species = messengerBoi #non-general statement
spec = ('I AM',) #

ga = popHandler(popSize, muRate, PRP, itrMax, printFreq, species, spec)
ga.initPop()
ga.searchForSolution(False)
x = ga.pop[ga.bestMember]
print(x.message) #

'''
######################################################
'''

#itrMax = 2000, testRange = 100
def handlerOptimizer(species, spec, itrMax, testRange):
    optimStartTime = time()
    print("=" * 42)
    print("Started...")
    printFreq = itrMax/10
    testRange = 100
    bestOnGen = [itrMax,0,0,0]
    bestOnTime = [3600,0,0,0]
    count = 0
    itrs = 10*50*50
    prntFrq = itrs/100
    for pop in range(1,21,2):
        for mu in range(1,101,2):
            for prp in range(1,101,2):
                totalGens = 0
                totalTime = 0
                popSize = pop
                muRate = mu/100
                PRP = prp/100 
                for i in range(testRange):
                    gb = popHandler(popSize,muRate,PRP,
                                    itrMax,printFreq,species,spec)
                    gb.initPop()
                    solFlag, gen, t = gb.searchForSolution(False)
                    totalGens += gen
                    totalTime += t
                avgGen = totalGens/testRange
                avgTime = totalTime/testRange
                if avgGen < bestOnGen[0] and solFlag:
                    bestOnGen = [avgGen, popSize, muRate, PRP]
                if avgTime < bestOnTime[0] and solFlag:
                    bestOnTime = [avgTime, popSize, muRate, PRP]
                if count % prntFrq == 0:
                    print("=" * 42)
                    print("Test set:", count)
                    print("BOG:", bestOnGen)
                    print("BOT:", bestOnTime)
                    print("Elapsed Time:", time() - optimStartTime)
                    print("=" * 42)
                count += 1
    print("Finished.")
    print("=" * 42)
    print("Total time:", time() - optimStartTime)
    return bestOnGen, bestOnTime

'''
######################################################
'''

itrMax = 100
printFreq = itrMax/10
testRange = 10

species = messengerBoi #non-general statement
spec = ('I AM',) #

bog, bot = handlerOptimizer(species, spec, itrMax, testRange)
print("Params with fewest generations:", bog)
print("Params with least time:", bot)

'''==Best on gen run=='''
print('==Best on gen run==\n')

popSize = bog[1]
muRate = bog[2]
PRP = bog[3]

gb = popHandler(popSize, muRate, PRP, itrMax, printFreq, species, spec)
gb.initPop()
gb.searchForSolution(True)
x = gb.pop[gb.bestMember]
print(x.message) #

'''==Best on time run=='''
print('==Best on time run==\n')

popSize = bot[1]
muRate = bot[2]
PRP = bot[3]

gc = popHandler(popSize, muRate, PRP, itrMax, printFreq, species, spec)
gc.initPop()
gc.searchForSolution(True)
x = gc.pop[gc.bestMember]
print(x.message) #
