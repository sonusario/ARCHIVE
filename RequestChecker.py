def rulerFile():
    rulerFileLines = []
    with open("C:\\Users\\SSpencer\\Documents\\Requests\\ComparisonChart.txt") as f:
        for line in f:
            rulerFileLines.append(line)
            #print(line)
    return rulerFileLines

def measureFile():
    measureLines = []
    with open("C:\\Users\\SSpencer\\Documents\\Requests\\gold.txt") as f:
        for line in f:
            measureLines.append(line)
    return measureLines

ruler = rulerFile()
measure = measureFile()
rulerSize = len(ruler)
measureSize = len(measure)
notches = 0
matches = 0
pMatches = []
nonMatches = []
continueFlag = False
for i in range(3, rulerSize):
    notches += 1
    rulerSplit = ruler[i].split('\t' or '\n')
    continueFlag = False
    j = 1
    while j < measureSize:
        if continueFlag:
            continueFlag = False
            j = measureSize
            continue
        measureSplit = measure[j].split('\t' or '\n')
        if (measureSplit[2] in rulerSplit[0]) or (rulerSplit[0] in measureSplit[2]):
            matches += 1
            if rulerSplit[2] != measureSplit[4]:
                #string = "rLine: " + str(i) + ", mLine: " + str(j) 
                pMatches.append("*!* " + rulerSplit[0] + " is not pending for some reason. ")# + string)
            else:
                pMatches.append(rulerSplit[0] + " is pending.")
            continueFlag = True
        elif j == (measureSize - 1):
            nonMatches.append(rulerSplit[0] + " was not found.")
        j += 1

pMatchSize = len(pMatches)
nonMatchSize = len(nonMatches)
print("=================================================================================")
print("There were", matches, " matches out of", str(notches) + ".")
print("---------------------------------------------------------------------------------")
for i in range(pMatchSize):
    print(pMatches[i])
print("---------------------------------------------------------------------------------")
for i in range(nonMatchSize):
    print(nonMatches[i])
print("=================================================================================")

#print(ruler[3].split('\t' or '\n'))
#print(measure[4].split('\t' or '\n'))
