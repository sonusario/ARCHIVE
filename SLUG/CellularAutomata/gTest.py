from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
from random import randrange
import time

startTime = time.time()

def rulToDec(rul):
    arr = list(int(c) for c in rul)
    d = len(rul) - 1
    total = 0
    for i in arr:
        total += (3**d) * i
        d -= 1
    return total

def randomRule(n):
    r = ''
    for i in range(n):
        r += str(randrange(3))
    return r

def cycle(rule):
    rarr = list(int(c) for c in rule)
    d = len(rule) - 1
    while d >= 0:
        if rarr[d] < 2:
            rarr[d] += 1
            break
        rarr[d] = 0
        d -= 1
    return ''.join(map(str,rarr))

def ruleDictionary(rule):
    ruleWord = '000'
    ruleSet = {}
    for c in rule:
        ruleSet[ruleWord] = c
        ruleWord = cycle(ruleWord)
    return ruleSet

def zcycle(zpr, d):
    for i in range(len(zpr)):
        zpr[i] += 1
        if zpr[i] == d:
            zpr[i] = 0
    return zpr

def getNewLine(ruleDict, line, d):
    zpr = [d-1,0,1]
    newLine = ''
    for j in range(d):
        newLine += ruleDict[line[zpr[0]] + line[zpr[1]] + line[zpr[2]]]
        zpr = zcycle(zpr,d)
    return newLine

WIDTH, HEIGHT = 1367, 769

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

rr = randomRule(27)
d = WIDTH + 20
mid = int(d/2) + 1
line = '1' * d
line = line[0:mid] + '2' + line[mid+1:d]

#rr = '011222120101102021122002010'
#rr = '011000122121021012200122220'
#rr = '202001210120201102110010101'
#rr = '201100120211102220001110202'
#rr = '201100120211102220001110210' #hmmm
#rr = '201100120211102220001110211'
#rr = '201100120211102220001110212'
#rr = '201100120211102220001110220'
#rr = '201100120211102220001110221' #end hmmm
#rr = '000012111112022011100002021'
#rr = '120220120021020220022221012'
#rr = '011100122021201102222202122' #?
#rr = '020010102202011111120100020'
#rr = '002221202201212001211021110'
#rr = '022021221101220222212010022' #
#rr = '201201000011212221121101012' # last not commented
#rr = '022202120110101112111221000'
#rr = '122211212100100020121021221'
#rr = '211001100102210211120122022'
#rr = '210212022021010210100210121' #
#rr = '120101010012020000222002002' #
#rr = '011221002111102202200111110'
#rr = '010200200021112200202101220'
#rr = '200010202010002211001020102'
#rr = '220122122201001020002001221'
#rr = '221211202211101020122011001'
#rr = '221200122222020002001210210'
#rr = '002120111202101121112210211'
#rr = '201120110210201122212022221'
#rr = '002100110100200101111011201' #!s!#
#rr = '212121121112121121001002200'
#rr = '212202111201101220211202002' #pymd
#rr = '210122211101202101221202211' #line
#rr = '102012201001100110222111120' #line 2Cs
#rr = '201120100120112122012220021'
#rr = '221002101221110012200202201'
#rr = '102021201020000022222122000'
#rr = '201001201022111201022000012'
#rr = '222020220221121102212121110' #ghouls
#rr = '012202111220220201021111200' #hmmm no cliff
#rr = '102200022122020102202121110'


ruleDict = ruleDictionary(rr)

for y in range(HEIGHT+20):
    for x in range(WIDTH+20):
        #'''
        if line[x] == '0':
            img.put("#ff0000",(x,y))
            #img.put("#000000",(x,y))
        elif line[x] == '1':
            img.put("#00ff00",(x,y))
            #img.put("#000000",(x,y))
            #img.put("#777777",(x,y))
            #img.put("#ffffff",(x,y))
        else:
            img.put("#0000ff",(x,y))
            #img.put("#ffffff",(x,y))
        #'''
        '''
        if randrange(2):
            img.put('#000000',(x,y))
        else:
            img.put('#ffffff',(x,y))
        #'''
    line = getNewLine(ruleDict, line, d)

print(rulToDec(rr),": #rr = '" + rr + "'")
print('Completed in', time.time()-startTime, 'seconds')
'''
for x in range(4 * WIDTH):
    y = int(HEIGHT/2 + HEIGHT/4 * sin(x/80.0))
    img.put("#000000", (x//4,y))

for x in range(int(HEIGHT/2)):
    y = x
    img.put("#00ffff",(x,y))

for x in range(WIDTH):
    y = HEIGHT//2
'''

mainloop()
