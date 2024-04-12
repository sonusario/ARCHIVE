from time import time

def printN(n,hmap):
    prfx = str(n) + " :"
    print(prfx, "{:05.2f}%".format((hmap[n]/sum(hmap))*100),":",hmap[n])
    return

def ddist(n, string):
    hmap = [0,0,0,0,0,0,0,0,0,0]
    hw = hash(string)
    start = time()
    for i in range(n):
        hws = str(hw)
        for c in hws:
            if c == '-': continue
            hmap[int(c)] += 1
        hw = hash(str(hw))
    for i in range(10):
        printN(i,hmap)
    print("\n\n")
    return

ddist(10000, "Hello, World!")
ddist(10000, "Hello, World!")
