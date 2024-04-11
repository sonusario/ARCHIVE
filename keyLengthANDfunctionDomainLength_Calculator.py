def f(x):
    return (((1 ** x) - (0 ** x)) * (((2 ** (x - 1)) * x) + (2 ** (x - 1)))) + 1

def g(x):
    return 2 ** ((2 ** x) - 1)

def rec(n):
    if n == 0:
        return 1
    add = 0
    for i in range(n - 1):
        add += rec(n-1)
    return (2 ** n) + add

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 2
    return fib2(n-1) + fib2(n-2)

def recFib(n):
    return fib2((n - 1) + n) + 1

def recSol(n):
    return int((((1**n) - (0**n)) * ((n+1) * (2**(n-1)))) + 1)
