def j(k,l):
    m = False
    if k not in l and k > 0:
        l.append(k)
        m = True
    return k,l,m

def o(p,q,r,s):
    if s:
        return q,r
    r.append(q)
    return p,r

def t(u,v,w):
    x = '!'
    y = False
    if u == v:
        x = w
        y = True
    return x,y

def a(b,c):
    d = 0
    e = '!'
    f = [0]
    z = False
    for g in range(1,c+1):
        h = d - g
        i = d + g
        d,f,n = j(h,f)
        d,f = o(i,h,f,n)
        e,z = t(d,b,g)
        if z: break
    return d,e,f
