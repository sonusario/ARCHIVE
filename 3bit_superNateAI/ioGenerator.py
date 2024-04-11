import math

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

def inOutArrs():
    inData = []
    outData = []
    x = [0] * 4
    y = [0] * 4
    for i in range(16):
        for j in range(16):
            inData.append(x + y)
            outData.append(addBin(x,y))
            y = cycle(y)
        x = cycle(x)
    return list(inData), list(outData)
