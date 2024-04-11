import fileOpener as fo
import string

def checkBoxIDs(tLines):
    w2s = []
    w3s = []

    for i in range(len(tLines)):
        d = dict.fromkeys(string.ascii_lowercase, 0)
        twoCounter = 0
        threeCounter = 0
        for j in range(len(tLines[i])):
            d[tLines[i][j]] += 1
            if d[tLines[i][j]] == 2:
                twoCounter += 1
            elif d[tLines[i][j]] == 3:
                twoCounter -= 1
                threeCounter += 1
            elif d[tLines[i][j]] == 4:
                threeCounter -= 1
        if twoCounter > 0:
            w2s.append(tLines[i])
        if threeCounter > 0:
            w3s.append(tLines[i])
    
    return w2s, w3s

def checksum(fname):
    tLines = fo.getLines(fname)
    w2s, w3s = checkBoxIDs(tLines)
    print("Checksum:", len(w2s) * len(w3s))
    return w2s, w3s

#checksum("d2p1.txt")
