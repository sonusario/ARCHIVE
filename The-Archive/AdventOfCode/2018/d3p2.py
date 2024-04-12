import d3p1

def getSLdict():
    cCoors = d3p1.getCorners()
    print(len(cCoors))
    siDict = {}
    shortList = {}
    claimID = 1
    for coors in cCoors:
        sx = coors[0]
        sy = coors[1]
        ex = coors[2]
        ey = coors[3]
        shortListFlag = True
        for i in range(sy,ey):
            for j in range(sx,ex):
                coor = str([j,i])
                if coor not in siDict:
                    siDict[coor] = [claimID]
                    if shortListFlag:
                        shortList[claimID] = claimID
                else:
                    siDict[coor].append(claimID)
                    shortListFlag = False
                    for cid in siDict[coor]:
                        if cid in shortList: del shortList[cid]
        claimID += 1
    return shortList

def printAnswer():
    sList = getSLdict()
    print(sList)
    for key in sList:
        print(key)
    return

printAnswer()
