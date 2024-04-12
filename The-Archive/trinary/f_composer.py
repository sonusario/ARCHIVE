fs = True

x = 'x'
y = 'y'
p = 'p'
q = 'q'
r = 'r'

#######

def fadd(a,b,ci=0):
    x = a + b + ci
    ax = abs(x)
    if ax > 2:
        o = ax - 3
        co = 1
        if x < -1:
            o *= -1
            co *= -1
    elif ax > 1:
        o = -2 * ax + 3
        co = ax - 1
        if x < -1:
            o *= -1
            co *= -1
    else:
        o = x
        co = 0
    return co,o

def agb(a,b):
    x = a - b
    return x

#######

def mini(a,b):
    return "min(1,1 - " + str(a) + " + " + str(b) + ")"

def imp(a,b):
    global fs
    return min(1,1-a+b) if fs else mini(a,b)

def neg(a):
    return imp(a,-1)

def orr(a,b):
    return imp(imp(a,b),b)

def ndd(a,b):
    return neg(orr(neg(a),neg(b)))

def bic(a,b):
    return ndd(imp(a,b),imp(b,a))

def inf(a):
    return imp(neg(a),a)

def ist(a):
    return neg(inf(neg(a)))

def aib(a,b):
    return ist(bic(a,b))

def anb(a,b):
    return neg(aib(a,b))

#######

def mux(s,a,b,c):
    return orr(orr(ndd(a,aib(s,-1)),ndd(b,aib(s,0))),ndd(c,aib(s,1)))

def add(a,b):
    return mux(a,mux(b,1,-1,0),mux(b,-1,0,1),mux(b,0,1,-1))

#######















