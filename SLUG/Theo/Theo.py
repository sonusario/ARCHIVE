running = True
import re

def removeSpaces(statement):
    stat = statement
    stat = ' ' + stat + ' '
    result = re.search('\s{2,}', stat)
    while result:
        a,b = result.span()
        c = len(stat)
        stat = stat[0:a] + ' ' + stat[b:c]
        result = re.search('\s{2,}', stat)
    stat = stat[1:len(stat) - 1]
    return stat

def converse():
    qMent = input('> ')
    qMent = removeSpaces(qMent)
    print(' ', qMent)
    return

def Theo():

    global running
    running = True
    
    while running:
        converse()
    return

Theo()
