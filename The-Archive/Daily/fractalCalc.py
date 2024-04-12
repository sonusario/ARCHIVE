arr = [[0,1,0],[1,1,1],[0,1,0]]
bArr = [[0,0,0],[0,0,0],[0,0,0]]

downRightLim = len(arr[0]) - 1

def upCheck(coor):
    if coor[0] == 0:
        return False
    elif arr[coor[0] - 1][coor[1]] == 0:
        return False
    return True

def downCheck(coor):
    if coor[0] == downRightLim:
        return False
    elif arr[coor[0] + 1][coor[1]] == 0:
        return False
    return True

def leftCheck(coor):
    if coor[1] == 0:
        return False
    elif arr[coor[0]][coor[1] - 1] == 0:
        return False
    return True

def rightCheck(coor):
    if coor[1] == downRightLim:
        return False
    elif arr[coor[0]][coor[1] + 1] == 0:
        return False
    return True

def boolDir(coor):
    count = 0
    if upCheck(coor): count += 1
    if downCheck(coor): count += 1
    if leftCheck(coor): count += 1
    if rightCheck(coor): count += 1
    if count == 1:
        return True
    return False

def updateBoolArr():
    for y in range(len(arr)):
        for x in range(len(arr)):
            bArr[y][x] = boolDir([y,x])
    return

updateBoolArr()
for row in bArr:
    print(row)
