#print("Enter number board with '16' being the blank space: ")
#board = input(":> ")

n = 4

boardWidth = n
boardHeight = n

locLUT = {}
numLUT = {}
count = 1
for i in range(boardHeight):
    for j in range(boardWidth):
        locLUT[count] = [i,j]
        numLUT[str([i,j])] = count 
        count += 1

class tile:
    def __init__(self, num, coords):
        self.num = num
        self.above = None
        self.below = None
        self.left  = None
        self.right = None
        self.coords = coords
        self.goalCoords = locLUT[num]
        self.distFromGoal = abs(self.coords[0] - self.goalCoords[0]) + abs(self.coords[1] - self.goalCoords[1])
        return

    def setAbove(self, tile):
        self.above = tile
        return

    def setBelow(self, tile):
        self.below = tile
        return

    def setLeft(self, tile):
        self.left = tile
        return

    def setRight(self, tile):
        self.right = tile
        return

    def updateDist(self):
        self.goalCoords = locLUT[num]
        self.distFromGoal = abs(self.coords[0] - self.goalCoords[0]) + abs(self.coords[1] - self.goalCoords[1])
        return

class board:
    def __init__(self, dataArr):
        self.tiles = []
        self.blankTile = 0
        count = 0
        for i in range(boardHeight):
            for j in range(boardWidth):
                self.tiles.append(tile(dataArr[count], [i,j]))
                if dataArr[count] == 16:
                    self.blankTile = count
        self.steps = 0
        self.totalDist = 0
        for i in range(len(self.tiles)):
            yup = self.tiles[i].coords[0] - 1
            ydown = self.tiles[i].coords[0] + 1
            y = self.tiles[i].coords[0]
            xleft = self.tiles[i].coords[1] - 1
            xright = self.tiles[i].coords[1] + 1
            x = self.tiles[i].coords[1]
            above = str([yup,x])
            below = str([ydown,x])
            left = str([y,xleft])
            right = str([y,xright])
            if above in numLUT:
                self.tiles[i].setAbove(self.tiles[numLUT[above]-1])
            if below in numLUT:
                self.tiles[i].setBelow(self.tiles[numLUT[below]-1])
            if left in numLUT:
                self.tiles[i].setLeft(self.tiles[numLUT[left]-1])
            if right in numLUT:
                self.tiles[i].setRight(self.tiles[numLUT[right]-1])
            self.totalDist += self.tiles[i].distFromGoal
        self.bCost = self.steps + self.totalDist

    def update(self, dpad):
        fromTile = self.tiles[self.blankTile]
        toTile = None
        if dpad == 'up':
            toTile = self.tiles[self.blankTile].above
        elif dpad == 'down':
            toTile = self.tiles[self.blankTile].below
        elif dpad == 'left':
            toTile = self.tiles[self.blankTile].left
        else:
            toTile = self.tiles[self.blankTile].right

        holder = fromTile.num
        fromTile.num = toTile.num
        toTile.num= holder
        self.totalDist -= fromTile.distFromGoal + toTile.distFromGoal
        fromTile.updateDist()
        toTile.updateDist()
        self.totalDist += fromTile.distFromGoal + toTile.distFromGoal

        self.steps += 1        
