from random import randrange

def randomRule(n):
    r = ''
    for i in range(n):
        r += str(randrange(3))
    return r

def cycle(rule):
    rarr = list(int(c) for c in rule)
    d = len(rule) - 1
    while d >= 0:
        if rarr[d] < 2:
            rarr[d] += 1
            break
        rarr[d] = 0
        d -= 1
    return ''.join(map(str,rarr))

def ruleDictionary(rule):
    ruleWord = '000'
    ruleSet = {}
    for c in rule:
        ruleSet[ruleWord] = c
        ruleWord = cycle(ruleWord)
    return ruleSet

def zcycle(zpr, d):
    for i in range(len(zpr)):
        zpr[i] += 1
        if zpr[i] == d:
            zpr[i] = 0
    return zpr

def tcAuto(n, rule):
    d = 167 #81 for half screen, 167 for full screen
    mid = int(d/2) + 1
    line = '1' * d
    line = line[0:mid] + '2' + line[mid+1:d]
    zpr = [d-1,0,1]
    ruleDict = ruleDictionary(rule)
    for i in range(n):
        newLine = ''
        for j in range(d):
            newLine += ruleDict[line[zpr[0]] + line[zpr[1]] + line[zpr[2]]]
            zpr = zcycle(zpr,d)
        print(line)
        line = newLine
    print(line)
    return ruleDict,zpr

#rdt,zpr = tcAuto(5, '100000000000020000000000000')
#rdt,zpr = tcAuto(32, '011001002011202212021122200')
rdt,zpr = tcAuto(75, '011000122121021012200122220')
'''
rr = randomRule(27)
rdt,zpr = tcAuto(32, rr)
'''
