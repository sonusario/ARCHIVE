import time
from operator import xor

def printResults(arr, total):
    d = len(arr)
    print("================")
    for i in range(d):
        print(i, ":", arr[i], "gates")
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
        total += (2**(d-i-1)) * arr[i]
    return total

def gateCounter(arr, inLen):
    gfNumCombos = len(arr)
    numOfFunctions = 2**(2**inLen)
    gateCounts = []
    gateLocals = []
    for i in range(numOfFunctions):
        gateCounts.append(0)
        gateLocals.append([])

    for i  in range(gfNumCombos):
        gate = gateIdentifier(arr[i])
        gateCounts[gate] += 1;
        gateLocals[gate].append(i)
    
    printResults(gateCounts, gfNumCombos)

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
#####################
def mor(arr):
    for i in arr:
        if i == 1:
            return 1
    return 0

def negLen(n):
    return int((((1**n) - (0**n)) * ((n+1) * (2**(n-1)))) + 1)

def depth2(gfList, inList, dOneIteration):
    inLen = len(inList)
    dOneLen = 2 ** (inLen - 1)
    arr = []
    for i in range(inLen):
        arr.append(xor(gfList[i + 1 + dOneLen + (dOneIteration * inLen)], inList[i]))
    return list(arr)
    

def depth1(gfList, inList):
    inLen = len(inList)
    dOneLen = 2 ** (inLen - 1)
    arr = []
    if inLen == 0:
        arr.append(1)
    elif inLen == 1:
        arr.append(xor(gfList[1], inList[0]))
        arr.append(xor(gfList[2], inList[0]))
    else:
        for i in range(dOneLen):
            arr.append(xor(gfList[i + 1], mor(depth2(gfList, inList, i))))
    return list(arr)

def superGate(gfList, inList):
    return xor(gfList[0], mor(depth1(gfList, inList)))
#####################

def gateMap(inLen, willPrint):
    gfLen = negLen(inLen)
    inNumCombos = 2 ** inLen
    gfNumCombos = 2 ** gfLen
    inList = []
    gfList = []
    tfResults = []
    
    for i in range(inLen):
        inList.append(0)
    for i in range(gfLen):
        gfList.append(0)

    for i  in range(gfNumCombos):
        if willPrint:
            print("====================================")
            print("GateFunctionList", gfList)
            print("--------------in-||-out-------------")
        sfResults = []
        for j in range(inNumCombos):
            z = superGate(gfList, inList)
            if willPrint:
                print("InputList", inList, "||", z)
            inList = cycle(inList)
            sfResults.append(z)
        gfList = cycle(gfList)
        tfResults.append(sfResults)
    gateCounter(tfResults, inLen)

def superGateRunner(superGateChoice, willPrint):
    print()
    print("==========================================")
    print("Super gate", superGateChoice, "started")
    startTime = time.time()
    gateMap(superGateChoice, willPrint)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("COMPLETED")
    print("Elapsed time:", elapsedTime)
    print("==========================================")

superGateRunner(int(input("Integer Please: ")), 0)
