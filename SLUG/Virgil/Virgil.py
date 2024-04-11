import random
import queue
import errno
import copy
import os
import re

userFolder = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__))) + '\\UserAccessibles'

def fndir_or_mkdir():
    try:
        os.makedirs(userFolder)
        return
    except:
        return

def fndFiles():
    global userFolder
    files = []
    for (dirpath, dirnames, filenames) in os.walk(userFolder):
        files.extend(filenames)
        break
    
    if len(files) == 0:
        return []
    return files

def copyFileList(files):
    global ufFiles
    ufFiles = copy.deepcopy(files)
    return

def updateFiles():
    copyFileList(fndFiles())
    return

def reStack():
    global deck
    global discardPile
    while discardPile.empty() == False:
        deck.append(discardPile.get_nowait())
    return

def randomSide():
    global card
    global fcSide
    
    if random.randrange(2):
        fcSide = 'wa'
        return card[0]
    fcSide = 'dq'
    return card[1]

def showCard():
    global pfcState
    global fcState
    global deck
    global card
    global fcSide
    global discardPile

    deckLen = len(deck)
    
    if deckLen == 0:
        if discardPile.empty():
            noDataMsg = '<empty deck, please load ' + fcState + ' with data>'
            fcState = pfcState
            if not(fcState == ''):
                start([fcState[0:len(fcState) - 4]])
            return noDataMsg
        reStack()
        deckLen = len(deck)
    
    rCard = random.randrange(deckLen)
    card = deck[rCard]
    discardPile.put_nowait(card)
    del deck[rCard]

    if fcOrder == 'random':
        return randomSide()
    elif fcOrder == 'qa':
        fcSide = 'dq'
        return 'q: ' + card[1]

    fcSide = 'wa'
    return 'a: ' + card[0]

def getCards():
    global deckFile
    global deck
    global discardPile
    
    dFile = deckFile.read()
    dLines = dFile.split('\n')

    deck = []
    discardPile = queue.Queue()
    
    for i in range(len(dLines)):
        splt = dLines[i].split(':|:')
        if len(splt) == 2:
            deck.append(splt)
        else:
            lineNumStr = str(i + 1)
            prnt('<error reading line ' + lineNumStr +' data>')
            prnt('<line ' + lineNumStr + ' will be skipped>\n')

    if deck == [['']]:
        deck = []
    return

def opFile(fname):
    global deckFile
    global deck
    deckFile = open(userFolder + '\\' + fname,'r+')
    getCards()
    deckFile.close()

    if len(deck) == 0:
        prnt('')
    elif not(len(deck[0]) == 2):
        fcDataReset()
        prnt('<Incorrect data format. File "'+ fname +'" will need a revision before use>\n')
    return

def fcDataReset():
    global ufFile
    global pfcState
    global fcState
    global fcSide
    global fcOrder
    global deckFile
    global deck
    global card
    global discardPile
    global pScore
    global totalScore
    global showedFC

    ufFiles = []
    updateFiles()

    pfcState = ''
    fcState = ''
    fcSide = 'dq'
    fcOrder = 'qa'

    deckFile = ''
    deck = []
    card = []
    discardPile = queue.Queue()

    pScore = 0
    totalScore = 0

    showedFC = False
    return

fndir_or_mkdir()

ufFiles = []
updateFiles()

pfcState = ''
fcState = ''
fcSide = 'dq' #dq, wa
fcOrder = 'qa' #qa, aq, random

deckFile = ''
deck = []
card = []
discardPile = queue.Queue()

pScore = 0
totalScore = 0

showedFC = False

def grade(statement):
    global pScore
    global totalScore
    cardScore = 0
    
    qaHolder = ''
    if fcSide == 'dq':
        qaHolder = card[0]
        prnt('a: ' + qaHolder + '\n')
    else:
        qaHolder = card[1]
        prnt('q: ' + qaHolder + '\n')
    
    qahLen = len(qaHolder)
    statLen = len(statement)
    minLen = 0
    longStr = ''
    shorStr = ''
    if statLen > qahLen:
        longStr = statement
        shorStr = qaHolder
        minLen = qahLen
    else:
        longStr = qaHolder
        shorStr = statement
        minLen = statLen

    for i in range(minLen):
        if qaHolder[i] == statement[i]:
            cardScore += 1
    pScore += qahLen
    totalScore += max((cardScore - abs(statLen - qahLen)),0)

