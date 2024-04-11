from copy import deepcopy as copy
defined = {}
def tokenize(rawtxt):
    t0 = rawtxt.replace('@', ' @ ').replace('$', ' $ ').replace('->', ' -> ')
    t1 = t0.replace('(', ' ( ').replace(')', ' ) ')
    tokens = t1.split()
    return tokens
def listify(tokens, recFlag=False):
    program = []
    if len(tokens) == 0 and recFlag:
        raise SyntaxError("Ratify> Unexpected EOF. Expected more ')'s")    
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token == '(':
            program.append(listify(tokens, True))
        elif token == ')':
            if recFlag:
                return program
            raise SyntaxError("Ratify> Unexpected ')'.")
        else:
            program.append(token)
    return program
def read():
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)
    return listify(tokenize(' '.join(content)))
def raise_NotEnoughData_error(n):
    missing_txt = ["Missing CONDITION_AND_OUTPUT LIST(s)",
                   "Missing FUNCTION NAME",
                   "Missing VAR LIST"]
    err_txt = ""
    for i in range(3-n):
        err_txt = missing_txt[i] + ". " + err_txt
    raise SyntaxError("Ratify> Error with definition spec. " + err_txt)
def check_params(tokens, dup_ledger, recFlag=False):
    if type(tokens) != type([]):
        raise SyntaxError("Ratify> Expected VAR LIST. " +
                          "Found '" + tokens + "'.")
    elif tokens == [] and recFlag:
        raise SyntaxError("Ratify> Empty list parameters are not allowed.")    
    for token in tokens:
        if token in ['@','$','->']:
            raise SyntaxError("Ratify> Error! '" + token +
                              "' is not a valid parameter name.")
        elif type(token) == type([]):
            check_params(token, dup_ledger, True)
        elif token in dup_ledger:
            raise SyntaxError("Ratify> Error! Duplicate parameter " +
                              "name '" + token + "' found in VAR LIST.")
        else:
            dup_ledger.append(token)
    return tokens
def check_fname(token):
    if type(token) == type([]):
        raise SyntaxError("Ratify> Expected FUNCTION NAME. " +
                          "Found list.")
    elif token in ['@','$']:
        raise SyntaxError("Ratify> Expected FUNCTION NAME. "
                          "Found '" + token + "'.")
    return token    
def check_condouts(tokens):
    condouts = []
    for token in tokens:
        if type(token) != type([]):
            raise SyntaxError("Ratify> Expected " +
                              "CONDITION_AND_OUPUT LIST. " +
                              "Found '" + token + "'.")
        elif token == [] or '->' not in token:
            token.insert(0, '->')

        condouts.append({"cond":token[:token.index('->')],
                         "out" :token[token.index('->')+1:]})
    return condouts
def verified(function):
    params = check_params(function[0], [])
    fname = check_fname(function[1])
    condouts = check_condouts(function[2:])
    return {"params":params, "fname":fname, "condouts":condouts}
def define(function):
    global defined
    
    if type(function) != type([]):
            raise SyntaxError("Ratify> Expected definition structured " +
                          "LIST Found '" + str(token) + "'.")
    elif len(function) < 3:
        raise_NotEnoughData_error(len(function))
    elif function[1] == '->':
        return True, verified(function)    
    fn = verified(function)
    defined[fn["fname"]] = fn
    return False, []
def build_LUT(values, params, LUT, recFlag=False):
    v = copy(values)
    p = copy(params)
    while len(v) < len(p):
        v.append('')
    while len(p) > 0:
        vel = v.pop(0)
        pel = p.pop(0)
        if type(pel) == type([]):
            if vel == '': vel = []
            elif len(p) == 1 and recFlag and len(params) > 2:
                if type(vel) != type([]):
                    vel = [vel]
                while len(v) > 1:
                    vel.append(v.pop(0))
            elif type(vel) != type([]): vel = [vel]
            build_LUT(vel,pel,LUT,True)
        elif len(p) == 1 and recFlag and len(params) > 2:
            vstuff = []
            while len(v) > 1:
                vstuff.append(v.pop(0))                
            if vel == '':
                LUT[pel] = vstuff
            else:
                LUT[pel] = [vel] + vstuff
        elif len(p) < 1 and recFlag:
            if vel == '':
                LUT[pel] = v
            else:
                LUT[pel] = [vel] + v
        else:
            if vel == '':
                LUT[pel] = []
            else:
                LUT[pel] = [vel]
    return
