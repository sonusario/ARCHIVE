from random import randrange

def getRandLine():
    forks = [1] * 15
    spons = [0] * 15

    line = []
    for i in range(30):
        fLen = len(forks)
        sLen = len(spons)

        if fLen:
            if sLen:
                if randrange(2):
                    line.append(forks[0])
                    del forks[0]
                else:
                    line.append(spons[0])
                    del spons[0]
            else:
                line.append(forks[0])
                del forks[0]
        elif sLen:
            line.append(spons[0])
            del spons[0]
    return line

def getKernals():
    line = getRandLine()
    kerns = []
    for i in range(21):
        kerns.append(line[i:i+10])
    return kerns, line

def countFS():
    kerns, line = getKernals()
    for i in range(len(kerns)):
        total = sum(kerns[i])
        if total == 5: return i, line

def declareSolution():
    i, line = countFS()
    print("Winning kernal starting at index", i, "of line", line)
    return line

line = declareSolution()
