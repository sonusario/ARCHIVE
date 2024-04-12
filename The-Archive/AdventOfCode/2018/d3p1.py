import fileOpener as fo

def getCorners():
    claims = fo.getLines("d3p1.txt")
    claimCorners = []
    for claim in claims:
        claimArr = claim.split(' ')
        sxy = claimArr[2].split(',')
        exy = claimArr[3].split('x')
        sx = int(sxy[0])
        sy = int(sxy[1][0:len(sxy[1])-1])
        ex = int(exy[0])
        ey = int(exy[1])
        claimCorners.append([sx, sy, sx+ex, sy+ey])
    return claimCorners

def getClaimMap():
    cCoors = getCorners()
    rng = 2000
    cMap = [[0 for i in range(2000)] for j in range(rng)]
    for coors in cCoors:
        sx = coors[0]
        sy = coors[1]
        ex = coors[2]
        ey = coors[3]
        for i in range(sy,ey):
            for j in range(sx,ex):
                cMap[i][j] += 1
    return cMap

def countOverlaps():
    cMap = getClaimMap()
    rng = 2000
    overlapCounter = 0
    for i in range(rng):
        for j in range(rng):
            if cMap[i][j] > 1: overlapCounter += 1
    print("Overlaps:", overlapCounter)
    return

#countOverlaps()
