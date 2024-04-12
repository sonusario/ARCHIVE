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
        err_txt = missing_txt + ". " + err_txt
    raise SyntaxError("Ratify> Error with definition spec. " + err_txt)
        

def gen_var_list(tokens, recFlag=False):
    var_names = []
    
    if type(tokens) != type([]):
        raise SyntaxError("Ratify> Expected VAR LIST. " +
                          "Found '" + tokens + "'.")
    elif tokens == [] and recFlag:
        raise SyntaxError("Ratify> Empty list parameters are not allowed.")
    
    form = "typeA"
    while len(tokens) > 0:
        token = tokens.pop(0)
        if recFlag and len(tokens) == 0:
            form = "typeB"

        if token in ['@','$','->']:
            raise SyntaxError("Ratify> Expected VAR. " +
                              "Found '" + token + "'.")
        elif type(token) == type([]): #Build list parameter(s)
            var_names.append({"data":gen_var_list(token, True),"form":"list"})
        else:
            var_names.append({"data":token,"form":form})
    return var_names

def get_func_name(token):
    if type(token) == type([]) or token in ['@','$','->']:
        raise SyntaxError("Ratify> Expected FUNCTION NAME. "
                          "Found '" + token + "'.")
    return token

def get_cond(token, recFlag=False):
    cond = []
    while len(token) > 0:
        sub_token = token.pop(0)
        if sub_token == '->' and not recFlag:
            return cond
        elif sub_token == '@' and not recFlag:
            raise SyntaxError("Ratify> Expected MATCH " +
                              "or '->'. Found '@'.")
            

def gen_cond_and_output_lists(tokens):
    while len(tokens) > 0: #Each iteration covers a new conditional and output
        token = tokens.pop(0)

        if type(token) != type([]):
            raise SyntaxError("Ratify> Expected " +
                              "CONDITION_AND_OUPUT LIST. " +
                              "Found '" + token + "'.")
        elif token == [] or '->' not in token:
            raise SyntaxError("Ratify> Expected [OPTIONAL CONDITION" +
                              "(s) -> OPTIONAL OUTPUT(s)].  Either no '->' " +
                              "was given or an empty list was given.")

        arrow_side = "matches"
        cond_out = {"matches":[],
                    "outputs":[]}

        cond_out["matches"] = get_cond(token)
        while len(token) > 0:
            sub_token = token.pop(0)
            cond_out["outputs"].append(sub_token)

    return

def define(tokens):
    global defined
    function_name = ""
    conditionals_and_outputs = []

    if type(tokens) != type([]):
        raise SyntaxError("Ratify> Expected definition structured " +
                          "LIST Found '" + str(tokens) + "'.")
    elif len(tokens) < 3:
        raise_NotEnoughData_error(len(tokens))
        
    # ---Generate list of variables---
    token = tokens.pop(0)
    var_names = gen_var_list(token)
    
    # ---Get function name---
    token = tokens.pop(0)
    function_name = get_func_name(token)
    
    # ---Generate list(s) of conditions and outputs---
    conditions_and_outputs = gen_cond_and_output_lists(tokens)

    defined[function_name] = {"vars":var_names, "conds":conditions_and_outputs}
    return

def call(tokens, fname):
    global defined
    
    if type(fname) == type([]):
        return [read_from_tokens(fname)]
    elif fname not in defined:
        return [fname]
    elif fname == '$':
        define(tokens.pop(-1))
        return []
    
    return

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
        elif token == '@' and recFlag:
            if STACK == []: continue #Nothing to run if stack is empty
            prepend_tokens = call(STACK,STACK.pop(-1))
            while len(prepend_tokens) > 0: #Add items produced by function
                tokens.insert(0,prepend_tokens.pop(-1))
        else:
            STACK.append(token)

    if recFlag and not lstTokenFlag:
        raise SyntaxError("Ratify> Unexpected EOF. Expected " +
                          str(recDepth) + " more ')'s")
    return

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
