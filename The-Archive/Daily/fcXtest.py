def fc(n):
    if n == 0: return 1
    return n * fc(n-1)

def fcXtest(n,x):
    for i in range(n):
        y = fc(i)
        if not (y % x == 0):
            print(str(i) + ':', y)
    return
