def triCycle(arr, direction):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] < 1:
            arr[d] += direction
            return list(arr)
        else:
            arr[d] = -1
        d -= 1

    return list(arr)

def triAdd(a,b,c):
    add = a+b+c
    carry = int(add/2)
    out = add + (3*-carry)
    return carry,out

def nTriAdd(A,B, calcOverflow):
    lenA = len(A)
    lenB = len(B)
    dif = abs(lenA - lenB)
    if dif != 0:
        if lenA < lenB:
            for i in range(dif):
                A.insert(0,0)
                lenA += dif
        else:
            for i in range(dif):
                B.insert(0,0)
                lenB += dif
    arrLen = lenA
    tempC = []
    C = []
    carry = 0
    out = 0
    for i in range(arrLen):
        a = A[arrLen - (i+1)]
        b = B[arrLen - (i+1)]
        carry,out = triAdd(a,b,carry)
        tempC.append(out)
    if carry != 0 and calcOverflow:
        tempC.append(carry)
    lenC = len(tempC)
    for i in range(lenC):
        C.append(tempC[lenC - (i+1)])
    return list(C)

