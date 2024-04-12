stLi = [0] * 2
for i in range(len(stLi)):
    stLi[i] = [i]

stLi[0][0] = {'00':['0',stLi[0]],
              '01':['1',stLi[0]],
              '10':['1',stLi[0]],
              '11':['0',stLi[1]]}

stLi[1][0] = {'00':['1',stLi[0]],
              '01':['0',stLi[1]],
              '10':['0',stLi[1]],
              '11':['1',stLi[1]]}

def update(prv, s):
    return prv[0][s][0], prv[0][s][1]

def ba(s1, s2):
    cst = stLi[0]
    ii1 = list(s1)
    ii2 = list(s2)
    out = ''
    for i in range(len(ii2)):
        tmp, cst = update(cst, ii1[i] + ii2[i])
        out = tmp + out
    return out

a = ['00','01','10','11']
b = ['00','01','10','11']

for i in range(4):
    for j in range(4):
        A = list(a[i])
        A.reverse()
        sa = ''.join(A)
        B = list(b[j])
        B.reverse()
        sb = ''.join(B)

        y = ba(sa,sb)
        print("  " + a[i] + "\n+ " + b[j] + "\n====\n  " + y + "\n")
