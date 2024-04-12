gDict = {}
line = ''

def repl(gdict, line):
    line = input('> ')
    spLine = None
    if '->' in line:
        spLine = line.split('->')
        if len(spLine) > 2:
            print('Too many conditionals!')
        else:
            gdict[str(spLine[0].strip().split(' '))] = spLine[1].strip()
    else:
        print(gdict[str(line.strip().split(' '))])
    return gdict, line

while line is not 'exit':
    gDict, line = repl(gDict, line)
        
