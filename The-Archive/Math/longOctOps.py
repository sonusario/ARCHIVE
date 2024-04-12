################################################################################

mulCount = 0
addCount = 0
subCount = 0
negCount = 0

def printCounts():
    global mulCount
    global addCount
    global subCount
    global negCount
    print("mul:", mulCount)
    print("add:", addCount)
    print("sub:", subCount)
    print("neg:", negCount)
    print("="*7)
    print("total:", mulCount + addCount + subCount + negCount)
    return

def zeroCounts():
    global mulCount
    global addCount
    global subCount
    global negCount
    mulCount = 0
    addCount = 0
    subCount = 0
    negCount = 0
    return

#REAL

def neg(n):
    global negCount
    negCount += 1
    return -n

def add(a,b):
    global addCount
    addCount += 1
    return a + b

def sub(a,b):
    global subCount
    subCount += 1
    return a - b

def mul(a,b):
    global mulCount
    mulCount += 1
    return a * b

#COMPLEX

def cn(arr): return list(map(lambda x: neg(x), arr))

def cc(arr): return [arr[0], neg(arr[1])]

def ca(arrAB, arrCD): return [add(arrAB[0], arrCD[0]), add(arrAB[1], arrCD[1])]

def cs(arrAB, arrCD): return [sub(arrAB[0], arrCD[0]), sub(arrAB[1], arrCD[1])]

def cm(arrAB, arrCD):
    fp = sub(mul(arrAB[0], arrCD[0]), mul(arrCD[1], arrAB[1]))
    sp = add(mul(arrAB[0], arrCD[0]), mul(arrCD[1], arrAB[1]))
    return [fp, sp]

def cd(arrAB, arrCD):
    fp = (arrAB[0] * arrCD[0] + arrCD[1] * arrAB[1]) / (arrCD[0]**2 + arrCD[1]**2)
    sp = (arrAB[1] * arrCD[0] - arrAB[0] * arrCD[1]) / (arrCD[0]**2 + arrCD[1]**2)
    return [fp, sp]

#QUATERNIONS

def hn(arr):
    fp = cn(arr[0:2])
    sp = cn(arr[2:4])
    return [fp[0], fp[1], sp[0], sp[1]]

def hc(arr):
    fp = cc(arr[0:2])
    sp = cn(arr[2:4])
    return [fp[0], fp[1], sp[0], sp[1]]

def ha(arrAB, arrCD):
    fp = ca(arrAB[0:2], arrCD[0:2])
    sp = ca(arrAB[2:4], arrCD[2:4])
    return [fp[0], fp[1], sp[0], sp[1]]

def hs(arrAB, arrCD):
    fp = cs(arrAB[0:2], arrCD[0:2])
    sp = cs(arrAB[2:4], arrCD[2:4])
    return [fp[0], fp[1], sp[0], sp[1]]

def hm(arrAB, arrCD):
    fp = cs(cm(arrAB[0:2],arrCD[0:2]),cm(arrCD[2:4],cc(arrAB[2:4])))
    sp = ca(cm(cc(arrAB[0:2]),arrCD[2:4]),cm(arrCD[0:2],arrAB[2:4]))
    return [fp[0], fp[1], sp[0], sp[1]]

#OCTONIONS

def on(arr):
    fp = hn(arr[0:4])
    sp = hn(arr[4:8])
    return [fp[0], fp[1], fp[2], fp[3], sp[0], sp[1], sp[2], sp[3]]

def oc(arr):
    fp = hc(arr[0:4])
    sp = hn(arr[4:8])
    return [fp[0], fp[1], fp[2], fp[3], sp[0], sp[1], sp[2], sp[3]]

def oa(arrAB, arrCD):
    fp = ha(arrAB[0:4], arrCD[0:4])
    sp = ha(arrAB[4:8], arrCD[4:8])
    return [fp[0], fp[1], fp[2], fp[3], sp[0], sp[1], sp[2], sp[3]]

def os(arrAB, arrCD):
    fp = hs(arrAB[0:4], arrCD[0:4])
    sp = hs(arrAB[4:8], arrCD[4:8])
    return [fp[0], fp[1], fp[2], fp[3], sp[0], sp[1], sp[2], sp[3]]

def om(arrAB, arrCD):
    fp = hs(hm(arrAB[0:4],arrCD[0:4]),hm(arrCD[4:8],hc(arrAB[4:8])))
    sp = ha(hm(hc(arrAB[0:4]),arrCD[4:8]),hm(arrCD[0:4],arrAB[4:8]))
    return [fp[0], fp[1], fp[2], fp[3], sp[0], sp[1], sp[2], sp[3]]
