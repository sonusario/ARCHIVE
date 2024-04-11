from time import time

def getCheck(x, g, n):
    c = x/g
    for i in range(n-2):
        c = c/g
    if c < 1: c = 1.000000000000001
    return c
    
def nr(x, n):
    g = x/n
    if g < 1: g = 1.000000000000001
    c = getCheck(x,g,n)
    while True:
        gb = g
        g -= (g-c)/n
        if gb == g: break
        c = getCheck(x,g,n)
    return g

def test(n,r):
    nx = n + 1
    print("nr started...")
    start = time()
    for i in range(1,nx):
        nr(nx,r)
    print("nr completed", i, "square roots in", time() - start, "seconds")
    print("pr started...")
    start = time()
    for i in range(1,nx):
        nx**(1/r)
    print("pr completed", i, "square roots in", time() - start, "seconds")
    return

test(10000000,500)
