from random import randrange
import re

def getRandNumCyph():
    numChars = ['0','1','2','3','4','5','6','7','8','9','-','.',' ']
    x = {}
    s = ''

def getRandAlphaCyph():
    x = {}
    y = {}
    s = ''
    for i in range(26):
        c = chr(i + 65)
        y[c] = []
        count = 0
        while count < 4:
            s = "{:0>2d}".format(randrange(-4,100))
            if s not in x:
                x[s] = c
                y[c].append(s)
                count += 1
    return x, y

def decode(message, decoder):
    message = message.split(' ')
    decoded = ''
    for c in message:
        if not (c == ''): decoded += decoder[c]
    return decoded

def encode(message, encoder):
    encoded = ''
    message = re.sub(' +', ' ', message)
    for c in message:
        if c == ' ':
            encoded += ' '
        else:
            encoded += encoder[c][randrange(len(encoder[c]))] + ' '
    return encoded

def cyPrint(cypher):
    for k in list(cypher.keys()):
        print(k, cypher[k])
    return

alphaDecoder, alphaEncoder = getRandAlphaCyph()


