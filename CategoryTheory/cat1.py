from random import randrange

def ob(C):
    return C["objs"]

def ar(C):
    return C["arrows"]

c = {"objs":['A'],"arrows":['idA']}

def f(n, g = None):
    s = ""
    if n == 0 and g == None:
        s = "1"
    elif n == 0:
        s = 1
    elif n > 0 and g == None:
        s = str(n * f(n-1,0))
    elif n > 0:
        s = n * f(n-1,0)
    else:
        s = "!"
    return s

def pf(n,d):
    chance = randrange(101)
    dev = d
    sign = 0
    if randrange(2): sign = -1
    else: sign = 1
    x = sign * dev * (chance/100)
    return n + x

