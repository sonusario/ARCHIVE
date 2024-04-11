import math

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
    return binArr

def binConverter(num, inLen):
    track = num
    #d = int(math.log(num,2))
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

print(binConverter(int(input('Enter and integer:')), 4))
