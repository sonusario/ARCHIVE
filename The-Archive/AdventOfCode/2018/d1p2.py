import d1p1

def getIntList():
    arrOfStrings = d1p1.opFile("d1p1.txt")
    arrOfInts = []
    for line in arrOfStrings:
        arrOfInts.append(eval(line))
    return arrOfInts

def trackRepeats():
    arrOfInts = getIntList()

    total = 0
    tracker = []
    itrCount = 0
    while True:
        itrCount += 1
        for i in arrOfInts:
            total += i
            if total in tracker: return [total, itrCount]
            tracker.append(total)
        #if itrCount%1000: print("Total: " + str(total) + ", Iteration: " + str(itrCount))

x = trackRepeats()        
print("Repeated Number: " + str(x[0]) + ", Iteration Reached:" + str(x[1]))
