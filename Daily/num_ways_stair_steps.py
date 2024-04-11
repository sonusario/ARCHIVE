callCount = 0

def num_ways_old(n,x):
    global callCount
    callCount += 1
    total = 0
    for s in x:
        d = n - s
        if d > 0: total += num_ways_old(d,x)
        elif d == 0: total += 1
    return total

print(num_ways_old(4,[1,2]))
print(callCount)

def num_ways(n,x):
    if n == 0: return 1
    if n <  0: return 0
    return sum([num_ways(n-s, x) for s in x])

print(num_ways(4,[1,2]))

def fac(n,x):
    if type(n) == type([]):
        return sum(list(map(fac,n)))
    if n == 0: return 1
    return n * fac(n-1,x)

# sum([fac(n-s,x) for s in list(map(lambda v: v - 1, list(range(6))[1:]))])
# [fac(n-s,x) for s in list(map(lambda v: v - 1, x))]

