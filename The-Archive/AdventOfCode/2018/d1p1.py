import os

workingDir = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

def getLines(txt):
    tFile = txt.read()
    tLines = tFile.split("\n")
    return tLines

def opFile(fname):
    txt = open(workingDir + "\\" + fname, "r+")
    tLines = getLines(txt)
    return tLines

def concatLines(tLines):
    cctLine = ""

    for line in tLines:
        cctLine += line

    return cctLine

def answer():
    print(eval(concatLines(opFile("d1p1.txt"))))
    return
