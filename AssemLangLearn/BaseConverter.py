#Binary, Balanced Ternary, Octal, Decimal, Hexadecimal, Balanced Heptavigesimal

hepDict = {
        'A': -13,
        'B': -12,
        'C': -11,
        'D': -10,
        'E': -9,
        'F': -8,
        'G': -7,
        'H': -6,
        'I': -5,
        'J': -4,
        'K': -3,
        'L': -2,
        'M': -1,
        '0': 0,
        'N': 1,
        'O': 2,
        'P': 3,
        'Q': 4,
        'R': 5,
        'S': 6,
        'T': 7,
        'U': 8,
        'V': 9,
        'W': 10,
        'X': 11,
        'Y': 12,
        'Z': 13
    }

hexDict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

decDict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

octDict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7
    }

terDict = {
        'M': -1,
        '0': 0,
        'N': 1
    }

binDict = {
        '0': 0,
        '1': 1
    }

dictList = [0]*30
dictList[2] = binDict
dictList[3] = terDict
dictList[8] = octDict
dictList[10] = decDict
dictList[16] = hexDict
dictList[27] = hepDict

def b2b(num, fr, to):
    numLen = len(num)-1
    dec = 0
    for i in range(numLen+1):
        dec += dictList[fr][num[i]]*(fr**(numLen-i))
    negFlag = dec < 0
    
    return dec
