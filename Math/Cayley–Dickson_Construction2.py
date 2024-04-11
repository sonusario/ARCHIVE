################################################################################

#COMPLEX

def cn(arr): return list(map(lambda x: -x, arr))

def cc(arr): return [arr[0], -arr[1]]

def ca(arrAB, arrCD): return [arrAB[0] + arrCD[0], arrAB[1] + arrCD[1]]

def cs(arrAB, arrCD): return [arrAB[0] - arrCD[0], arrAB[1] - arrCD[1]]

def cm(arrAB, arrCD):
    fp = arrAB[0] * arrCD[0] - arrCD[1] * arrAB[1]
    sp = arrAB[0] * arrCD[1] + arrCD[0] * arrAB[1]
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

#Octonion numbers in linear algebra

#Octonion vector to matrix
def ovTOm(v):
    return [[v]]

#Octonion matrix to vector
def omTOv(M):
    return M[0]

#Octonion matrix transposition
def omt(A):
    arLen = len(A)
    acLen = len(A[0])

    AT = []
    for j in range(acLen):
        ATi = []
        for i in range(arLen):
            ATi.append(A[i][j])
        AT.append(ATi)
    return AT

#Octonion dot product
def odp(v1, v2):
    pSum = [0,0,0,0,0,0,0]
    for i in range(len(v1)):
        pSum = oa(pSum, om(v1[i] * v2[i]))
    return pSum

#Octonion matrix dot product
def omdp(A, B):
    C = []
    BT = omt(B)
    for Ai in A:
        Ci = []
        for Bj in BT:
            Ci.append(odp(Ai,Bj))
        C.append(Ci)
    return C

#Octonion matrix addition and subtraction
def omas(A,B,f=oa):
    arLen = len(A)
    brLen = len(B)
    if not arLen == brLen:
        print("A and B do not have the same number of rows...")
        return
    
    acLen = len(A[0])
    bcLen = len(B[0])
    if acLen == 0:
        print("A and B do not have the same number of columns...")
        return

    C = []
    for i in range(arLen):
        Ci = []
        for j in range(acLen):
            Ci.append(f(A[i][j], B[i][j]))
        C.append(Ci)
    return C

#Octonion matrix addition
def oma(A,B):
    return omas(A,B)

def oms(A,B):
    return omas(A,B,os)

#Octonion matrix scalar addition
def omsa(A, s):
    C = []
    arLen = len(A)
    acLen = len(A[0])
    for i in range(arLen):
        Ci = []
        for j in range(acLen):
            Ci.append(oa(A[i][j],s))
        C.append(Ci)
    return C

#Octonion matrix scalar multiplication
def omsm(s, A, rhsm=False): #last parameter indicate left or right hand multiplication
    arLen = len(A)
    acLen = len(A[0])

    C = []
    for i in range(arLen):
        Ci = []
        for j in range(acLen):
            if not rhsm: Ci.append(om(s, A[i][j]))
            else: Ci.append(om(A[i][j], s))
        C.append(Ci)
    return C
