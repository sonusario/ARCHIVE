from random import randrange

#b for base
#i for input
#o for output

#(number of possible outputs) to the power of (number of possible inputs)
#(output base) to the power of (number of output slots)

def bio(b,i,o):
    return (b**o)**(b**i)

def test(b, i, o):
    limit = 1000000
    nums = list(range(b))
    cnts = []
    for n in range(b):
        cnts.append(0)
    for n in range(limit):
        x = getLUT(b,i,o)
        for m in range(i):
            x = x[randrange(b)]
        cnts[x] += 1
    for n in range(b):
        print(str(n) + ':', cnts[n]/limit)

def getLUT(b, i, o):
    if i == 0:
        if o > 1:
            return list(map(lambda x: randrange(b),list(range(o))))
        else:
            return randrange(b)
    return list(map(lambda x: getLUT(b,i-1,o), list(range(b))))
