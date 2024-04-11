from time import time
from math import *

def sr(n):
    g = n/2
    c = n/g
    while True:#abs(g-c) > 0.000000000003000:
        gb = g
        g -= (g-c)/2
        if gb == g: break
        c = n/g
    return g

def test(n):
    nx = n + 1
    print("sr started...")
    start = time()
    for i in range(1,nx):
        sr(i)
    print("sr completed", i, "square roots in", time() - start, "seconds")
    print("sqrt started...")
    start = time()
    for i in range(1,nx):
        sqrt(i)
    print("sqrt completed", i, "square roots in", time() - start, "seconds")
    return

test(10000000)
