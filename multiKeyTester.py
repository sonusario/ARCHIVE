from time import time

mKey = [[0,0,0,0,0,0,0,0,0,0],
        [0,1,2,3,4,5,6,7,8,9],
        [0,2,4,6,8,10,12,14,16,18],
        [0,3,6,9,12,15,18,21,24,27],
        [0,4,8,12,16,20,24,28,32,36],
        [0,5,10,15,20,25,30,35,40,45],
        [0,6,12,18,24,30,36,42,48,54,],
        [0,7,14,21,28,35,42,49,56,63],
        [0,8,16,24,32,40,48,56,64,72],
        [0,9,18,27,36,45,54,63,72,81]]

aKey = [[0,1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9,10],
        [2,3,4,5,6,7,8,9,10,11],
        [3,4,5,6,7,8,9,10,11,12],
        [4,5,6,7,8,9,10,11,12,13],
        [5,6,7,8,9,10,11,12,13,14],
        [6,7,8,9,10,11,12,13,14,15],
        [7,8,9,10,11,12,13,14,15,16],
        [8,9,10,11,12,13,14,15,16,17],
        [9,10,11,12,13,14,15,16,17,18]]

def multiKey(n):
    z = 0
    for i in range(n):
        for j in range(10):
            for k in range(10):
                z += mKey[j][k]
    return z

def multiply(n):
    z = 0
    for i in range(n):
        for j in range(10):
            for k in range(10):
                z += j*k
    return z

def test(n):
    t0 = time()
    print('Standard * ans:', multiply(n), ', took', time()-t0, 'seconds')
    t0 = time()
    print('Key * ans:', multiKey(n), ', took', time()-t0, 'seconds')
    return
