def add(a,b):
    c = a+b
    if c > 1: c = 1 - c
    elif c < -1: c = -1 - c
    return c 


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

def test(a,b,ci=0):
    c,o = fadd(a,b,ci)
    print([c,o])
    print(c*3 + o)

def tadd(a,b):
    c,o2 = fadd(a[1],b[1],0)
    c,o1 = fadd(a[0],b[0],c)
    return c,o1,o2
