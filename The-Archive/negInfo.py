def negLen(n):
    return int((((1**n) - (0**n)) * ((n+1) * (2**(n-1)))) + 1)

def negCom(n):
	return 2**negLen(n)

def negInfo(n):
    for i in range(n):
        print(str(i) + ":", negLen(i), ":", negCom(i))

negInfo(8)
