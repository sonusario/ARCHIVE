from operator import xor

def printResults(arr, locations, total):
    print()
    print("================")
    print("False  :", arr[0], "gates at locations", locations[0])
    print("and    :", arr[1], "gates at locations", locations[1])
    print("~(a->b):", arr[2], "gates at locations", locations[2])
    print("a      :", arr[3], "gates at locations", locations[3])
    print("~(b->a):", arr[4], "gates at locations", locations[4])
    print("b      :", arr[5], "gates at locations", locations[5])
    print("xor    :", arr[6], "gates at locations", locations[6])
    print("or     :", arr[7], "gates at locations", locations[7])
    print("nor    :", arr[8], "gates at locations", locations[8])
    print("xnor   :", arr[9], "gates at locations", locations[9])
    print("~b     :", arr[10], "gates at locations", locations[10])
    print("b->a   :", arr[11], "gates at locations", locations[11])
    print("~a     :", arr[12], "gates at locations", locations[12])
    print("a->b   :", arr[13], "gates at locations", locations[13])
    print("nand   :", arr[14], "gates at locations", locations[14])
    print("True   :", arr[15], "gates at locations", locations[15])
    print("----------------")
    print("Total  :", total)

def getTotals(arr):
    d = len(arr)
    total = 0
    for i in range(d):
        total += arr[i]
    return total

def gateIdentifier(arr):
    d = len(arr)
    total = 0
    for i in range(d):
        total += (2 ** (d - i - 1)) * arr[i]
    return total

def gateCounter(arr):
    d = len(arr)
    gateCounts = []
    gateLocals = []
    for i in range(16):
        gateCounts.append(0)
        gateLocals.append([])
        
    for i in range(d):
        gate = gateIdentifier(arr[i])
        gateCounts[gate] += 1;
        gateLocals[gate].append(i)

    total = getTotals(gateCounts)
    printResults(gateCounts, gateLocals, total)

def cycle(arr):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] == 0:
            arr[d] = 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1

    return list(arr)

def superGate(neg1, neg2, neg3, neg4, neg5, neg6, neg7, a, b):
    return xor(neg1, xor(neg2, xor(neg4, a) or xor(neg5, b)) and xor(neg3, xor(neg6, a) and xor(neg7, b)))

def superGate2(neg1, neg2, neg3, neg4, neg5, neg6, neg7, a, b):
    return xor(neg1, xor(neg2, xor(neg4, a) or xor(neg5, b)) or xor(neg3, xor(neg6, a) or xor(neg7, b)))

def superGate3(neg1, neg2, neg3, neg4, neg5, neg6, neg7, a, b):
    return xor(neg2, xor(neg4, a) or xor(neg5, b)) or xor(neg3, xor(neg6, a) or xor(neg7, b))

def superArr(gList, iList):
    tList = list(gList)
    return superGate3(tList[0], tList[1], tList[2], tList[3], tList[4], tList[5], tList[6], iList[0], iList[1])

def xorFinder():
    gList = [0,0,0,0,0,0,0]
    iList = [0,0]
    xorList = [0,0,0,0]
    xorMatch = []
    xorCount = 0

    for x in range(128):
        ioList = []
        for y in range(4):
            z = superArr(gList, iList)
            ioList.append(z)
            cycle(iList)
        if ioList == xorList:
            xorMatch.append(list(gList))
            xorCount += 1
        cycle(gList)

    print(xorCount)
    print(xorMatch)

def gateMap():
    gList = [0,0,0,0,0,0,0]
    iList = [0,0]
    oList = []
    
    for x in range(128):
        #print("====================================")
        #print("GateList", gList)
        #print("--------------in-||-out-------------")
        ioList = []
        for y in range(4):
            z = superArr(gList, iList)
            #print("InputList", iList, "||", z)
            ioList.append(z)
            cycle(iList)
        oList.append(ioList)
        cycle(gList)
    gateCounter(oList)
    #print(oList)

gateMap()
#xorFinder()
