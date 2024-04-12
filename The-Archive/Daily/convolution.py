def slides(size,xORy):
    slides = xORy - size
    return slides + 1

def convTest1():
    for xLines in range(2,101):
        for yLines in range(2,101):
            gridX = xLines - 1
            gridY = yLines - 1
            convOne = slides(1, gridX) * slides(1, gridY)
            convTwo = slides(2, gridX) * slides(2, gridY)
            convTri = slides(3, gridX) * slides(3, gridY)
            if convOne < 0: convOne = 0
            if convTwo < 0: convTwo = 0
            if convTri < 0: convTri = 0
            total = sum([convOne,convTwo,convTri])
            if (total >= 100 and total < 110) or total < 2:
                print(xLines, ",", yLines)
                print(total)

def convTest2():
    for xLines in range(200):
        for yLines in range(200):
            if xLines > 1 and yLines > 1:
                one = (xLines - 1) * (yLines - 1)
            else:
                one = 0
            if xLines > 2 and yLines > 2:
                two = (xLines - 2) * (yLines - 2)
            else:
                two = 0
            if xLines > 3 and yLines > 3:
                tri = (xLines - 3) * (yLines - 3)
            else:
                tri = 0
            total = one + two + tri
            if total == 100:
                print(xLines, yLines, ": sum(", one, two, tri, ") =", total)

def convTest3():
    for xLines in range(200):
        for yLines in range(200):
            convs = []
            for i in range(min(xLines,yLines)-1):
                j = i+1
                convs.append((xLines - j) * (yLines - j))
            total = sum(convs)
            if total == 100:
                print(xLines, yLines, xLines+yLines,": sum(", convs, ") =", total)

convTest3()
