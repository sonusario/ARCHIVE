from random import randrange
#from time import time
#from math import *

key = list(range(32,127))
kil = list(range(1,len(key)))
kil.append(0)

class memNode():
    def __init__(self, data=None, connections=None, whoEdit=None):
        self.data = data
        self.connections = connections
        self.whoEdit = whoEdit
        

class Cell():
    def __init__(self, noc, cid):
        #self.shift = randrange(95)
        self.cid = cid
        self.memReadFrom = randrange(noc)
        

string = list(input("Enter string to reverse: "))
noc = int(input("Enter number of cells: "))

cells = []
mem = memNode('root',[])
output = []
expOutput = []

for i in range(noc):
    cells.append(Cell(noc,i))

for c in string:
    expOutput = [c] + expOutput
    mem.connections.append(memNode(c,[mem]))
