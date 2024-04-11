import os

workingDir = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

def readLines(txt):
    tFile = txt.read()
    tLines = tFile.split("\n")
    return tLines

def openFile(fname):
    txt = open(workingDir + "\\" + fname, "r+")
    tLines = readLines(txt)
    txt.close()
    return tLines

def getLines(fname):
    return openFile(fname)
