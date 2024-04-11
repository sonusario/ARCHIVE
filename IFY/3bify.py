from copy import deepcopy as copy

'''
=======
Implemented
---
['(',')','@','->']
=======
'''

def Error(msg, flag=True):
    print("IFY> " + msg)
    return flag

def tokenize(rawtxt):
    t0 = rawtxt.replace('(', ' ( ').replace(')', ' ) ')
    t1 = t0.replace('@', ' @ ').replace('->', ' -> ')
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

def fn_define(defined,fokens):
    if len(fokens) != 3:
        return [],Error("Invalid function specification! Expected 3 items, " +
                        "(parameter[s]), function name or '->', (output[s]) " +
                        ", but got " + str(len(fokens)) + " items.")
    input_spec = fokens.pop(0)
    dupList = []
    for item in input_spec:
        if type(item) != type("str"):
            return [],Error("Parameters cannot be of type "+str(type(item))+"!")
        elif item in ['@','->']: # '~'
            return [],Error("'" + item + "' cannot be used as a parameter!")
        elif item in dupList:
            return [],Error("Error! Duplicate parameter name '" + item +
                            "' found in parameter list.")
        else:
            dupList.append(item)

    fname = fokens.pop(0)
    if type(fname) != type("str"):
        return [],Error("Expected function name or '->'. Got " +
                        str(type(fname)) + ".")
    elif fname in ['@']: # '~'
        return [],Error("'" + fname + "' cannot be used as a function name!")

    output_spec = fokens.pop(0)
    if type(output_spec) != type([]):
        return [],Error("Expected output LIST. Got " + output_spec)

    function = {"input_spec":input_spec,"fname":fname,"output_spec":output_spec}

    if fname == '->':
        return [function],False
    else:
        defined[fname] = function
        return [],False
    
def replace_params(function, vLUT, output_spec):
    replacement_list = []
    for item in output_spec:
        if type(item) == type([]):
            replacement_list.append(replace_params(function,vLUT,item))
        elif item in vLUT:
            replacement_list.append(vLUT[item])
            #elif item == '~': replacement_list += function
        else:
            replacement_list.append(item)
    return replacement_list

def fn_call(defined,stack):
    if stack == []:
        return [],Error("Empty call error! No function given to '@'!")

    function = stack.pop(-1)

    if type(function) != type({}):
        if function in defined:
            function = copy(defined[function])
        else:
            return [function],False

    pCount = len(function["input_spec"])
    vals = []
    while len(vals) < pCount and len(stack) > 0:
        vals.insert(0,stack.pop(-1))
    if len(vals) != pCount:
        return vals,Error("Start of Stack error (SoS)!", False)
    vLUT = {}
    for i in range(pCount):
        vLUT[function["input_spec"][i]] = vals[i]
    output = replace_params(function,vLUT,function["output_spec"])
    return output,False

def pender(pend_tokens, tokens, append_code):
    while len(pend_tokens) > 0:
        if append_code == "append":
            tokens.append(pend_tokens.pop(0))
        elif append_code == "prepend":
            tokens.insert(0,pend_tokens.pop(-1))
    return

def evaluate(defined, stack, tokens):
    errFlag = False
    while len(tokens) > 0 and not errFlag:
        token = tokens.pop(0)
        
        if token == '@':
            #print(format_stack(["IFY>"] + stack)) #debugger ;)
            prepend_tokens,errFlag = fn_call(defined,stack)
            if errFlag: continue
            pender(prepend_tokens,tokens,"prepend")
        elif type(token) == type([]):
            append_tokens,errFlag = fn_define(defined,token)
            if errFlag: continue
            pender(append_tokens,stack,"append")
        else:
            stack.append(token)
    return {"defined":defined, "stack":stack, "errFlag":errFlag}

#===============================================================================

def format_stack(stack):
    txt = ""
    for item in stack:
        if type(item) == type([]):
            txt += '( '
            txt += format_stack(item)
            txt += ') '
        elif type(item) != type("str"):
            txt += "<anon_fn> "
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
