import re

s = 'ba baka ka ka ka ka ka ka ka ka ka baba ba bayaro yaro baba bakayaro ba ba ba ba ba ba ba ba ba ba ba bakayaro ba bakayaro ba ba ba ba ba ba ba ba ba ba ba bakayaro ba ba ba ba ba ba ba ba ba ba bakayaro baka ka ka baba ba bayaro yaro baba bakayaro ka baka ka baba ba ba bayaro yaro baba ka bakayaro ba baka ka ka baba ba bayaro yaro baba ba ba ba ba bakayaro ka ka ka baka ka baba ba ba bayaro yaro baba bakayaro ka baka ka ka ka ka ka baba ba bayaro yaro baba bakayaro baba ka baka ka ka ka baba ba bayaro yaro baba ka bakayaro baka ka ka baba ba bayaro yaro baba ba ba ba bakayaro ba baka ka ka baba ba ba ba bayaro yaro baba ba ba bakayaro ba bakayaro baba ba baka ka ka ka baba ba ba bayaro yaro baba ba ba bakayaro baba ka baka ka ka ka ka ka ka ka baba ba bayaro yaro baba bakayaro ba ba baka ka ka ka baba ba ba bayaro yaro baba bakayaro'
sarr = s.split(' ')
sict = {}

for word in sarr:
    if word in sict:
        sict[word] += 1
    else:
        sict[word] = 1

tics = {'ka': '-', 'baka': '[', 'bakayaro': '.', 'yaro': ']',
        'ba': '+', 'bayaro': '<', 'baba': '>'}

def convert(arr):
    out = ''
    for word in arr:
        out += tics[word]
    return out

x = convert(sarr)

print(sict)
print(x)
