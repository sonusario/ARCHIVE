def quote(x):
    return x.__name__

def F(x, y, z):
    return x

def U(x, y, z):
    return y

def T(x, y, z):
    return z

def imp(p,q):
    return p(T, q(U,T,T), q)

def neg(p):
    return imp(p,F)

def orr(p,q):
    return imp(imp(p,q),q)

def nnd(p,q):
    return neg(orr(neg(p),neg(q)))

def bic(p,q):
    return nnd(imp(p,q),imp(q,p))

def pisnf(p):
    return imp(neg(p),p)

def pist(p):
    return neg(pisnf(neg(p)))

def pisq(p,q):
    return pist(bic(p,q))

def pisnq(p,q):
    return neg(pisq(p,q))

def mux(p,a,b,c):
    return orr(orr(nnd(a,pisq(p,F)),nnd(b,pisq(p,U))),nnd(c,pisq(p,T)))

def tand(p,q):
    return mux(p,mux(q,U,T,T),T,mux(q,T,T,F))

#imp(imp(imp(imp(imp(p,q),F),imp(imp(q,p),F)),imp(imp(q,p),F)),F) is bic
array_of_fun = [imp,orr,nnd,bic,pisq,pisnq,tand]
array_of_values = [F,U,T]

def fun_test():
    for func in array_of_fun:
        print('\n')
        print("a b |", quote(func))
        print("=========")
        for val_a in array_of_values:
            for val_b in array_of_values:
                print(quote(val_a), quote(val_b),
                      "| ", quote(func(val_a,val_b)))
    return

fun_test()
