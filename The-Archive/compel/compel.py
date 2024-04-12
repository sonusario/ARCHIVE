from inspect import signature as sig
from math import *

#Testing Tools and Helpers

def cycle(bits, nBits):
    d = nBits - 1
    while d >= 0:
        if bits[d] == 0:
            bits[d] += 1
            return bits
        else:
            bits[d] = 0
        d -= 1
    return bits

def cycleTest(func, nBits):
    if nBits < 1: return []
    d = len(sig(func).parameters)
    bitSet = []
    for i in range(d):
        bitSet.append([0] * nBits)
    combos = (2 ** nBits) ** d
    for i in range(combos):
        args = tuple(bitSet)
        print("{:0>2d}".format(i) + ":", func.__name__ + "(", *args, ") =", func(*args))
        groupBits = []
        for j in bitSet: groupBits += j
        groupBits = cycle(groupBits, nBits * d)
        prv = 0
        for j in range(d):
            nxt = len(bitSet[j]) + prv
            bitSet[j] = groupBits[prv:nxt]
            prv = nxt
    return

def binToDec(arr, arrLen):
    maxVal = (2**arrLen) /2
    total = 0
    for i in arr:
        total += maxVal * i
        maxVal /= 2
    return int(total)

#Combinatorial Chips

def neg(bit):
    return 0 if bit else 1

def mneg(arr):
    newArr = []
    for bit in arr: newArr.append(neg(bit))
    return newArr

def mand(arr):
    return 1 if 0 not in arr else 0

def band(A, B):
    newArr = []
    for i in range(len(A)):
        newArr.append(mand([A[i], B[i]]))
    return newArr

def mor(arr):
    return 1 if 1 in arr else 0

def mxor(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans ^ arr[i]
    return ans

def nand(arr):
    return neg(mand(arr))

def nor(arr):
    return neg(mor(arr))

def mux(arr):
    d = len(arr)
    nSels = int(log(d,2))
    x = binToDec(arr[:nSels], nSels) + nSels
    if x >= d: return None
    return arr[x]

def dmux(arr):
    nSels = len(arr) - 1
    x = binToDec(arr[:nSels], nSels)
    newArr = [0]*(2**nSels)
    newArr[x] = arr[nSels]
    return newArr

def halfAdder(arr):
    if not (len(arr) == 2): return None
    return mand(arr), mxor(arr)

def fullAdder(arr):
    if not (len(arr) == 3): return None
    x,y = halfAdder(arr[1:len(arr)])
    return mor([mand([arr[0],y]),x]), mxor([y,arr[0]])

def nAdder(A, B):
    d = len(A)
    C = [0] * d
    c = 0
    for i in range(d-1,-1,-1):
        c, C[i] = fullAdder([c, A[i], B[i]])
    return C

def nInc(arr):
    d = len(arr) -1
    b = [0] * d + [1]
    return nAdder(arr, b)

def zero(arr):
    d = len(arr)
    return [0] * d

def ALU(X, Y, zx, nx, zy, ny, f, no):
    X = zero(X) if zx else X
    X = mneg(X) if nx else X
    Y = zero(Y) if zy else Y
    Y = mneg(Y) if ny else Y
    O = nAdder(X, Y) if f else band(X, Y)
    O = mneg(O) if no else O
    zr = 1 if nor(O) else 0
    ng = 1 if O[0] else 0
    return O, zr, ng

#Sequential Chips
'''
def dFF(arr):
    q = arr[0] if arr[1] else arr[2]
    return q,neg(q)
'''

class DFF:
    def __init__(self, state):
        self.q = state
        self.nq = neg(self.q)
        
    def dFF(self, arr): #arr[0] is in, arr[1] is clock
        self.q = arr[0] if arr[1] else self.q
        self.nq = neg(self.q)
        return self.q

class bitREG:
    def __init__(self, state):
        self.dff = DFF(state)

    def bitRegOut(self, arr): #arr[0] is load, arr[1] is in, arr[2] is clock
        return self.dff.dFF([mux([arr[0],arr[1],self.dff.q]),arr[2]])

class nBitREG:
    def __init__(self, n, stateArr):
        self.nBits = n
        self.bitRegs = []
        for i in range(self.nBits):
            self.bitRegs.append(bitREG(stateArr[i]))

    def nRegOut(self, arr):
        load = arr[0]
        iArr = arr[1:self.nBits+1]
        clock = arr[self.nBits+1]
        out = []
        for i in range(self.nBits):
            out.append(self.bitRegs[i].bitRegOut([load, iArr[i], clock]))
        return out

class nRAM:
    def __init__(self, n, w, stateArr2D):
        self.nRegisters = n
        self.bitsPerReg = w
        self.addresSize = int(log(n,2))
        self.indexMarkOne = self.bitsPerReg + 1
        self.indexMarkTwo = self.indexMarkOne + self.addresSize
        
        self.registers = []
        for i in range(self.nRegisters):
            self.registers.append(nBitREG(w, stateArr2D[i]))

    def nRamOut(self, arr):
        load = arr[0]
        iArr = arr[1:self.indexMarkOne]
        aArr = arr[self.indexMarkOne:self.indexMarkTwo]
        clock = arr[self.indexMarkTwo]
        out = self.registers[binToDec(aArr, self.addresSize)].nRegOut([load]+iArr+[clock])
        return out

class counter:
    def __init__(self, n, stateArr):
        self.nBits = n
        self.bits = stateArr

    def countOut(self, arr):# (reset_flag, load_input_flag, increment_flag, [input_arr], clock_state)
        rset = arr[0]
        load = arr[1]
        incr = arr[2]
        iArr = arr[3:self.nBits+3]
        clock = arr[self.nBits+3]
        if not clock:
            return self.bits
        elif rset:
            self.bits = zero(self.bits)
        elif load:
            self.bits = iArr
        elif incr:
            self.bits = nInc(self.bits)

        return self.bits


        
