from copy import deepcopy as copy

'''
=======
Implemented
---
@ $ -> ( )
=======
'''

stack = []
defined = {}

def tokenize(program):
    global stack
    t0 = program.replace('@', ' @ ').replace('$', ' $ ').replace('->', ' -> ')
    t1 = t0.replace('(', ' ( ').replace(')', ' ) ')
    tokens = stack + t1.split()
    return tokens

#========================================

def raise_NotEnoughData_error(n):
    missing_txt = ["Missing CONDITION_AND_OUTPUT LIST(s)",
                   "Missing FUNCTION NAME",
                   "Missing VAR LIST"]
    err_txt = ""
    for i in range(3-n):
        err_txt = missing_txt[i] + ". " + err_txt
    raise SyntaxError("Ratify> Error with definition spec. " + err_txt)

def gen_param_list(tokens, dup_ledger, recFlag=False):
    param_list = []

    if type(tokens) != type([]):
        raise SyntaxError("Ratify> Expected VAR LIST. " +
                          "Found '" + tokens + "'.")
    elif tokens == [] and recFlag:
        raise SyntaxError("Ratify> Empty list parameters are not allowed.")

    while len(tokens) > 0:
        token = tokens.pop(0)
        if token in ['@','$','->']:
            raise SyntaxError("Ratify> Error! '" +
                              token + "' is not a valid parameter name.")
        elif type(token) == type([]):
            param_list.append(gen_param_list(token, dup_ledger, True))
        elif token in dup_ledger:
            raise SyntaxError("Ratify> Error! Duplicate parameter name '" +
                              token + "' found in VAR LIST.")
        else:
            param_list.append(token)
            dup_ledger.append(token)
    return param_list

def get_func_name(token):
    if type(token) == type([]):
        raise SyntaxError("Ratify> Expected FUNCTION NAME. " +
                          "Found list.")
    elif token in ['@','$','->']:
        raise SyntaxError("Ratify> Expected FUNCTION NAME. "
                          "Found '" + token + "'.")
    return token

def get_cond(tokens, recFlag=False):
    cond = []
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token == '->' and not recFlag:
            return cond
        elif token == '@' and not recFlag:
            raise SyntaxError("Ratify> Expected MATCH condition" +
                              "or '->'. Found '@'.")
        cond.append(token)
    raise SyntaxError("Ratify> How did you get here!? (PyCode: get_cond)")

def get_output(tokens):
    out = []
    while len(tokens) > 0:
        token = tokens.pop(0)
        out.append(token)
    return out

def get_condout_lists(tokens, num_of_params):
    condouts = []
    while len(tokens) > 0: #Each iteration covers a new condout list
        token = tokens.pop(0)

        if type(token) != type([]):
            raise SyntaxError("Ratify> Expected " +
                              "CONDITION_AND_OUPUT LIST. " +
                              "Found '" + token + "'.")
        elif token == [] or '->' not in token:
            raise SyntaxError("Ratify> Expected [OPTIONAL CONDITION" +
                              "(s) -> OPTIONAL OUTPUT(s)].  Either no '->' " +
                              "was given or an empty list was given.")

        condout = {}
        condout["cond"] = get_cond(token)
        condout["out"] = get_output(token)

        cond_len = len(condout["cond"])
        if cond_len > 0 and cond_len != num_of_params:
            raise SyntaxError("Ratify> Number of items in " +
                              str(condout["cond"]) + " is not zero and does " +
                              "not match the number of parameters in the " +
                              "parameter list [" + str(num_of_params) + "].")
        condouts.append(condout)
    return condouts

def define(tokens):
    global defined

    if type(tokens) != type([]):
        raise SyntaxError("Ratify> Expected definition structured " +
                          "LIST Found '" + str(tokens) + "'.")
    elif len(tokens) < 3:
        raise_NotEnoughData_error(len(tokens))

    token = tokens.pop(0)
    param_list = gen_param_list(token,[]) #[] for duplicated params

    token = tokens.pop(0)
    function_name = get_func_name(token)

    conds_and_outs = get_condout_lists(tokens, len(param_list))

    defined[function_name] = {"params":param_list,"condouts":conds_and_outs}
    return

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
            elif type(vel) != type([]): vel = [vel]
            build_LUT(vel,pel,LUT,True)
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

def look_for_match(vals, vLUT, condout_lists, vCount):
    there_is_a_match = False
    while there_is_a_match is False and len(condout_lists) > 0:
        condout = condout_lists.pop(0)

        cond_list = condout["cond"]
        cond_count = len(cond_list)
        if cond_count == 0:
            there_is_a_match = True
            continue
        elif cond_count > vCount: #Helps handle input shortage
            for i in range(cond_count - vCount):
                vals.append('')
                
        match_list = replace_params(vLUT, cond_list)
        match_count = len(match_list)
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

    if type(fname) == type([]):
        return [read_from_tokens(fname)]
    elif fname == '$':
        if len(tokens) == 0:
            raise SyntaxError("Ratify> Expected definition structured " +
                              "LIST. Found NOTHING.")
        define(tokens.pop(-1))
        return []
    elif fname not in defined:
        return [fname]

    param_list = copy(defined[fname]["params"])
    condout_lists = copy(defined[fname]["condouts"])
    par_count = len(param_list)

    values = []
    counter = 0
    while len(tokens) > 0 and counter < par_count:
        values.append(tokens.pop(-1))
        counter += 1
    values.reverse()
    val_count = len(values)

    val_LUT = {}
    build_LUT(values,param_list,val_LUT)

    there_is_a_match, output_list = look_for_match(values,
                                                   val_LUT,
                                                   condout_lists,
                                                   val_count)
    output = []
    if there_is_a_match:
        output = replace_params(val_LUT, output_list)
    return output

def read_from_tokens(tokens, recFlag=False, lstTokenFlag=False):
    STACK = []

    while len(tokens) > 0:
        #print(format_stack(["Ratify>"] + tokens))
        token = tokens.pop(0)
        if token == '(':
            STACK.append(read_from_tokens(tokens, True))
        elif type(token) == type([]):
            STACK.append(read_from_tokens(token, True, True))
        elif token == ')':
            if recFlag:
                return STACK
            else:
                raise SyntaxError("Ratify> Unexpected ')'.")
        elif token == '@' and not recFlag:
            if STACK == []: continue #Nothing to run if stack is empty
            prepend_tokens = call(STACK,STACK.pop(-1))
            while len(prepend_tokens) > 0: #Add items produced by function
                tokens.insert(0,prepend_tokens.pop(-1))
        else:
            STACK.append(token)

    if recFlag and not lstTokenFlag:
        raise SyntaxError("Ratify> Unexpected EOF. Expected more ')'s")
    return STACK

#========================================

def parse(program):
    return read_from_tokens(tokenize(program))

def get_program():
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)
    return ' '.join(content)

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
    global stack
    while True:
        print("-------<<<INPUT>>>-------",
              " "*15, "(Write code, press Enter, then Ctrl-d)")
        program = get_program()
        stack = parse(program)
        print("-------<<<STACK>>>-------")
        print(format_stack(stack))
        print("\n\n\n")
    return

repl()
