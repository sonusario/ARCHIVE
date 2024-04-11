from random import randrange

def buildCoorArr(n):
    cArr = []
    for i in range(n):
        for j in range(n):
            cArr.append([i,j])
    return list(cArr)

def buildGrid(n):
    for i in range()

def gridFill(n):
	a = []
	aLen = n
	for i in range(n):
		a.append(i+1)
	x = []
	for i in range(aLen):
		b = random.randrange(0,aLen - i)
		x.append(a[b])
		a.remove(a[b])
	return list(x)

def canSee(path):
    pathLen = len(path) - 1
    cSee = 1
    n = path[0]
    for i  in range(pathLen):
        if n < path[i+1]:
            cSee += 1
            n = path[i+1]
    return cSee

def gridWalker(grid, iStart, jStart, iStep, jStep, iGoal, jGoal, function):
    i = iStart
    j = jStart
    path = []
    while i != iGoal:
        print(i,j,iStep,jStep,iGoal,jGoal,function)
        while j != jGoal:
            path.append(grid[i][j])
            if function == '+i' or function == '-i':
                break
            j += jStep
        if function == '-j' or function == '+j':
            break
        i += iStep
    return path

def rowOrColumnPuller(inLen, index, grid):
    n = int(inLen/4)
    cardinal = int(index/n)
    if cardinal < 2:
        rowCol = index - (n*cardinal)
    else:
        rowCol = n - (index - (n*cardinal)) - 1
    if cardinal == 0:
        return gridWalker(grid, 0, rowCol, 1, 0, n, n, '+i')
    elif cardinal == 1:
        return gridWalker(grid, rowCol, n-1, 0, -1, -1, -1, '-j')
    elif cardinal == 2:
        return gridWalker(grid, n-1, rowCol, -1, 0, -1, -1, '-i')
    elif cardinal == 3:
        return gridWalker(grid, rowCol, 0, 0, 1, n, n, '+j')

def geneticSolver(inArr):
    inLen = len(inArr)
    n = int(inLen/4)
    grid = gridFill(n)

def cspSolver(inArr):
    return

coorArr = []
def ssSolver(solveOp, inArr):
    coorArr = buildCoorArr(int(len(inArr)/4)
    if solveOp == 0:
        return geneticSolver(inArr)
    return cspSolver(inArr)

def tester():
    inputs = [[3, 1, 2, 2, 2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 3, 2],
              [0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 1, 3, 0, 3],
              [1, 3, 2, 5, 4, 2, 2, 3, 3, 2, 5, 2, 3, 1, 3, 3, 3, 4, 2, 2, 1, 2, 3, 3, 3, 4, 2, 2, 3, 3, 4, 1],
              [4, 3, 0, 3, 2, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 2, 0, 0, 2, 3, 0, 0, 0, 0]]
    
    for i in range(2):
        for j in range(4):
            solution = ssSolver(i, inputs[j])
            print(solution)
