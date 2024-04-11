from random import randrange

def randDist10():
    x = randrange(11)
    val = 10
    while x < val and val > 0:
        x = randrange(11)
        val -= 1
    return x if randrange(2) else -x

class get:
    def __init__(self):
        self.nums = ""
        self.count = randrange(1000)
        for i in range(self.count):
            x = randDist10()
            self.nums += str(x) + ' '
        self.runFlag = False

    def run(self):
        if self.runFlag: return self.nums
        self.runFlag = True
        return self.count

def tempTest():
    q = get()
    q.run()
    z = list(map(int,q.run().split()))
    x = 0 if z==[] else z[z.index(min(z,key=abs))]
    print(x if abs(x) not in z else abs(x))
    return z
