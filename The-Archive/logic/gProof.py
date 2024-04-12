def impstr(p,q):
    return "If (" + p + "), then (" + q + ")"

def andstr(p,q):
    return "(" + p + ") and (" + q + ")"

a = "There exists potential states for actual things"
b = "God is required for an actual thing with potential states to be held in it's actual state"
c = "God exists"

p1 = impstr(a,b) + "."
p2 = impstr(andstr(b,a),c) + "."
p3 = a + "."
###
c1 = b + ". MP 1 and 3"
c2 = c + ". MP 2 and 4"

print("1. " + p1)
print("2. " + p2)
print("3. " + p3)
print("4. " + c1)
print("5. " + c2)
