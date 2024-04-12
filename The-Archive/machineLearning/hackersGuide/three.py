from random import randrange
from math import *

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

class circuit():
    def __init__(self):
        self.mulg0 = mulGate()
        self.mulg1 = mulGate()
        self.addg0 = addGate()
        self.addg1 = addGate()
        
    def forward(self, x, y, a, b, c):
        self.ax = self.mulg0.forward(a, x)
        self.by = self.mulg1.forward(b, y)
        self.axpby = self.addg0.forward(self.ax, self.by)
        self.axpbypc = self.addg1.forward(self.axpby, c)
        return self.axpbypc
    
    def backward(self, gradient_top):
        self.axpbypc.grad = gradient_top
        self.addg1.backward()
        self.addg0.backward()
        self.mulg1.backward()
        self.mulg0.backward()

class SVM():
    def __init__(self):
        self.a = unit( 1.0, 0.0)
        self.b = unit(-2.0, 0.0)
        self.c = unit(-1.0, 0.0)
        self.chip = circuit()
        
    def forward(self, x, y):
        self.unit_out = self.chip.forward(x, y, self.a, self.b, self.c)
        return self.unit_out
    
    def backward(self, label):
        self.a.grad = 0.0
        self.b.grad = 0.0
        self.c.grad = 0.0

        pull = 0.0
        if label == 1 and self.unit_out.val < 1:
            pull = 1
        if label == -1 and self.unit_out.val > -1:
            pull = -1
        self.chip.backward(pull)

        self.a.grad += -self.a.val
        self.b.grad += -self.b.val
        
    def learnFrom(self, x, y, label):
        self.forward(x, y)
        self.backward(label)
        self.parameterUpdate()
        
    def parameterUpdate(self):
        stepSize = 0.01
        self.a.val += stepSize * self.a.grad
        self.b.val += stepSize * self.b.grad
        self.c.val += stepSize * self.c.grad

data = []
labels = []

data.append([1.2, 0.7])
labels.append(1)

data.append([-0.3, -0.5])
labels.append(-1)

data.append([3.0, 0.1])
labels.append(1)

data.append([-0.1, -1.0])
labels.append(-1)

data.append([-1.0, 1.1])
labels.append(-1)

data.append([2.1, -3])
labels.append(1)

svm = SVM()

def evalTrainingAccuracy():
    numCorrect = 0
    for i in range(len(data)):
        x = unit(data[i][0], 0.0);
        y = unit(data[i][1], 0.0);
        trueLabel = labels[i]

        predictedLabel = 1 if svm.forward(x,y).val > 0 else -1
        if predictedLabel == trueLabel:
            numCorrect += 1

    return numCorrect / len(data)

for i in range(400):
    n = randrange(len(data))
    x = unit(data[n][0], 0.0)
    y = unit(data[n][1], 0.0)
    label = labels[n]
    svm.learnFrom(x, y, label)

    if i%25 == 0:
        print("Training accuracy at iter " +  str(i) + ": " + str(evalTrainingAccuracy()))

    
