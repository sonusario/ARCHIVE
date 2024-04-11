from random import randrange
from time import time

length = 25000000
timeout = 0.5
percentGate = 0.875

mem = list(map(lambda x: [randrange(length),randrange(2)],list(range(length))))

def diffFinder(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            arr3.append(i)
    return arr3

def changer(data):
    arr = list(data)
    timer = time()
    size = len(arr)
    start = 0
    step = 7
    stop = (int((size*percentGate)/step)*step) - (step - 1)
    gateLoc = list(range(0,stop,step))
    gLsize = len(gateLoc)
    i = 0
    loopCount = 0
    while i < stop:
        gate = arr[i:i+step]
        iA = arr[gate[0][0]%size][1]
        iB = arr[gate[1][0]%size][1]
        cA = arr[gate[2][0]%size][1]
        cB = arr[gate[3][0]%size][1]
        outT = arr[gate[4][0]%size]
        jmp = gateLoc[gate[5][0]%gLsize]
        put = arr[gate[6][0]%size][1]

        i += step

        if iA == cA and iB == cB:
            arr[put] = outT
        else:
            i = jmp
        
        if time() - timer > timeout:
            print("Program timed out on loop", loopCount, "with a timeout of", timeout, "seconds.")
            print("Percent of memory that consists of gates:", percentGate)
            print("Memory length:", length)
            i = stop

        loopCount += 1

    return arr
        
x = changer(mem)
y = diffFinder(x,mem)
print()
print(len(y), "memory units where modified.")
