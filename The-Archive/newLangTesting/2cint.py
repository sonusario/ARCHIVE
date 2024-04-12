import re

def isInt(chars):
    out = re.sub('(-0*[1-9])?\d+', 'INT', chars)
    return out == "INT"

def is2cInt(chars):
    out = re.sub('(0|9)\d+', '2CINT', chars)
    return out == "2CINT"

CL = ['0','1','2','3','4','5','6','7','8','9']

flipKey = {CL[0]:CL[9],
           CL[1]:CL[8],
           CL[2]:CL[7],
           CL[3]:CL[6],
           CL[4]:CL[5],
           CL[5]:CL[4],
           CL[6]:CL[3],
           CL[7]:CL[2],
           CL[8]:CL[1],
           CL[9]:CL[0],
           '-':'-'}

incFlipKey = {CL[0]:CL[0],
              CL[1]:CL[9],
              CL[2]:CL[8],
              CL[3]:CL[7],
              CL[4]:CL[6],
              CL[5]:CL[5],
              CL[6]:CL[4],
              CL[7]:CL[3],
              CL[8]:CL[2],
              CL[9]:CL[1]}

'''
flipKey = {'0':'9','1':'8','2':'7','3':'6','4':'5',
           '5':'4','6':'3','7':'2','8':'1','9':'0'}

incflipKey = {'0':'0','1':'9','2':'8','3':'7','4':'6',
              '5':'5','6':'4','7':'3','8':'2','9':'1'}
#'''

def intTo2Cint(chars):
    print(chars, ':', end='')
    pF = 0
    pL = len(chars) - 1
    gR = chars[1:pL]
    st = 0
    out = ''
    d = pL + 1
    count = 0
    while count < d:
        '''
        print('d', d)
        print('st', st)
        print('pL', pL)
        print('chars', chars)
        print('gR', gR)
        print('out', out)
        print('count', count)
        #'''
        if st == 0:
            if chars[pF] == '-':
                chars = CL[0] + gR + chars[pL]
                gR = chars[:pL]
                st = 1
            else:
                chars = CL[0] + chars
                d += 1
                pL += 1
                gR = chars[:pL]
                st = 4
        elif st == 1:
            if chars[pL] == CL[0]:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gR = chars[:pL]
                st = 2
            else:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gR = chars[:pL]
                st = 3
        elif st == 2:
            if chars[pL] == CL[0]:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gr = chars[:pL]
            else:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gR = chars[:pL]
                st = 3
        elif st == 3:
            out = flipKey[chars[pL]] + out
            count += 1
            pL -= 1
            chars = gR
            gR = chars[:pL]
        elif st == 4:
            out = chars[pL] + out
            count += 1
            pL -= 1
            chars = gR
            gR = chars[:pL]
    return out

def C2intToInt(chars):
    print(chars, ':', end='')
    pF = 0
    pL = len(chars) - 1
    gR = chars[1:pL]
    st = 0
    out = ''
    d = pL + 1
    count = 0
    while count < d:
        '''
        print('d', d)
        print('st', st)
        print('pL', pL)
        print('chars', chars)
        print('gR', gR)
        print('out', out)
        print('count', count)
        #'''
        if st == 0:
            if chars[pF] == '9':
                chars = '-' + gR + chars[pL]
                gR = chars[:pL]
                st = 1
            else:
                #chars = CL[0] + chars
                #d += 1
                #pL += 1
                gR = chars[:pL]
                st = 4
        elif st == 1:
            if chars[pL] == CL[0]:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gR = chars[:pL]
                st = 2
            else:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gR = chars[:pL]
                st = 3
        elif st == 2:
            if chars[pL] == CL[0]:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gr = chars[:pL]
            else:
                out = incFlipKey[chars[pL]] + out
                count += 1
                pL -= 1
                chars = gR
                gR = chars[:pL]
                st = 3
        elif st == 3:
            out = flipKey[chars[pL]] + out
            count += 1
            pL -= 1
            chars = gR
            gR = chars[:pL]
        elif st == 4:
            out = chars[pL] + out
            count += 1
            pL -= 1
            chars = gR
            gR = chars[:pL]
    return out

#'''
for i in range(-25,26):
    print('', intTo2Cint(str(i)))
#'''
print('='*42)
#'''
for i in range(91,100):
    print('', C2intToInt(str(i)))
#'''
print('='*42)
#'''
for i in range(0,10):
    print('', C2intToInt('0' + str(i)))
#'''    

#print('', intTo2Cint('10'))
