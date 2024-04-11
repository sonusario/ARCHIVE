import time

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

#####################################################

def mNand(arr):
    for i in arr:
        if i == 0:
            return 1
    return 0

def negBin(num, inLen):
    track = num
    arr = []
    pointer = 0
    for i in range(inLen):
        arr.append(0)
    for i in range(inLen):
        x = (2 ** (inLen - i - 1))
        if x <= track:
            track -= x
            arr[pointer] = 1
            pointer += 1
        else:
            pointer += 1
    return arr

def negate(yn, val):
    if yn == 0:
        return not val
    return val

def gfInCombo(gfList, inList):
    gfLen = len(gfList)
    inLen = len(inList)
    nandArr = []
    for i in range(gfLen):
        subNarr = [gfList[i]]
        negatorArr = negBin(i,inLen)
        for j in range(inLen):
            subNarr.append(negate(negatorArr[j], inList[j]))
        nandArr.append(mNand(subNarr))
    return nandArr

def superNand(gfList, inList):
    return mNand(gfInCombo(gfList, inList))
########################################################

def gateMap(inLen, willPrint):
    gfLen = 2 ** inLen
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
            z = superNand(gfList, inList)#
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
