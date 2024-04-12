from copy import deepcopy as copy
import re

'''
=======
Implemented
---
['@','->','->->']
=======
'''

def Error(msg):
    print("IFY> " + msg)
    return True

def tokenize(rawtxt):
    t0 = rawtxt.replace('@', ' @ ').replace('->', ' -> ')
    t1 = re.sub(r"->\s+->", "->->", t0)
    t2 = t1.replace('(', ' ( ').replace(')', ' ) ')
    tokens = t2.split()
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

def fn_replace(defined, fname):
    function = [fname]
    if type(fname) == type([]):
        return [],Error("Expected function name. Got LIST")
    elif fname in ['@','->','->->']:
        return [],Error("Expected function name. Got " + fname)
    elif fname in defined:
        function = copy(defined[fname])
    return function,False

def fn_define(defined,args,tokens):
    if type(args) != type([]):
        return Error("Expected argument LIST. Got " + args)
    elif tokens == []:
        return Error("Expected function name. Found NOTHING.")
    fname = tokens.pop(0)
    if type(fname) == type([]):
        return Error("Expected function name. Got LIST")
    elif fname in ['@','->']:
        return Error("Expected function name. Got " + fname)
    elif tokens == []:
        return Error("Expected ->. Found NOTHING.")
    tmp = tokens.pop(0)
    if tmp != '->':
        return Error("Expected ->. Got " + str(tmp))
    elif tokens == []:
        return Error("Expected output LIST. Found NOTHING.")
    output = tokens.pop(0)
    if type(output) != type([]):
        return Error("Expected output LIST. Got " + output)

    for item in args:
        if type(item) == type([]):
            return Error("Parameters cannot be of type LIST!")
        elif item in ['@','->','->->']:
            return Error("'" + item  + "' cannot be used as a parameter!")
    defined[fname] = [args] + ['->->'] + [output]
    return False

def replace_params(vLUT, param_output):
    replacement_list = []
    for item in param_output:
        if type(item) == type([]):
            replacement_list.append(replace_params(vLUT,item))
        elif item in vLUT:
            replacement_list.append(vLUT[item])
        else:
            replacement_list.append(item)
    return replacement_list

def fn_call(stack,args,param_output):
    if type(args) != type([]):
        return [],Error("Expected argument LIST. Got " + args)
    elif type(param_output) != type([]):
        return [],Error("Expected output LIST. Got " + param_output)

    pCount = len(args)
    vals = []
    cnt = 0
    while len(vals) < pCount and len(stack) > 0:
        vals.insert(0,stack.pop(-1))
        if type(args[cnt]) == type([]):
            return [],Error("Parameters cannot be of type LIST!")
        cnt += 1
    if len(vals) != pCount:
        return [],Error("Not enough values for function. Expected " +
                        str(pCount) + ". Got " + str(len(vals)) + ".")
    vLUT = {}
    for i in range(pCount):
        vLUT[args[i]] = vals[i]
    output = replace_params(vLUT,param_output)
    return output,False

def evaluate(defined, stack, tokens):
    errFlag = False
    while len(tokens) > 0 and not errFlag:
        token = tokens.pop(0)
        if token == '@':
            if stack == []:
                errFlag = Error("No function given to '@'!")
                continue
            prepend_tokens,errFlag = fn_replace(defined,stack.pop(-1))
            if errFlag: continue
            while len(prepend_tokens) > 0:
                tokens.insert(0, prepend_tokens.pop(-1))
        elif token == '->':
            if stack == []:
                errFlag = Error("No args given for define!")
                continue
            errFlag = fn_define(defined,stack.pop(-1),tokens)
        elif token == '->->':
            if stack == [] or tokens == []:
                errFlag = Error("Either no args, or no output was given to '->->'!")
                continue
            prepend_tokens,errFlag = fn_call(stack,stack.pop(-1),tokens.pop(0))
            if errFlag: continue
            while len(prepend_tokens) > 0:
                tokens.insert(0, prepend_tokens.pop(-1))
        else:
            stack.append(token)
    return {"defined":defined, "stack":stack, "errFlag":errFlag}

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
        new_data = evaluate(copy(defined),copy(stack), program)
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
