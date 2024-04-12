def getBinStr(n):
    s = bin(n)
    ss = s[2:len(s)]
    return ss

def bn(ns):
    cFlag = False
    count = 0
    for c in ns:
        if c == '0':
            if not cFlag:
                cFlag = True
            count += 1
        else:
            if cFlag:
                if count%2 == 1:
                    return '0'
                cFlag = False
                count = 0
    if count%2 == 1:
        return '0'
    return '1'

def generate(n):
    n = int(n)
    bss = '1'
    for i in range(1,n+1):
        ns = getBinStr(i)
        bss += bn(ns)
    print(' ', bss)
    return

n = input('> ')
generate(n)
