from math import *
# R,C,H,O ######################################################################

a = 0
b = 1
c = 0
d = 1

class C():
    def __init__(self, R1,R2):
        self.cn = (R1, R2)

    def __repr__(self):
        return str(self.cn)

    def __neg__(self):
        return C(-self.cn[a], -self.cn[b])

    def __invert__(self): #conjugate ~
        return C(self.cn[a], -self.cn[b])

    def __add__(self, conu):
        return C(self.cn[a] + conu.cn[c], self.cn[b] + conu.cn[d])

    def __sub__(self, conu):
        return C(self.cn[a] - conu.cn[c], self.cn[b] - conu.cn[d])

    def __mul__(self, conu):
        fp = (self.cn[a]*conu.cn[c]) - (conu.cn[d]*self.cn[b])
        sp = (self.cn[a]*conu.cn[d]) + (conu.cn[c]*self.cn[b])
        return C(fp,sp)

class H():
    def __init__(self, C1, C2):
        self.hn = (C1, C2)

    def __repr__(self):
        return str(self.hn)

    def __neg__(self):
        return H(-self.hn[a], -self.hn[b])

    def __invert__(self): #conjugate ~
        return H(~self.hn[a], -self.hn[b])

    def __add__(self, conu):
        return H(self.hn[a] + conu.hn[c], self.hn[b] + conu.hn[d])

    def __sub__(self, conu):
        return H(self.hn[a] - conu.hn[c], self.hn[b] - conu.hn[d])

    def __mul__(self, conu):
        fp = (self.hn[a]*conu.hn[c]) - (conu.hn[d]*(~self.hn[b]))
        sp = ((~self.hn[a])*conu.hn[d]) + (conu.hn[c]*self.hn[b])
        return H(fp,sp)

class O():
    def __init__(self, H1, H2):
        self.on = (H1, H2)

    def __repr__(self):
        return str(self.on)

    def __neg__(self):
        return O(-self.on[a], -self.on[b])

    def __invert__(self):
        return O(~self.on[a], -self.on[b])

    def __add__(self, conu):
        return O(self.on[a] + conu.on[c], self.on[b] + conu.on[d])

    def __sub__(self, conu):
        return O(self.on[a] - conu.on[c], self.on[b] - conu.on[d])

    def __mul__(self, conu):
        fp = (self.on[a]*conu.on[c]) - (conu.on[d]*(~self.on[b]))
        sp = ((~self.on[a])*conu.on[d]) + (conu.on[c]*self.on[b])
        return O(fp,sp)


e7 = O(H(C(1,0),C(0,0)),H(C(0,0),C(0,0)))
e1 = O(H(C(0,1),C(0,0)),H(C(0,0),C(0,0)))
e2 = O(H(C(0,0),C(1,0)),H(C(0,0),C(0,0)))
e3 = O(H(C(0,0),C(0,1)),H(C(0,0),C(0,0)))
e4 = O(H(C(0,0),C(0,0)),H(C(1,0),C(0,0)))
e5 = O(H(C(0,0),C(0,0)),H(C(0,1),C(0,0)))
e6 = O(H(C(0,0),C(0,0)),H(C(0,0),C(1,0)))
e0 = O(H(C(0,0),C(0,0)),H(C(0,0),C(0,1)))

print(e1*e2*e3*e4*e5*e6*e7)

def cosine(a):
	return cos(radians(a))
def sine(a):
	return sin(radians(a))

p = C(2,2)
q = C(cosine(45),sine(45))
s = C(1,1)
t = C(2,0)
u = C(0,0)

print((q*(p-s))+s)
print((q*(u-s))+s)
print((q*(t-s))+s)