def replace_params(val_LUT, param_filled_list):#
    vLUT = copy(val_LUT)
    pfL = copy(param_filled_list)
    replacement_list = []
    while len(pfL) > 0:
        PF = pfL.pop(0)
        if type(PF) == type([]):
            replacement_list.append(replace_params(vLUT, PF))
        elif PF in vLUT:
            for element in vLUT[PF]:
                replacement_list.append(copy(element))
        else:
            replacement_list.append(PF)
    return replacement_list
def look_for_match(vals, vLUT, condouts, vCount):
    there_is_a_match = False
    while there_is_a_match is False and len(condouts) > 0:
        condout = condouts.pop(0)
        cond_list = condout["cond"]
        cond_count = len(cond_list)
        if cond_count == 0:
            there_is_a_match = True
            continue
        elif cond_count > vCount: #Helps handle input shortage
            for i in range(cond_count - vCount):
                vals.append('')
        match_list = replace_params(vLUT, cond_list)
        match_list = evaluate([],match_list)
        match_count = len(match_list)
        if match_count > 0 and match_count != vCount:
            raise SyntaxError("Ratify> Number of items in " +
                              str(match_list) + " is not zero and does " +
                              "not match the number of parameters in the " +
                              "parameter list [" + str(vCount) + "].")
        match_flag = True
        if match_count == 0:
            match_flag = False
        for i in range(match_count):
            if vals[i] != match_list[i]:
                match_flag = False
        if match_flag:
            there_is_a_match = True
    return there_is_a_match, condout["out"]
def call(tokens, fname):
    global defined
    function = {"params":[], "fname":'->', "condouts":[{"cond":[],"out":[]}]}
    if type(fname) == type([]):
        return [evaluate([],fname)]
    elif fname == '$':
        if len(tokens) == 0:
            raise SyntaxError("Ratify> Expected definition structured " +
                              "LIST. Found NOTHING.")
        function_is_anon, function = define(tokens.pop(-1))
        if not function_is_anon: return []
    elif fname in defined:
        function = copy(defined[fname])
    else:
        return [fname]
    params = function["params"]
    condouts = function["condouts"]
    pCount = len(params)
    values = []
    counter = 0
    while len(tokens) > 0 and counter < pCount:
        values.insert(0, tokens.pop(-1))
        counter += 1
    vCount = len(values)
    vLUT = {}
    build_LUT(values, params, vLUT)
    there_is_a_match, out_list = look_for_match(values, vLUT, condouts, vCount)
    output = []
    if there_is_a_match:
        output = replace_params(vLUT, out_list)
    return output
def evaluate(stack, tokens):
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token == '@':
            if stack == []: continue
            prepend_tokens = call(stack, stack.pop(-1))
            while len(prepend_tokens) > 0:
                tokens.insert(0, prepend_tokens.pop(-1))
        else:
            stack.append(token)
    return stack
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
    g_stack = []
    while True:
        print("-------<<<INPUT>>>-------",
              " "*15, "(Write code, press Enter, then Ctrl-d)")
        program = read()
        g_stack = evaluate(copy(g_stack), program)
        print("-------<<<STACK>>>-------")
        print(format_stack(g_stack))
        print("\n\n\n")
    return
repl()

'''
note: "exec" is not "eval"
from inspect import signature
len(signature(lambda x,y: x).parameters)
'''
