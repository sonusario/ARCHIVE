from copy import deepcopy as copy

'''
=======
Implemented
---
@ $ -> ( ) /@
=======
To Add
---
- help
- debug tooling
- infinite loop handling
- pause ???
- print def?
- compose and decompose
- \ and remove literal
- until at front of local space
- Stack Out v. Console Out
- anon function making
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
    conditions_and_outputs = []

    if type(tokens) != type([]) or len(tokens) == 0:
        raise SyntaxError("Ratify> Expected definition structured " +
                          "LIST Found '" + str(tokens) + "'.")

    # ---Generate list of variables---
    token = tokens.pop(0)
    if type(token) != type([]):
        raise SyntaxError("Ratify> Expected VAR LIST. " +
                          "Found '" + token + "'.")

    while len(token) > 0:
        sub_token = token.pop(0)

        if type(sub_token) == type([]) or sub_token in ['$','@','/@','->']:
            raise SyntaxError("Ratify> Expected VAR. " +
                              "Found '" + sub_token + "'.")
        else:
            var_names.append(sub_token)

    # ---Get function name---
    if len(tokens) == 0:
        raise SyntaxError("Ratify> Expected FUNCTION NAME. " +
                          "Found NOTHING.")
    
    token = tokens.pop(0)
    if type(token) == type([]) or token in ['$','@','/@','->']:
        raise SyntaxError("Ratify> Expected FUNCTION NAME. "
                          "Found '" + token + "'.")
    
    function_name = token

    if len(tokens) == 0:
        raise SyntaxError("Ratify> Expected " +
                          "CONDITION_AND_OUTPUT LIST(s). Found NOTHING.")

    # ---Generate list(s) of conditions and outputs---
    while len(tokens) > 0:
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
        while len(token) > 0:
            sub_token = token.pop(0)

            if arrow_side == "matches":
                if type(sub_token) == type([]) or sub_token in ['$','@','/@']:
                    raise SyntaxError("Ratify> Expected MATCH " +
                                      "or '->'. Found '" + token + "'.")
                elif sub_token == '->':
                    arrow_side = "outputs"
                    continue

            cond_out[arrow_side].append(sub_token)

        cond_len = len(cond_out["matches"])
        if cond_len > 0 and cond_len != len(var_names):
            raise SyntaxError("Ratify> Number of items in " +
                              str(cond_out["matches"]) + " is not zero and " +
                              "does not match the number of items in " +
                              str(var_names) + ".")

        conditions_and_outputs.append(cond_out)

    defined[function_name] = {"vars":var_names, "conds":conditions_and_outputs}
    return

def gen_output(output_list, val_LUT, var_list):
    out_stack = []
    for out in output_list:
        if type(out) == type([]):
            out_stack.append(gen_output(out, val_LUT, var_list))
        elif out in val_LUT:
            out_stack.append(val_LUT[out])
        elif out in var_list:
            continue
        else:
            out_stack.append(out)
    return out_stack

def call(tokens, fname):
    global defined
    
    if type(fname) == type([]):
        return fname
    elif fname not in defined:
        return [fname]
    
    var_list = copy(defined[fname]["vars"])
    cond_list = copy(defined[fname]["conds"])
    var_count = len(var_list)
    output = []

    values = []
    counter = 0
    while len(tokens) > 0 and counter < var_count:
        values.append(tokens.pop(-1))
        counter += 1
    values.reverse()
    val_len = len(values)

    val_LUT = {}
    for i in range(val_len): # Assigns values inputed to function variables
        val_LUT[str(var_list[i])] = values[i] # str Handles list inputs

    there_is_a_match = False
    cond = None
    while there_is_a_match is False and len(cond_list) > 0:
        cond = cond_list.pop(0)

        match_list = cond["matches"]
        match_len  = len(match_list)
        if match_len > val_len: # Helps handle empty inputs
            for i in range(match_len - val_len):
                values.append('')

        match_flag = True
        for i in range(match_len):
            if str(match_list[i]) in val_LUT: # Places input values in match space
                match_list[i] = val_LUT[str(match_list[i])]
            if match_list[i] != values[i]:
                match_flag = False # Helps handle empty inputs

        if match_len == 0 or match_flag:
            there_is_a_match = True

    output_list = cond["outputs"]
    
    if there_is_a_match:
        for out in output_list:
            if type(out) == type([]):
                output.append(gen_output(out, val_LUT, var_list))
            elif out in val_LUT:# Places input values in output space per spec.
                output.append(copy(val_LUT[str(out)]))
            elif out in var_list: # Handles case where a variable was referenced
                continue #skip    # in the output space but there were not enou-
            else:                 # -gh inputs to give it a value
                output.append(out)
    return output

def read_from_tokens(tokens, recDepth=0, lstTokenFlag=False):
    STACK = []

    while len(tokens) > 0:
        #print(format_stack(["Ratify>"] + tokens))
        token = tokens.pop(0)
        if token == '(':
            STACK.append(read_from_tokens(tokens, recDepth + 1))
        elif type(token) == type([]):
            STACK.append(read_from_tokens(token, recDepth + 1, True))
        elif token == ')':
            if recDepth > 0:
                return STACK
            else:
                raise SyntaxError("Ratify> Unexpected ')'.")
        elif token == '$' and recDepth == 0:
            define(STACK.pop(-1))
        elif (token == '@' and recDepth == 0)or(token == '/@' and recDepth < 2):
            if STACK == []: continue #change "== 0" to "< 2" for min. char set
            prepend_tokens = call(STACK,STACK.pop(-1))
            while len(prepend_tokens) > 0: # Add items produced by function
                tokens.insert(0,prepend_tokens.pop(-1))
        elif token == '->' and recDepth == 0:
            raise SyntaxError("Ratify> Unexpected '->'.")
        else:
            STACK.append(token)

    if recDepth > 0 and not lstTokenFlag:
        raise SyntaxError("Ratify> Unexpected EOF. Expected " +
                          str(recDepth) + " more ')'s")
    return STACK

def parse(program):
    return copy(read_from_tokens(tokenize(program)))

def get_program():
    content = []
    while True: # Get multi-lined input
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

repl()

'''
Ideas:
=======
compile to wasm
compile to jvm
add multithreading based on how many values a function "eats"
'''
