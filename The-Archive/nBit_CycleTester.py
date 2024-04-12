import time

def shortCycle4(arr):
    d = len(arr) - 1
    if arr[d] == 0:
        arr[d] = 1
        return list(arr)
    arr[d] = 0
    d -= 1
    while d >= 0:
        if arr[d] == 0:
            arr[d] = 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1

    return list(arr)

def shortCycle3(arr):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] == 0:
            arr[d] = 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1

    return list(arr)

def shortCycle2(arr):
    d = len(arr) - 1
    clone = list(arr)

    while d >= 0:
        if arr[d] == 0:
            clone[d] = 1
            return list(clone)
        else:
            clone[d] = 0
        d -= 1

    return list(clone)

def shortCycle(arr):
    d = len(arr) - 1
    clone = list(arr)
    arrDB_val = int(''.join(map(str, arr)))

    while d >= 0:
        clone[d] = 1
        if int(''.join(map(str, clone))) > arrDB_val:
            return list(clone)
        else:
            clone[d] = 0
        d -= 1

    return list(clone)

def longCycle(arr):
    narr = list(arr)
    d = len(narr)
    m = 2 ** d
    total = 0
    
    for i in range(d):
        total += (2 ** (d - i - 1)) * narr[i]

    total += 1
    if total == m: total = 0
    track = total
    
    for i in range(d):
        x = (2 ** (d - i - 1))
        if x <= track:
            track -= x
            narr[i] = 1
        else:
            narr[i] = 0

    return list(narr)

def f(num, cycleChoice):
    x = 0
    y  = 2 ** num
    binary = []
    for i in range(num):
        binary.append(0)
    while x < y:
        #print(binary)
        if cycleChoice == 0:
            binary = shortCycle(binary)
        elif cycleChoice == 1:
            binary = longCycle(binary)
        elif cycleChoice == 2:
            binary = shortCycle2(binary)
        elif cycleChoice == 3:
            binary = shortCycle3(binary)
        elif cycleChoice == 4:
            binary = shortCycle4(binary)
        x = x + 1

def f2(num):
    x = 0
    y  = 2 ** num
    binary = []
    for i in range(num):
        binary.append(0)
    while x < y:
        print(binary)
        binary = shortCycle3(binary)
        x = x + 1

def f3(num):
    x = 0
    y  = 2 ** num
    binary = []
    for i in range(num):
        binary.append(0)
    while x < y:
        print(binary)
        binary = shortCycle4(binary)
        x = x + 1

def cycleRunner(cycleChoice):
    print("==========================================")
    print("Cycle", cycleChoice, "started")
    startTime = time.time()
    f(24, cycleChoice)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("COMPLETED")
    print("Elapsed time:", elapsedTime)
    print("==========================================")

def cycleRunner2():
    print("==========================================")
    print("Cycle 3 started")
    startTime = time.time()
    f2(2)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("COMPLETED")
    print("Elapsed time:", elapsedTime)
    print("==========================================")

def cycleRunner3():
    print("==========================================")
    print("Cycle 4 started")
    startTime = time.time()
    f3(2)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("COMPLETED")
    print("Elapsed time:", elapsedTime)
    print("==========================================")

#cycleRunner(1)
#cycleRunner(0)
#cycleRunner(2)
cycleRunner(3)
cycleRunner(4)

#cycleRunner2()
#cycleRunner3()
