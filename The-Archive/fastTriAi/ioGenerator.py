import math

def triCycle(arr):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] < 1:
            arr[d] += 1
            return list(arr)
        else:
            arr[d] = -1
        d -= 1

    return list(arr)

def triDCycle(arr):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] > -1:
            arr[d] -= 1
            return list(arr)
        else:
            arr[d] = 1
        d -= 1

    return list(arr)

def triAdd(a,b,c):
    add = a+b+c
    carry = int(add/2)
    out = add + (3*-carry)
    return carry,out

def nTriAdd(A,B, calcOverflow):
    lenA = len(A)
    lenB = len(B)
    dif = abs(lenA - lenB)
    if dif != 0:
        if lenA < lenB:
            for i in range(dif):
                A.insert(0,0)
                lenA += dif
        else:
            for i in range(dif):
                B.insert(0,0)
                lenB += dif
    arrLen = lenA
    tempC = []
    C = []
    carry = 0
    out = 0
    for i in range(arrLen):
        a = A[arrLen - (i+1)]
        b = B[arrLen - (i+1)]
        carry,out = triAdd(a,b,carry)
        tempC.append(out)
    if carry != 0 and calcOverflow:
        tempC.append(carry)
    lenC = len(tempC)
    for i in range(lenC):
        C.append(tempC[lenC - (i+1)])
    return list(C)

def inOutArrs(hiLen):
    inData = []
    outData = []
    x = [-1] * hiLen
    y = [-1] * hiLen
    run = 3**hiLen
    maxLen = math.ceil(math.log(run,3)) + 1
    appendCount = 0
    for i in range(run):
        for j in range(run):
            inData.append(x + y)
            outData.append(nTriAdd(x,y,True))
            while len(outData[appendCount]) < maxLen:
                outData[appendCount].insert(0,0)
            appendCount += 1
            y = triCycle(y)
        x = triCycle(x)
    return list(inData), list(outData)


def inOutArrs2():
    inData = []
    outData = []
    iD = []
    oD = []
    iArr = [1,1,1]
    oArr = [-1,-1,-1]
    for i in range(27):
        iD += iArr
        oD += oArr
        iArr = triDCycle(iArr)
        oArr = triCycle(oArr)
    inData.append(iD)
    outData.append(oD)
    return list(inData), list(outData)
