def add(a,b):
    return str(a + b)

def multi(a,b):
    c = 0
    for i in range(a):
        c = c + b
    return str(c)

def exp(a,b):
    c = 1
    for i in range(b):
        c = int(multi(c,a))
    return str(c)

def div(a,b):
    x = 0
    c = b
    if b < a:
        x = 1
    while c <= int(add(a,int(chr(45) + str(b)))):
        c = c + b
        x = x + 1
    if int(add(a,int(chr(45) + str(c)))) != 0:
        return 'Non' + chr(45) + 'integral answer'
    return str(x)

def lexer(charArr):
    charArrLen = len(charArr)
    numberStacks = [[],[]]
    signOpStack = ['','','']
    numFlag = False
    numFlag2 = False
    errorFlag = False
    errorMsg = ''
    stackIndex = 0
    for i in range(charArrLen):
        if i == 0 and not charArr[i].isdigit():
            signOpStack[0] = charArr[i]
        if charArr[i].isdigit() and stackIndex == 0:
            numFlag = True
            numberStacks[0].append(charArr[i])
        elif not charArr[i].isdigit() and numFlag:
            numFlag = False
            stackIndex = 1
            signOpStack[1] = charArr[i]
            if (i+1) < charArrLen:
                if not charArr[i+1].isdigit():
                    signOpStack[2] = charArr[i+1]
        elif charArr[i].isdigit() and stackIndex == 1:
            numFlag2 = True
            numberStacks[1].append(charArr[i])
        elif not charArr[i].isdigit() and numFlag2:
            stackIndex = 2
        elif charArr[i].isdigit() and stackIndex == 2 and not errorFlag:
            errorFlag = True
            errorMsg = 'Error: Too many integers entered in equation. '
            
    return [signOpStack, numberStacks, errorFlag, errorMsg]

def parser(tokArr):
    lexErrFlag = tokArr[2]
    errorMsg = tokArr[3]
    #print(tokArr)

    if not lexErrFlag:
        signOpStack = list(tokArr[0])
        numberStacks = list(tokArr[1])
        opErrFlag = False
        result = ''

        opArr = [chr(42),chr(43),chr(45),chr(47),chr(94)]
        for i in ''.join(signOpStack):
            if i not in opArr and not opErrFlag:
                opErrFlag = True
                errorMsg = errorMsg + 'Error: Invalid operator in equation. '

        if not opErrFlag:
            sign1 = signOpStack[0]
            op = signOpStack[1]
            sign2 = signOpStack[2]
            if op == '':
                opErrFlag = True
                errorMsg = errorMsg + 'Error: Missing operator in equation. '
            if sign1 != chr(45) and sign1 != '':
                opErrFlag = True
                errorMsg = errorMsg + 'Error: Invalid sign(s) for integers. '
            if sign2 != chr(45) and sign2 != '':
                opErrFlag = True
                errorMsg = errorMsg + 'Error: Invalid sign(s) for integers. '
            if not opErrFlag:
                if op == chr(43) or op == chr(45):
                    a = int(sign1 + ''.join(numberStacks[0]))
                    if op == chr(45) and sign2 == chr(45):
                        b = int(''.join(numberStacks[1]))
                    else:
                        b = int(op + ''.join(numberStacks[1]))
                    result = add(a,b)
                else:
                    a = int(''.join(numberStacks[0]))
                    b = int(''.join(numberStacks[1]))
                    if op == chr(42):
                        hold = multi(a,b)
                        if sign1 == chr(45) and sign2 != chr(45):
                            result = chr(45) + hold
                        elif sign2 == chr(45) and sign1 != chr(45):
                            result = chr(45) + hold
                        else:
                            result = hold
                    elif op == chr(47):
                        if b == 0:
                            hold = 'Not' + chr(45) + 'defined'
                        else:
                            hold = div(a,b)
                        if hold.isdigit():
                            if sign1 == chr(45) and sign2 != chr(45):
                                result = chr(45) + hold
                            elif sign2 == chr(45) and sign1 != chr(45):
                                result = chr(45) + hold
                            else:
                                result = hold
                        else:
                            result = hold
                    elif op == chr(94):
                        if sign2 == chr(45):
                            result = 'Non' + chr(45) + 'integral answer'
                        else:
                            hold = exp(a,b)
                            if sign1 == chr(45) and not div(b,2).isdigit():
                                result = chr(45) + hold
                            else:
                                result = hold
            else:
                result = errorMsg
        else:
            result = errorMsg
    else:
        result = errorMsg
    return result

def calc(formula):
    result = parser(lexer(formula))
    if not 'Error: ' in result:
        return formula + ' = ' + result
    
    return result

testArr = ['12+25',
           '-30+100',
           '100-30',
           '100--30',
           '-25-29',
           '-41--10',
           '9*3',
           '9*-4',
           '-4*8',
           '-12*-9',
           '100/2',
           '75/-3',
           '-75/3',
           '7/3',
           '0/0',
           '5^3',
           '-5^3',
           '-8^3',
           '-1^1',
           '1^1',
           '0^5',
           '5^0',
           '10^-3',
           '-5^2']

for i in testArr:
    print(calc(i))
