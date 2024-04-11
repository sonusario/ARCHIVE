import re

def getLines(location, fName):
    f = open(location + fName)
    lines = f.readlines()
    for i in range(len(lines)):
        leli = len(lines[i]) - 1
        lines[i] = re.sub('\n', '', lines[i])#.lower())
    f.close
    if len(lines) == 0: lines.append(' ')
    return lines

def writeToFile(lines, location, fName):
    f = open(location + fName,"w")
    for line in lines:
        f.write(line)# + "\n")
    f.close
    return

def loadDictionary():
    fileName = "\\dictionary.txt"
    dictionary = getLines("",fileName)
    return dictionary

