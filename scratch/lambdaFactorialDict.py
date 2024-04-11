from time import time

def factorial(x): return x * factorial(x-1) if x else 1

f = {'':(lambda x: x * f[''](x-1) if x else 1)}

y = (lambda a: lambda v: a(a,v))(lambda s,x: 1 if x==0 else x*s(s,x-1))


def testFacts(func, itr):
    startTime = time()
    for i in range(itr):
        out = func(993)
    print("Function " + func.__name__ +
          " took " + str(time()-startTime) +
          " seconds to run.") 
    return

noi = 1000
testFacts(factorial,noi)
testFacts(f[''],noi)
testFacts(y,noi)
