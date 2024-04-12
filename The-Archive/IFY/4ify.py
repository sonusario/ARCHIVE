from copy import deepcopy as copy

'''
=======
Implemented
---
['(',')','@','->','~']
=======
'''

def Error(msg, flag=True):
    print("IFY> " + msg)
    return flag

def tokenize(rawtxt):
    t0 = rawtxt.replace('(', ' ( ').replace(')', ' ) ')
    t1 = t0.replace('@', ' @ ').replace('->', ' -> ').replace('~', ' ~ ')
    tokens = t1.split()
    return tokens

def listify(tokens, recFlag=False):
    program = []
    errFlag = False
    while len(tokens) > 0:
        token = tokens.pop(0)

        if token == '(':
            program.append(listify(tokens, True))
        elif token == ')':
            if recFlag:
                return program
            errFlag = Error("Unexpected ')'!")
            return [],errFlag
        else:
            program.append(token)
    if recFlag:
        errFlag = Error("Unexpected EOF. Expected more ')'s!")
        return [],errFlag
    
    return program, errFlag

def read():
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)
    return listify(tokenize(' '.join(content)))

#===============================================================================

def fn_replace(defined, fname):
    function = [fname]
    if fname in ['->','~']:
        return [],Error("Expected function name. Got " + fname)
    elif fname in defined:
        function = copy(defined[fname])
    return function,False

def verify(defined, input_spec, tokens):
    if tokens == []:
        return [],False,Error("Expected '->' or function name. Found NOTHING.")

    dupList = []
    for item in input_spec:
        if type(item) == type([]):
            return [],False,Error("Parameters cannot be of type LIST!")
        elif item in ['@','->','~']:
            return [],False,Error("'" + item +
                                  "' cannot be used as a parameter!")
        elif item in dupList:
            return [],False,Error("Error! Duplicate parameter name '" +
                                  item + "' found in parameter list.")
        else:
            dupList.append(item)

    fname = tokens.pop(0)
    callFlag = fname == '->'
    if not callFlag:
        if type(fname) == type([]):
            return [],False,Error("Expected function name. Got LIST")
        elif fname in ['@','->','~']:
            return [],False,Error("'" + fname +
                                  "' cannot be used as a function name!")
        
    if tokens == []:
        return [],False,Error("Expected output LIST. Found NOTHING.")

    output_spec = tokens.pop(0)
    if type(output_spec) != type([]):
        return [],False,Error("Expected output LIST. Got " + output_spec)

    if not callFlag:
        defined[fname] = [input_spec] + ['->'] + [output_spec]
    return output_spec,callFlag,False

def replace_params(input_spec, output_spec, vLUT, output_part):
    replacement_list = []
    for item in output_part:
        if type(item) == type([]):
            replacement_list.append(replace_params(input_spec,output_spec,
                                                   vLUT,item))
        elif item in vLUT:
            replacement_list.append(vLUT[item])
        elif item == '~':
            replacement_list += [input_spec] + ['->'] + [output_spec]
        else:
            replacement_list.append(item)
    return replacement_list

def fn_call(stack, input_spec, output_spec):
    pCount = len(input_spec)
    vals = []
    while len(vals) < pCount and len(stack) > 0:
        vals.insert(0,stack.pop(-1))
    if len(vals) != pCount:
        return vals,Error("Start of Stack error (SoS)! ", False)
    vLUT = {}
    for i in range(pCount):
        vLUT[input_spec[i]] = vals[i]
    output = replace_params(input_spec,output_spec,vLUT,output_spec)
    return output,False

def fn_handler(defined, stack, input_spec, tokens, callFlag):
    errFlag = False
    if not callFlag:
        output_spec,callFlag,errFlag = verify(defined,input_spec,tokens)
    else:
        tmp = tokens.pop(0)
        output_spec = tokens.pop(0)

    if errFlag:
        return [],errFlag
    elif not callFlag:
        return [],errFlag
    return fn_call(stack,input_spec,output_spec)

def prepender(pre_tokens,tokens):
    while len(pre_tokens) > 0:
        tokens.insert(0,pre_tokens.pop(-1))
    return

def evaluate(defined, stack, tokens):
    errFlag = False
    callFlag = False
    while len(tokens) > 0 and not errFlag:
        token = tokens.pop(0)
        if token == '@':
            if stack == []:
                errFlag = Error("Empty stack error. No function given to '@'!")
                continue
            else:
                prepend_tokens,errFlag = fn_replace(defined,stack.pop(-1))
                if errFlag: continue
                prepender(prepend_tokens,tokens)
                callFlag = True
        elif type(token) == type([]):
            prepend_tokens,errFlag = fn_handler(defined,stack,token,
                                                tokens,callFlag)
            prepender(prepend_tokens,tokens)
            callFlag = False
        else:
            stack.append(token)
            callFlag = False
    return {"defined":defined, "stack":stack, "errFlag":errFlag}

#===============================================================================

def format_stack(stack):
    txt = ""
    for item in stack:
        if type(item) == type([]):
            txt += '( '
            txt += format_stack(item)
            txt += ') '
        else:
            txt += item + ' '
    return txt

def repl():
    defined = {}
    stack = []
    while True:
        print("-------<<<INPUT>>>-------",
              " "*15, "(Write code, press Enter, then Ctrl-d)")
        program,errFlag = read()
        if errFlag: continue
        new_data = evaluate(copy(defined),copy(stack),program)
        if new_data["errFlag"]:
            continue
        else:
            defined = new_data["defined"]
            stack = new_data["stack"]
        print("-------<<<STACK>>>-------")
        print(format_stack(stack))
        print("\n\n\n")
    return

repl()
