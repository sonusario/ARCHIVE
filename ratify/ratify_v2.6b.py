from copy import deepcopy as copy

'''
=======
Implemented
---
@ $ -> ( ) # %
=======
'''

defined = {}

def tokenize(rawtxt):
    t0 = rawtxt.replace('@', ' @ ').replace('$', ' $ ').replace('->', ' -> ')
    t1 = t0.replace('(', ' ( ').replace(')', ' ) ')
    tokens = t1.split()
    return tokens

def listify(tokens, recFlag=False):
    program = []
    
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
    if recFlag:
        raise SyntaxError("Ratify> Unexpected EOF. Expected more ')'s")
    
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
        if token in ['@','$','->','#','%']:
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
    elif token in ['@','$','#','%']:
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

def concat_name(lst, recFlag=False):
    cname = "{"
    for n in lst:
        if type(n) == type([]):
            cname += concat_name(n, True) + "}"
        else:
            cname += n + "_"
    return cname[:-1] + "}"

def lstName(val, p, LUT):
    cName = concat_name(p)
    LUT[cName] = val

def blank(params, LUT):
    for p in params:
        if type(p) == type([]):
            lstName([],p,LUT)
            blank(p, LUT)
        else:
            LUT[p] = []

def ALL(lst, cnt):
    return lst,True

def FIRST(lst, cnt):
    if len(lst[cnt:]) > 0:
        return lst[cnt:][0],False
    return '',False

def REST(lst, cnt):
    return lst[cnt:],True

def BODY(lst, cnt):
    return lst[cnt:-1],True

def LAST(lst, cnt):
    if len(lst) > 0:
        return lst[-1],False
    return '',False

def nest_assoc(v,p,LUT):
    LV = len(v)
    LP = len(p)
    lst_pt = LP - (2 if LP > 2 else 1)
    fs_choice = 2 if LP > 2 else LP-1
    f_set = [[ALL], [FIRST,REST], [FIRST,BODY,LAST]][fs_choice]
    f_cnt = 0
    cnt = 0
    while cnt < LP:
        val,nestFlag = f_set[f_cnt](v,cnt)
        data_compare(val,p[cnt],LUT,nestFlag)
        if cnt == lst_pt-1 or cnt == lst_pt:
            f_cnt += 1
        cnt +=1

def vCheck(v,nestFlag):
    if nestFlag:
        if len(v) == 1:
            if type(v[0]) == type([]):
                return True
            else:
                return False
        else:
            return False
    return True

def data_compare(v, p, LUT, nestFlag=False):
    val = [] if v == '' else (v if nestFlag else [v])
    if type(p) == type([]):
        if nestFlag:
            lstName(v,p,LUT)
        else:
            lstName(val,p,LUT)
        vFlag = vCheck(v,nestFlag)
        if type(v) == type([]) and v != [] and vFlag:
            VAL = v[0] if vFlag and nestFlag else v
            nest_assoc(VAL,p,LUT)
        else:
            blank(p,LUT)
    else:
        LUT[p] = val

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    LP = len(p)
    while len(v) < LP:
        v.append('')
    for i in range(LP):
        data_compare(v[i],p[i],LUT)

def replace_params(val_LUT, param_filled_list):
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

def mis_match_error(match_list_str, pCount_str):
    raise SyntaxError("Ratify> Number of items in " +
                      match_list_str + " is not zero and does " +
                      "not match the number of parameters in the " +
                      "parameter list " + pCount_str + ".")

def look_for_match(vals, vLUT, condouts, pCount, moreFlag):
    there_is_a_match = False
    while there_is_a_match is False and len(condouts) > 0:
        condout = condouts.pop(0)

        cond_list = condout["cond"]
        cond_count = len(cond_list)
        if cond_count == 0:
            there_is_a_match = True
            continue

        match_list = replace_params(vLUT, cond_list)
        match_list = evaluate([],match_list,True)###
        match_count = len(match_list)

        if match_count != pCount and moreFlag:
            mis_match_error(str(match_list), str(pCount))
        elif match_count != pCount and not moreFlag:####
            continue

        vCount = len(vals)
        if match_count > vCount and moreFlag:
            mis_match_error(str(match_list), str(vCount))
        elif match_count > vCount:
            while match_count > len(vals):
                vals.append('')
        elif match_count < vCount and match_count > 0:
            mis_match_error(str(match_list), str(vCount))

        match_flag = True
        if match_count == 0:
            match_flag = False
        for i in range(match_count):
            if vals[i] != match_list[i]:
                match_flag = False
        if match_flag:
            there_is_a_match = True
    return there_is_a_match, condout["out"]

def compose(lst):
    composition = ""
    for item in lst:
        if type(item) == type([]):
            composition += compose(item)
        else:
            composition += item
    return composition

def decompose(word):
    lst = []
    for c in word:
        lst.append(c)
    return lst

def call(tokens, fname):
    global defined

    function = {"params":[], "fname":'->', "condouts":[{"cond":[],"out":[]}]}
    if type(fname) == type([]):
        return [evaluate([],fname,True)]###
    elif fname == '$':
        if len(tokens) == 0:
            raise SyntaxError("Ratify> Expected definition structured " +
                              "LIST. Found NOTHING.")
        function_is_anon, function = define(tokens.pop(-1))
        if not function_is_anon: return []
    elif fname == '#':
        if len(tokens) == 0:
            raise SyntaxError("Ratify> Expected LIST. Found NOTHING.")
        elif type(tokens[-1]) != type([]):
            raise SyntaxError("Ratify> Expected LIST. Found " +
                              tokens[-1] + ".")
        else:
            return [compose(tokens.pop(-1))]
    elif fname == '%':
        if len(tokens) == 0:
            raise SyntaxError("Ratify> Expected WORD. Found NOTHING.")
        elif type(tokens[-1]) == type([]):
            raise SyntaxError("Ratify> Expected WORD. Found " +
                              str(tokens[-1]) + ".")
        else:
            return [decompose(tokens.pop(-1))]
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
    moreFlg = len(tokens) > 0

    vLUT = {}
    build_LUT(values, params, vLUT)

    there_is_a_match, out_list = look_for_match(values, vLUT, condouts,
                                                pCount, moreFlg)

    output = []
    if there_is_a_match:
        output = replace_params(vLUT, out_list)
    return output

itr = 0

def evaluate(stack, tokens,recFlag=False):#
    global defined
    global itr
    
    while len(tokens) > 0:
        token = tokens.pop(0)

        #print(format_stack(["Ratify>"] + stack + [token]))
        '''
        if token == '@':
            x = chr(946) if recFlag else chr(937)
            fn = '' if stack == [] else '' if type(stack[-1]) == type([]) else stack[-1]
            y = str(len(defined[fn]["params"])) if fn in defined else ''
            print(format_stack([str(itr),"Ratify>"] + stack + [x] + ["EATS-" + y]))
            #input()
            itr += 1
        #'''

        if token == '@':
            if stack == []: continue
            prepend_tokens = call(stack, stack.pop(-1))
            while len(prepend_tokens) > 0:
                tokens.insert(0, prepend_tokens.pop(-1))
        else:
            stack.append(token)
    if not recFlag:
        itr = 0
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
