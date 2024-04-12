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

def sixteens(sixteen, eight, four, two, one):
    if one == 1 and two == 1 and four == 1 and eight == 1 and sixteen == 1:
        return 0
    elif one == 1 and two == 1 and four == 1 and eight == 1:
        return 1
    else:
        return sixteen

def thirtyTwos(thirtyTwo, sixteen, eight, four, two, one):
    if one == 1 and two == 1 and four == 1 and eight == 1 and sixteen == 1 and thirtyTwo == 1:
        return 0
    elif one == 1 and two == 1 and four == 1 and eight == 1 and sixteen == 1:
        return 1
    else:
        return thirtyTwo

def sixtyFours(sixtyFour, thirtyTwo, sixteen, eight, four, two, one):
    if one == 1 and two == 1 and four == 1 and eight == 1 and sixteen == 1 and thirtyTwo == 1 and sixtyFour == 1:
        return 0
    elif one == 1 and two == 1 and four == 1 and eight == 1 and sixteen == 1 and thirtyTwo == 1:
        return 1
    else:
        return sixtyFour

def cycle(bList):
    aList = list(bList)
    bList[6] = ones(aList[6])
    bList[5] = twos(aList[5], aList[6])
    bList[4] = fours(aList[4], aList[5], aList[6])
    bList[3] = eights(aList[3], aList[4], aList[5], aList[6])
    bList[2] = sixteens(aList[2], aList[3], aList[4], aList[5], aList[6])
    bList[1] = thirtyTwos(aList[1], aList[2], aList[3], aList[4], aList[5], aList[6])
    bList[0] = sixtyFours(aList[0], aList[1], aList[2], aList[3], aList[4], aList[5], aList[6])
    return list(bList)

def f(num):
    x = 0
    binary = [0,0,0,0,0,0,0]
    while x < num:
        print(binary)
        cycle(binary)
        x = x + 1

f(128)
