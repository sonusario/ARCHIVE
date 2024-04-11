stateList = [0] * 7
for i in range(len(stateList)):
    stateList[i] = [i]

stateList[0][0] = {'1':['',stateList[1]], '2':['',stateList[3]], '3':['',stateList[5]], '':['','end']}

stateList[1][0] = {'1':['',stateList[2]], '2':['11',stateList[3]], '3':['11',stateList[5]], '':['11','end']}
stateList[3][0] = {'1':['12',stateList[1]], '2':['',stateList[4]], '3':['12',stateList[5]], '':['11','end']}
stateList[5][0] = {'1':['13',stateList[1]], '2':['13',stateList[3]], '3':['',stateList[6]], '':['13','end']}

stateList[2][0] = {'1':['31',stateList[0]], '2':['21',stateList[3]], '3':['21',stateList[5]], '':['21','end']}
stateList[4][0] = {'1':['22',stateList[1]], '2':['32',stateList[0]], '3':['22',stateList[5]], '':['22','end']}
stateList[6][0] = {'1':['23',stateList[1]], '2':['23',stateList[3]], '3':['33',stateList[0]], '':['23','end']}

def update(prv, c):
    return prv[0][c][0], prv[0][c][1]

def las(s):
    cst = stateList[0]
    iii = list(s) + ['']
    out = ''
    for c in iii:
        tmp, cst = update(cst, c)
        out += tmp
    return out

x = '1'
print(x)
for i in range(14):
    x = las(x)
    print(x)

x = '1'
print("Len Comp Start")
for i in range(10000000):
    y = las(x)
    if len(y) == len(x):
        print(x)
        print(y)
    x = y
print("Len Comp Finish")
#0000000000000000000000000000000000000000000000000000000000000000000000000000000
