from math import *

def derivative(f,varArr,wrtIndex):
    h = 0.0001
    return (f(*(varArr[:wrtIndex] + [varArr[wrtIndex] + h] + varArr[wrtIndex+1:])) - f(*varArr))/h

def gradient(f,varArr):
    gradArr = []
    for i in range(len(varArr)):
        gradArr.append(derivative(f,varArr,i))
    return gradArr

def gradStep(varArr, gradArr):
    stepSize = 0.01
    for i in range(len(varArr)):
        varArr[i] += stepSize * gradArr[i]
    return varArr

def sig(x):
    return 1/(1 + e**(-x))

def sigGrad(x):
    sgx = sig(x)
    return sgx * (1 - sgx)

class unit():
    def __init__(self, val, grad):
        self.val = val
        self.grad = grad

class mulGate():
    def forward(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = unit(u0.val * u1.val, 0.0)
        return self.utop
    def backward(self):
        self.u0.grad += self.u1.val * self.utop.grad
        self.u1.grad += self.u0.val * self.utop.grad

class addGate():
    def forward(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = unit(u0.val + u1.val, 0.0)
        return self.utop
    def backward(self):
        self.u0.grad += 1 * self.utop.grad
        self.u1.grad += 1 * self.utop.grad

class sigGate():
    def forward(self, u0):
        self.u0 = u0
        self.utop = unit(sig(self.u0.val), 0.0)
        return self.utop
    def backward(self):
        s = sig(self.u0.val)
        self.u0.grad += (s * (1 - s)) * self.utop.grad

#generate inputs
a = unit( 1.0, 0.0)
b = unit( 2.0, 0.0)
c = unit(-3.0, 0.0)
x = unit(-1.0, 0.0)
y = unit( 3.0, 0.0)

#generate gates
mulg0 = mulGate()
mulg1 = mulGate()
addg0 = addGate()
addg1 = addGate()
sg0   = sigGate()

#define the forward pass
def forwardNeuron():
    ax = mulg0.forward(a, x)
    by = mulg1.forward(b, y)
    axpby = addg0.forward(ax, by)
    axpbypc = addg1.forward(axpby, c)
    return sg0.forward(axpbypc)

stepSize = 0.01

s = forwardNeuron()
print(s.val)
s.grad = 1.0

sg0.backward()
addg1.backward()
addg0.backward()
mulg1.backward()
mulg0.backward()

a.val += stepSize * a.grad
b.val += stepSize * b.grad
c.val += stepSize * c.grad
x.val += stepSize * x.grad
y.val += stepSize * y.grad

print([a.grad, b.grad, c.grad, x.grad, y.grad])

s = forwardNeuron()
print(s.val)

def fcf(a,b,c,x,y):
    return 1/(1 + e**-(a*x + b*y + c))

a = 1
b = 2
c = -3
x = -1
y = 3

h = 0.0001

aGrad = (fcf(a+h,b,c,x,y) - fcf(a,b,c,x,y))/h
bGrad = (fcf(a,b+h,c,x,y) - fcf(a,b,c,x,y))/h
cGrad = (fcf(a,b,c+h,x,y) - fcf(a,b,c,x,y))/h
xGrad = (fcf(a,b,c,x+h,y) - fcf(a,b,c,x,y))/h
yGrad = (fcf(a,b,c,x,y+h) - fcf(a,b,c,x,y))/h

print([aGrad, bGrad, cGrad, xGrad, yGrad])
print(gradient(fcf,[a,b,c,x,y]))

arr = gradStep([a,b,c,x,y], gradient(fcf, [a,b,c,x,y]))
for i in range(10):
    print(fcf(*arr))
    arr = gradStep(arr, gradient(fcf, arr))
