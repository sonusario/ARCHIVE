def triAddTC(a,b,c):
    add = a+b+c
    carry = int(add/2)
    out = add + (3*-carry)
    return carry,out

def triAddDC(a,b,c):
    add = a+b
    carry = int(add/2)
    out = add + (3*((carry**2)*-carry))

    if c != 0:
        i,out = triAddDC(out,c,0)
        j,carry = triAddDC(carry,i,0)
    return carry,out

def triAddN(a,b,c):
	if a == b:
		out = -b
		carry = a
	else:
		out = a+b
		carry = 0
	if c != 0:
		i,out = triAddN(out,c,0)
		j,carry = triAddN(carry,i,0)
	return carry,out

def triAddSO(a,b,c):
	sym = {'-':-1,'0':0,'+':1}
	mys = {-1:'-',0:'0',1:'+'}
	x = sym[a]
	y = sym[b]
	z = sym[c]
	if x == y:
		out = mys[-y]
		carry = mys[x]
	else:
		out = mys[x+y]
		carry = '0'
	if z != 0:
		i,out = triAddSO(out,c,'0')
		j,carry = triAddSO(carry,i,'0')
	return carry,out

def triAddS(a,b,c):
	sym = {'-':-1,'0':0,'+':1}
	mys = {-1:'-',0:'0',1:'+'}
	if sym[a] == sym[b]:
		out = mys[-sym[b]]
		carry = mys[sym[a]]
	else:
		out = mys[sym[a] + sym[b]]
		carry = '0'
	if c != '0':
		i,out = triAddS(out,c,'0')
		j,carry = triAddS(carry,i,'0')
	return carry,out

def triAdd(a,b,c):
    sym = {'--':'+','-0':'-','-+':'0',
           '0-':'-','00':'0','0+':'+',
           '+-':'0','+0':'+','++':'-'}
    
    car = {'--':'-','-0':'0','-+':'0',
           '0-':'0','00':'0','0+':'0',
           '+-':'0','+0':'0','++':'+'}

    carry = car[a+b]
    out = sym[a+b]

    if c != '0':
        x,out = triAdd(out,c,'0')
        y,carry = triAdd(carry,x,'0')

    return carry,out

def nTTAdd(arrA,arrB):
    aLen = len(arrA)
    bLen = len(arrB)
    dif = abs(aLen - bLen)
    if dif != 0:
        if aLen < bLen:
            for i in range(dif):
                arrA.insert(0,'0')
        else:
            for i in range(dif):
                arrB.insert(0,'0')
    arrLen = len(arrA)
    temp_arrC = []
    arrC = []
    carry = '0'
    out = '0'
    for i in range(arrLen):
        a = arrA[arrLen - (i + 1)]
        b = arrB[arrLen - (i + 1)]
        carry,out = triAdd(a,b,carry)
        temp_arrC.append(out)        
    if carry != '0':
        temp_arrC.append(carry)
    cLen = len(temp_arrC)
    for i in range(cLen):
        arrC.append(temp_arrC[cLen - (i + 1)])
    return list(arrC)

def testNTTADD(n, mp):
    m = '-'
    z = '0'
    p = '+'
    arrA = [z]
    arrB = [z]
    for i in range(n):
        arrA = nTTAdd(arrA,arrB)
        print(str(i) + ':',arrA)
        arrB = []
        aLen = len(arrA)
        for j in range(aLen):
            arrB.append(z)
        arrB[aLen - 1] = mp
    return

drNum = 5
numOfTrits = abs(drNum)
combos = round((3**numOfTrits) / 2) + 1
dr = '+'

if drNum < 0:
    dr = '-'

m = '-'
z = '0'
p = '+'

testNTTADD(combos, dr)
