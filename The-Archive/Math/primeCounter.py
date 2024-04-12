def primeCounter(n):
    itrs = n+1
    nums = list(map(lambda x: x+1, list(range(n))))
    numDivis = []
    divis = []
    for i in range(n):
        numDivis.append(0)
        divis.append([])
        for j in range(1,itrs):
            if nums[i]%j == 0:
                numDivis[i] += 1
                divis[i].append(j)

    for i in range(n):
        print(str(i+1) + ':', numDivis[i], divis[i])
    return [nums, numDivis, divis]

arr = primeCounter(1000)
