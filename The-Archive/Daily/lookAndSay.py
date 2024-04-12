def lass(current):
    result = ''
    cLen = len(current)
    numOfX = 0
    x = current[0]
    for i in range(cLen + 1):
        if i == cLen:
            result += str(numOfX) + x
        elif x == current[i]:
            numOfX += 1
        else:
            result += str(numOfX) + x
            numOfX = 1
            x = current[i]
    return result