running = True
exe = lambda statement: execute(statement)
glo = []
cmdList = {'help':[lambda args:hlp(args),
                   "'help' will print out a list of commands\n" +
                   "'help <command>' will describe what the command does\n"],
           'leave':[lambda args:leave(args),
                    "'leave' exits the program'\n"],
           'cls':[lambda args:cls(args),
                  "'cls' clears the current screen of text\n"],
           'dex':[lambda args:dex(args),
                    "'dex' prints index of files avalible\n"],
           'start':[lambda args:start(args),
                    "'start' <file> will run the flash card program on specified file\n"],
           'stop':[lambda args:stop(args),
                    "'stop' will exit currently running flash cards if it had been started"],
           'furl':[lambda args:furl(args),
                    "'furl' will print the file location accessible to the user via this program\n"]}

           #'change':[lambda args:change(args),
           #         "'change' <file> will allow addition or removal of flash cards from specified file\n"],
           #'mkf':[lambda args:mkf(args),
           #         "'mkf' <file> will create txt file if name is not already in use\n"],
           #'dlf':[lambda args:dlf(args),
           #         "'dlf' <file> will delete file if it exists\n"],

def execute(statement):
    if statement[0:6] != 'print(':
        pr = 'print(' + statement + ')'
    try:
        exec(pr)
        return ''
    except:
        return statement

def thereIsNoGloIn(statement):
    for obj in glo:
        if re.search(r'\b' + obj + r'\b', statement):
            return False
    return True

def removeSpaces(statement):
    stat = statement
    stat = ' ' + stat + ' '
    result = re.search('\s{2,}', stat)
    while result:
        a,b = result.span()
        c = len(stat)
        stat = stat[0:a] + ' ' + stat[b:c]
        result = re.search('\s{2,}', stat)
    stat = stat[1:len(stat)-1]
    return stat

def prnt(string):
    lines = string.split('\n')
    for line in lines:
        if len(line) == 0:
            print()
        else:
            print('  ' + line)
    return

def sprnt(string, spaceNum):
    lines = string.split('\n')
    for line in lines:
        if len(line) == 0:
            print()
        else:
            print('  ' + (' ' * spaceNum) + line)
    return

def hlp(args):
    argsLen = len(args)
    if argsLen == 0:
        print('=' * 21)
        print('COMMANDS')
        print('-' * 21)
        for key in cmdList:
            print(key)
        print('=' * 21)
        print()
    elif argsLen > 1:
        prnt('<to many arguments for help command>')
        prnt('<expected 1, got ' + str(argsLen) + '>\n')
    else:
        arg = args[0]
        if arg in cmdList:
            sprnt(cmdList[arg][1],4)
        else:
            prnt('<' + arg + ' not in list of commands>')
            prnt("<type 'help' for  a list of commands>\n")
    return

def leave(args):
    global running
    running = False
    fcDataReset()
    return

def cls(args):
    for i in range(100):
        print()
    return

def dex(args):
    files = fndFiles()

    if len(files) == 0:
        prnt("<hmmm... there's nothing here>\n")
        return
    for f in files:
        print(f[0:len(f)-4])

    copyFileList(files)
    return

def start(args):
    global pfcState
    global fcState
    global pScore
    global totalScore
    global showedFC

    showedFC = False
    
    updateFiles()
    argsLen = len(args)
    if argsLen == 1:
        arg = args[0] + '.txt'
        if arg in ufFiles:
            pfcState = fcState
            fcState = arg
            opFile(arg)
            pScore = 0
            totalScore = 0
        else:
            prnt('<the specified deck was not found>')
    else:
        prnt('<to many/few arguments for start command>')
        prnt('expected 1, got ' + str(argsLen) + '>\n')
    return

def stop(args):
    if(fcState == ''):
        prnt('<No flash cards currently running...>\n')
    fcDataReset()
    return

def furl(args):
    print(userFolder)
    return

def hub():
    global showedFC
    
    if fcState == '':
        iptPrompt = '> '
    else:
        iptPrompt = '# '
    statement = input(iptPrompt)
    statement = removeSpaces(statement)
    statLen = len(statement)
    seg = statement[0:2]
    cmdStr = statement.split(' ')

    fcResponse = False
    
    if cmdStr[0] in cmdList:
        cmdList[cmdStr[0]][0](cmdStr[1:len(cmdStr)])
    elif (not (fcState == '')) and (seg == 'q:' or seg == 'a:'):
        startOfQA = 2
        if len(statement) > 2:
            if statement[2] == ' ':
                startOfQA = 3
        if seg == 'a:' and fcSide == 'dq':
            grade(statement[startOfQA:statLen])
            fcResponse = True
            showedFC = False
        elif seg == 'q:' and fcSide == 'wa':
            grade(statement[startOfQA:statLen])
            fcResponse = True
            showedFC = False
        else:
            prnt('<wrong side of card indicated>')
    elif cmdStr[0] != '':
        if thereIsNoGloIn(statement):
            try:
                exec(exe(statement), globals())
            except:
                prnt('<statement not recognized or error occured>\n')
        else:
            prnt("<can't use pre-defined globals in statement>\n")

    if (not (fcState == '')) and ((not showedFC) or fcResponse):
        prnt(showCard())
        showedFC = True
    return

def Virgil():
    print()
    
    global running
    running = True
    
    while running:
        hub()
    #cls([])
    return

glo = [obj for obj in globals()]
Virgil()
