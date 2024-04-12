import time

def cycle(arr, base):
    d = len(arr) - 1
    while d >= 0:
        if arr[d] < base-1:
            arr[d] += 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1
    return list(arr)

def asciiConverter(arr):
    asciiArr = []
    for i in arr:
        asciiArr.append(chr(i + 32))
    return list(asciiArr)

def cycleTester(arrLen, base):
    arr = []
    for i in range(arrLen):
        arr.append(0)

    combos = base ** arrLen
    for i in range(combos + 1):
        print(str(i) + ':',asciiConverter(arr))
        arr = cycle(arr, base)
    return

startTime = time.time()
cycleTester(4,3)
endTime = time.time()
elapsed1 = endTime - startTime

startTime = time.time()
#cycleTester(2,95)
endTime = time.time()
elapsed2 = endTime - startTime

print('Time 1:', elapsed1)
print('Time 2:', elapsed2)
print('Time 2/1:', elapsed2/elapsed1)
print('Time 1*95:', elapsed1*95)
