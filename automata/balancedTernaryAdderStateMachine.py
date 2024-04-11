stLi = [0] * 3
for i in range(len(stLi)):
    stLi[i] = [i]

stLi[0][0] = {'-0':['-',stLi[0]],
              '-+':['0',stLi[0]],
              '0-':['-',stLi[0]],
              '00':['0',stLi[0]],
              '0+':['+',stLi[0]],
              '+-':['0',stLi[0]],
              '+0':['+',stLi[0]],
              '--':['+',stLi[1]],
              '++':['-',stLi[2]]}

stLi[1][0] = {'-+':['-',stLi[0]],
              '00':['-',stLi[0]],
              '0+':['0',stLi[0]],
              '+-':['-',stLi[0]],
              '+0':['-',stLi[0]],
              '++':['+',stLi[0]],
              '--':['0',stLi[1]],
              '-0':['+',stLi[1]],
              '0-':['+',stLi[1]]}

stLi[2][0] = {'--':['-',stLi[0]],
              '-0':['0',stLi[0]],
              '-+':['+',stLi[0]],
              '0-':['0',stLi[0]],
              '00':['+',stLi[0]],
              '+-':['+',stLi[0]],
              '0+':['-',stLi[2]],
              '+0':['-',stLi[2]],
              '++':['0',stLi[2]]}

def update(prv, s):
    return prv[0][s][0], prv[0][s][1]

def bta(s1, s2):
    cst = stLi[0]
    ii1 = list(s1)
    ii2 = list(s2)
    out = ''
    for i in range(len(ii2)):
        tmp, cst = update(cst, ii1[i] + ii2[i])
        out = tmp + out
    return out

a = ['--','-0','-+','0-','00','0+','+-','+0','++']
b = ['--','-0','-+','0-','00','0+','+-','+0','++']

for i in range(9):
    for j in range(9):
        A = list(a[i])
        A.reverse()
        sa = ''.join(A)
        B = list(b[j])
        B.reverse()
        sb = ''.join(B)

        y = bta(sa, sb)
        print("  " + a[i] + "\n+ " + b[j] + "\n====\n  " + y + "\n")
