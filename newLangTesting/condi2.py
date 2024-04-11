import re
gDict = {'+': [2, lambda a,b: a+b]}
line = ''

def repl(gdict, line):
    line = input('> ')
    conLine = None
    acnLine = line.strip().split()
    if '->' in line:
        conLine = line.split('->')
        if len(conLine) > 2:
            print('Too many conditionals!')
        else:
            gdict[str(conLine[0].strip().split(' '))] = conLine[1].strip()
    elif str(acnLine) in gdict:
        print(gdict[str(line.strip().split(' '))])
    return gdict, line



def run(gDict, line):
    while line != 'exit':
        gDict, line = repl(gDict, line)

run(gDict, line)
line = ''
