def derivative(f,varArr,wrtIndex):
    h = 0.0001

    return (f(*(varArr[:wrtIndex] + [varArr[wrtIndex] + h] + varArr[wrtIndex+1:])) - f(*varArr))/h

def forwardMultiplyGate(a, b):
    return a * b

def forwardAddGate(a, b):
    return a + b

def forwardCircuit(a, b, c):
    return forwardMultiplyGate(forwardAddGate(a,b), c)

#print(forwardMultiplyGate(-2,3))

stepSize = 0.01

x = -2
y = 5
z = -4

#print(derivative(forwardMultiplyGate,[x,y],0))
#print(derivative(forwardMultiplyGate,[x,y],1))

#x += stepSize * derivative(forwardMultiplyGate,[x,y],0)
#y += stepSize * derivative(forwardMultiplyGate,[x,y],1)

#print(forwardMultiplyGate(x,y))

print(forwardCircuit(x,y,z))

fWRTz = derivative(forwardMultiplyGate,[forwardAddGate(x,y),z],1)
print(derivative(forwardMultiplyGate,[forwardAddGate(x,y),z],0))

print(derivative(forwardAddGate,[x,y],0))
print(derivative(forwardAddGate,[x,y],1))

fWRTx = derivative(forwardAddGate,[x,y],0) * derivative(forwardMultiplyGate,[forwardAddGate(x,y),z],0)
fWRTy = derivative(forwardAddGate,[x,y],1) * derivative(forwardMultiplyGate,[forwardAddGate(x,y),z],0)

print([fWRTx, fWRTy, fWRTz])

x += stepSize * fWRTx
y += stepSize * fWRTy
z += stepSize * fWRTz

print(forwardCircuit(x,y,z))

print()
print("again")
print()

x = -2
y = 5
z = -4

print(forwardCircuit(x,y,z))

gWRTx = derivative(forwardCircuit, [x,y,z], 0)
gWRTy = derivative(forwardCircuit, [x,y,z], 1)
gWRTz = derivative(forwardCircuit, [x,y,z], 2)

print([gWRTx, gWRTy, gWRTz])

x += stepSize * gWRTx
y += stepSize * gWRTy
z += stepSize * gWRTz

print(forwardCircuit(x,y,z))
