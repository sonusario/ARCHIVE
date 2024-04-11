def ones(one):
    if one == 1:
        return 0
    else:
        return 1

def twos(two, one):
    if one == 1 and two == 1:
        return 0
    elif one == 1:
        return 1
    else:
        return two

def fours(four, two, one):
    if one == 1 and two == 1 and four == 1:
        return 0
    elif one == 1 and two == 1:
        return 1
    else:
        return four

def eights(eight, four, two, one):
    if one == 1 and two == 1 and four == 1 and eight == 1:
        return 0
    elif one == 1 and two == 1 and four == 1:
        return 1
    else:
        return eight

def cycle(bList):
    aList = list(bList)
    bList[3] = ones(aList[3])
    bList[2] = twos(aList[2], aList[3])
    bList[1] = fours(aList[1], aList[2], aList[3])
    bList[0] = eights(aList[0], aList[1], aList[2], aList[3])
    return list(bList)

def f(num):
    x = 0
    binary = [0,0,0,0]
    while x < num:
        print(binary)
        cycle(binary)
        x = x + 1

f(16)
