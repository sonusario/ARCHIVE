import time

def cycle(arr):
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

def f(num):
    x = 0
    y  = 2 ** num
    binary = []
    for i in range(num):
        binary.append(0)
    while x < y:
        #print(binary)
        cycle(binary)
        x = x + 1

print("Program started")
startTime = time.time()
f(10)
endTime = time.time()
elapsedTime = endTime - startTime
print("COMPLETED")
print("Elapsed time:", elapsedTime)
