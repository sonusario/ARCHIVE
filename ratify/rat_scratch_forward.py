from copy import deepcopy as copy
from atexit import register

'''
=======
Implemented
---
@ $ -> ( ) /@
=======
To Add
---
- print def?
- compose and decompose
- \
- until at front of local space
- Stack Out v. Console Out
'''

stack = []
defined = {}

def tokenize(program):
    global stack
    t0 = program.replace('(', ' ( ').replace(')', ' ) ')
    t1 = t0.replace('/@', '<forward_func_call>').replace('@', ' @ ')
    t2 = t1.replace('<forward_func_call>', ' /@ ')
    t3 = t2.replace('$',' $ ').replace('->', ' -> ')
    tokens = stack + t3.split()
    return tokens

def define(tokens):
    global defined
    var_names = []
    function_name = ""
    output_conditions = []
    if type(tokens) != type([]):
        raise SyntaxError("Error! Expected definition structured LIST" +
                          " Found '" + tokens + "'.")
    token = tokens.pop(0)
    if token != '(':
        raise SyntaxError("Error! Expected VAR LIST. Found '" + token + "'.")
    
    while token != ')':
        token = tokens.pop(0)
        if token in ['(','@','$','->']:
            raise SyntaxError("Error! Expected VAR. Found '" + token + "'.")
        elif token == ')': continue
        else:
            var_names.append(token)

    token = tokens.pop(0)
    if token in ['(',')','@','$','->']:
        raise SyntaxError("Error! Expected FUNCTION NAME. Found '" +
                          token + "'.")
    function_name = token
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token != '(':
            raise SyntaxError("Error! Expected OUPUT CONDITION LIST." +
                              "Found '" + token + "'.")
        out_cond = {"match":[],
                    "output":[]}
        while token != "->":
            token = tokens.pop(0)
            if token in ['(',')','@','$']:
                raise SyntaxError("Error! Expected MATCH or '->'. Found '" +
                                  token + "'.")
            elif token == '->': continue
            else:
                out_cond["match"].append(token)

        condL = len(out_cond["match"])
        if condL > 0 and condL != len(var_names):
            raise SyntaxError("Error! Number of items in " +
                              str(out_cond["match"]) + " is not zero and " +
                              "does not match the number of items in " +
                              str(var_names) + ".")
        depth = 1
        while depth > 0:
            token = tokens.pop(0)

            if token == '(': depth += 1
            elif token == ')': depth -= 1

            if depth != 0:
                out_cond["output"].append(token)

        output_conditions.append(out_cond)

    defined[function_name] = {"vars":var_names, "conds":output_conditions}
    return

def call(tokens, fname):
    lt = len(tokens)
    if type(fname) == type([]):
        return -lt, fname
    global defined
    if fname not in defined:
        return -lt, [fname]
    var_list = copy(defined[fname]["vars"])
    cond_list = copy(defined[fname]["conds"])
    
    num_of_vars = len(var_list)
    if num_of_vars == 0:
        values = []
    else:
        values = tokens[-num_of_vars:]
    val_LUT = {}
    for i in range(len(values)):
        val_LUT[var_list[i]] = values[i]
    val_len = len(values)
   
    noMatch = True
    output = []
    cond = None
    while noMatch and len(cond_list) > 0:
        cond = cond_list.pop(0)
        match_list = cond["match"]
        match_len = len(match_list)
        if match_len > val_len: #val_a*:handles empty match
            for i in range(match_len - val_len):
                values.append('')
        output_list = cond["output"]
        if len(match_list) == 0:
            noMatch == False
        match_flag = True
        for i in range(len(match_list)):
            if match_list[i] in val_LUT:
                match_list[i] = val_LUT[match_list[i]]
            if match_list[i] != values[i]:#val_a*:handles empty match
                match_flag = False
        if match_flag:
            noMatch = False

    if noMatch == False:
        output_list = cond["output"]
        for out in output_list:
            if out in val_LUT:
                output.append(val_LUT[out])
            elif out in var_list:
                continue
            else:
                output.append(out)
    if num_of_vars == 0:
        return -lt, output
    else:
        return num_of_vars, output

def read_from_tokens(tokens, recDepth=0):
    STACK = []
    ran_atFlag = False
    while len(tokens) > 0:
        token = tokens.pop(0)
        #print('before', token, '<<<', STACK, '>>>--<<<',tokens, '>>>', recDepth)
        #print(token, "|", tokens, "|", recDepth)
        if ran_atFlag: recDepth += 1#
        ran_atFlag = False#
        if token == '/@' and recDepth == 0:
            token = '@'
        if token == '(' and recDepth == 0:
            STACK.append(read_from_tokens(tokens, recDepth + 1)[:-1])
        elif token == '(':
            STACK.append('(')
            STACK += read_from_tokens(tokens, recDepth + 1)
        elif token == ')':
            if recDepth > 0:
                STACK.append(')')
                return STACK
            else:
                raise SyntaxError("Error! Unexpected ')'.")
        elif token == '$' and recDepth == 0:
            define(STACK.pop(-1))
        elif token == '@' and recDepth == 0:
            if STACK == []: continue
            trash, prepend = call(STACK,STACK.pop(-1))
            STACK = STACK[:-trash]
            tokens = prepend + tokens
        elif token == '/@' and recDepth == 1:
            #print('inside1', token, '<<<', STACK, '>>>--<<<',tokens, '>>>', recDepth)
            if STACK == []: continue
            trash, prepend = call(STACK,STACK.pop(-1))
            #print('inside-MID:',trash, prepend)
            STACK = STACK[:-trash]
            tokens = prepend + tokens
            #print('inside2', token, '<<<', STACK, '>>>--<<<',tokens, '>>>', recDepth)
            ran_atFlag = True#
        elif token == '->' and recDepth == 0:
            raise SyntaxError("Error! Unexpected '->'.")
        else:
            STACK.append(token)
        print('after', token, '<<<', STACK, '>>>--<<<',tokens, '>>>', recDepth)

    if recDepth > 0:
        raise SyntaxError("Error! Unexpected EOF.")
    return STACK

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

def repl():
    global stack
    while True:
        print("-------<<<INPUT>>>-------",
              " "*15, "(Write code, press Enter, then Ctrl-d)")
        program = get_program()#input(">>> ")
        stack = parse(program)
        print("-------<<<STACK>>>-------")
        for token in stack:
            print(token, end=" ")
        print("\n\n\n")

repl()
