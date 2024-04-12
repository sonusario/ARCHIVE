from random import randrange
from time import time

n = 8
nList = list(range(n))

#ops: d,dw,r,rw

#gates take in 4 inputs. 2 for use in executing logic based on the
# input look up table (LUT) and 2 for use in determining the
# operation to be used: direct out (d), d and write to memory (dw),
# read out from memory (r), and r and write to memory (rw)

#gates have one memory and one output unit that is specifed as a list of
# length two. This is done to implement a clock that prevents values from
# being overwritten before they are used.

'''
######################################################
'''

class gate:
    def __init__(self):
        self.inGates = self.getInGates()
        self.inLUT = self.getLUT(2,1)
        self.opLUT = self.getLUT(2,2)
        self.mem = [-1, -1]
        self.out = [-1, -1]
        return

    #Specifies where gate gets its inputs from
    def getInGates(self):
        gA = randrange(n)
        gB = randrange(n)
        opA = randrange(n)
        opB = randrange(n)
        return [[gA, gB], [opA, opB]]

    #Makes gate Look Up Tables
    def getLUT(self, n, o):
        if n == 0:
            if o > 1:
                return list(map(lambda x: randrange(2),list(range(o))))
            else:
                return randrange(2)
        return list(map(lambda x: self.getLUT(n-1,o), list(range(2))))

    def load(self, bit, clock):
        self.out[clock] = bit

    def getOut(self, clock):
        return self.out[clock]

    def setOut(self, clock, gList):
        goA = gList[self.inGates[0][0]].out[clock]
        goB = gList[self.inGates[0][1]].out[clock]
        opA = gList[self.inGates[1][0]].out[clock]
        opB = gList[self.inGates[1][1]].out[clock]
        goAB = self.inLUT[goA][goB]
        opAB = self.opLUT[opA][opB]
        if not opAB[0] and not opAB[1]:
            self.out[int(not clock)] = goAB
        elif not opAB[0] and opAB[1]:
            self.mem[int(not clock)] = goAB
            self.out[int(not clock)] = goAB
        elif opAB[0] and not opAB[1]:
            self.out[int(not clock)] = self.mem[clock]
        else:
            self.mem[int(not clock)] = goAB
            self.out[int(not clock)] = self.mem[clock]

class chip: #species
    def __init__(self, numOfGates, startInput, goalOutput): #ex. spec = (8, [0], [0])
        self.chipSize = numOfGates
        self.clock = 0
        self.gates = self.getGates(numOfGates)
        self.startInput = startInput
        self.goalOutput = goalOutput
        self.mxScore = len(goalOutput)
        self.score = 0
        #self.output = self.runChip()
        #self.updateScore()

    def getGates(self, n):
        gArr = []
        for i in range(n):
            gArr.append(gate())
        return gArr

    def updateScore(self):
        self.score = sum(list(map(
            lambda a,b: 1 if a == b else 0,
            self.output,
            self.goalOutput)))

'''
######################################################
'''
