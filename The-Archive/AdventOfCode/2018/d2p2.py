import d2p1

def diffByOneIndexer(unfilteredBoxList):
    for box1 in unfilteredBoxList:
        for box2 in unfilteredBoxList:
            if box1 == box2: continue
            diffCounter = 0
            diffIndex = 0
            for i in range(len(box1)):
                if not (box1[i] == box2[i]):
                    diffCounter += 1
                    diffIndex = i
            if diffCounter == 1:
                return box1, diffIndex
                
    return

def removeDiff(w2s, w3s):
    box, index = diffByOneIndexer(w2s + w3s)
    box = box[0:index] + box[index+1:len(box)]
    print(box)
    return

removeDiff(*d2p1.checksum("d2p1.txt"))
