import time

def cycle(arr):
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

def f(num):
    x = 0
    y  = 2 ** num
    binary = []
    for i in range(num):
        binary.append(0)
    while x < y:
        #print(binary)
        binary = cycle(binary)
        x += 1

print("Program started")
startTime = time.time()
f(10)
endTime = time.time()
elapsedTime = endTime - startTime
print("COMPLETED")
print("Elapsed time:", elapsedTime)
