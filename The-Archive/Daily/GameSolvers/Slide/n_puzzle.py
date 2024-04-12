class node:
    def __init__(self, data, x, y, d, n = None, e = None, w = None, s = None):
        self.data = data[d-y][d-x]
        self.n = n
        self.e = e
        self.w = w
        self.s = s

    def updateNeighboors(self, grid, x, y, d):
        self.n
        return

data = []
count = 0
while count < 16:
    i = count
    data.append([i+1, i+2, i+3, i+4])
    count += 4

grid = []
for i in range(len(data)):
    for j in range(len(data)):
        grid.append(node(data, 3-j, 3-i, 3))
