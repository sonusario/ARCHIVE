import re

line = ''
gDict = {}

class node:
    def __init__(self, arg):
        self.arg = arg
        self.sarg = None

    def subarg(self, sarg):
        self.sart = sarg

def tree(spLine, lLen):
    cntr = 0
    synTree = []
    tmpTree = []
    ttDepth = 0
    ttFlag = False
    while cntr < lLen:
        if '(' in spLine[cntr]:
            ttDepth += 1
            ttFlag = True
        elif ')' in spLine[cntr]:
            ttDepth -= 1
        if ttFlag and ttDepth is 1:
            tmpTree.append(list(filter(None,re.findall(r"[^()]+", spLine[cntr]))))
        elif ttFlag and ttDepth > 1:
            tmpTree.append(spLine[cntr])
        elif ttFlag and ttDepth is 0:
            synTree.append(tmpTree)
            tmpTree = []
            ttFlag = False
    synTree
    return

def repl(gdict):
    line = input('> ')
    spLine = line.split(' ')
    lLen = len(spLine)
    synTree = tree(spLine, lLen)
    return gdict

while line is not 'exit':
    gDict = repl(gDict)
