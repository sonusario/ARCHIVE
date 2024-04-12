from random import randrange
from time import time
from math import *

def pushLeft(data=None):
    memory = [data] + memory
    return

def pushRight(data=None):
    memory = memory + [data]
    return

def pullLeft(data=None):
    x = memory[0]
    del memory[0]
    return x

def pullRight(data=None):
    memLen = len(memory) - 1
    x = memory[memLen]
    del memory[memLen]
    return x

class Node():
    def __init__(self):
        self.inputNodes = []
        self.data = None
        self.shift = randrange(95)
        self.output = None

    def calcOutput(self):
        if self.data == None: return None
        itr = key.index(self.data)
        for i in range(self.shift):
            itr = kil[itr]
        self.output = key[itr]

x = Node()

key = list(range(32,127))
kil = list(range(1,len(key)))
kil.append(0)
memory = []
functions = []

string = list(input("Enter line: "))

#cell can writeForget/writeRetain to anywhere in memory
#cell can readRemove/readLeave from anywhere in memory
#cell can remove from memory
#cell can move memory around
#cell can attach to any other cell(s)
#cell can detach from any cell(s)


#cell can shift up to 94 times along the kil
