from operator import xor
import math

def triToDec(arr):
    arrLen = len(arr)
    maxNum = (3**arrLen) / 3#*#
    total = 0
    for i in arr:
        total += i * maxNum
        maxNum /= 3#*#
    return int(total)

#########################

def biCycle(arr):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] == 0:
            arr[d] = 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1
    return list(arr)

def biAdd(a,b,c):
    ab = xor(a,b)
    carry = (ab and c) or (a and b)
    out = xor(ab,c)
    return carry,out

def nBiAdd(A,B, calcOverflow):
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
        carry,out = biAdd(a,b,carry)
        tempC.append(out)
    if carry != 0 and calcOverflow:
        tempC.append(carry)
    lenC = len(tempC)
    for i in range(lenC):
        C.append(tempC[lenC - (i+1)])
    return list(C)

##########################

def triCycle(arr, direction):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] < 1:
            arr[d] += direction
            return list(arr)
        else:
            arr[d] = -1
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

def inOutArrs(hiLen):#*#
    inData = []
    outData = []
    x = [-1] * hiLen#*#
    y = [-1] * hiLen#*#
    run = 3**hiLen##
    maxLen = math.ceil(math.log(run,3)) + 1##
    appendCount = 0
    for i in range(run):#*#
        for j in range(run):#*#
            inData.append(x + y)
            outData.append(nTriAdd(x,y,True))#*#
            while len(outData[appendCount]) < maxLen:##
                outData[appendCount].insert(0,0)##
            appendCount += 1
            y = triCycle(y,1)#*#
        x = triCycle(x,1)#*#
    return list(inData), list(outData)

def inOutArrs2(hiLen):#*#
    inData = []
    outData = []
    x = [0] * hiLen#*#
    y = [0] * hiLen#*#
    run = 2**hiLen##
    maxLen = math.ceil(math.log(run,2)) + 1##
    appendCount = 0
    for i in range(run):#*#
        for j in range(run):#*#
            inData.append(x + y)
            outData.append(nBiAdd(x,y,True))#*#
            while len(outData[appendCount]) < maxLen:##
                outData[appendCount].insert(0,0)##
            appendCount += 1
            y = biCycle(y)#*#
        x = biCycle(x)#*#
    return list(inData), list(outData)

'''
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

def addBin(arrA, arrB):
	bitLen = len(arrA)
	carry = 0
	outBuf = []
	out = [0] * bitLen
	for i in range(bitLen):
		outBuf.append(arrA[bitLen-(i+1)] + arrB[bitLen-(i+1)] + carry)
		if outBuf[i] == 2:
			outBuf[i] = 0
			carry = 1
		elif outBuf[i] == 3:
			outBuf[i] = 1
			carry = 1
		else:
			carry = 0
	for i in range(bitLen):
		out[i] = outBuf[bitLen-(i+1)]
	return list(out)

def decToBin(num):
    if num == 0:
        return list([0])
    track = num
    inLen = int(math.log(num,2)) + 1
    binArr = []
    pointer = 0
    for i in range(inLen):
	    binArr.append(0)
    for i in range(inLen):
        x = (2 ** (inLen - i - 1))
        if x <= track:
            track -= x
            binArr[pointer] = 1
            pointer += 1
        else:
            pointer += 1
    return list(binArr)

def binConverter(num, inLen):
    track = num
    binArr = []
    pointer = 0
    for i in range(inLen):
        binArr.append(0)
    for i in range(inLen):
        x = (2 ** (inLen - i - 1))
        if x <= track:
            track -= x
            binArr[pointer] = 1
            pointer += 1
        else:
            pointer += 1
    return binArr

def inOutArrs2():
    inData = []
    outData = []
    outLen = 8
    for i in range(16):
        for j in range(16):
            inData.append(decToBin(i) + [0,0] + decToBin(j))
            outData.append(binConverter(i+j, outLen))
    for i in range(16):
        for j in range(16):
            if j < i:
                inData.append(decToBin(i) + [0,1] + decToBin(j))
                outData.append(binConverter(i-j, outLen))
    for i in range(16):
        for j in range(16):
            if j != 0:
                inData.append(decToBin(i) + [1,0] + decToBin(j))
                outData.append(binConverter(int(i/j), outLen))
    for i in range(16):
        for j in range(16):
            inData.append(decToBin(i) + [1,1] + decToBin(j))
            outData.append(binConverter(i*j, outLen))
    return list(inData), list(outData)
'''
