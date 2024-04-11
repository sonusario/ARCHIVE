from math import *

def ntsum(n):
    return sum(list(map(int,list(str(n)))))

def fndex(n,ans):
    g = 0
    ch = n**g
    prev = None
    while ch < ans:
        g += 1
        ch = n**g
        if prev is not None and prev == ch: break
        prev = ch
    return g

def isex(n,ex,ans):
    return n**ex == ans

def fnd_Digit_exponent_Sums(r):
    for ans in range(r):
        n = ntsum(ans)
        ex = fndex(n,ans)
        if isex(n,ex,ans):
            print(str(n) + "**" + str(ex) + ' = ' + str(ans))
    return

def fnd_DES2(r):
    for ans in range(2,r):
        n = ntsum(ans)
        try:
            g = log(ans,n)
        except:
            round(3)
        if g == round(g):
            print(str(n) + "**" + str(g) + ' = ' + str(ans))
    return

def test(x, y, debug=True):
    num = x**y
    digitalsum = sum(int(a) for a in str(num))
    if x == digitalsum and debug:
        print(x, y, num)
        return x == digitalsum
def fnd_DES3(r):
    for i in range(1,1000):
        for j in range(1,100):
            if test(i, j):
                print(i, j)

fnd_DES3(200000000)
fnd_DES2(200000000)
#fnd_Digit_exponent_Sums(200000000)
