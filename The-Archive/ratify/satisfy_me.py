from copy import deepcopy as copy


'''
@ $ -> ( )
'''


stack = []
stack_pointer = -1
sub_pointer = -1
mode = "repl"
error_message = ""

def tokenize(program):
    global stack_pointer
    global mode
    
    stack_pointer = len(stack)
    tokens = stack + program.replace('(', ' ( ').replace(')', ' ) ').split()
    if stack_pointer == len(tokens):
        mode = "repl"
    return tokens
    

def stacker(tokens):
    global stack
    global stack_pointer
    global sub_pointer
    global mode
    global error_message

    list_depth = 0
    start = -1
    if stack_pointer == len(tokens):
        stack = tokens
        mode = "repl"
        return
    elif tokens[stack_pointer] == '(':
        list_depth += 1
        sub_pointer = stack_pointer
        stack_pointer += 1
        start = stack_pointer
        for i in range(start, len(tokens)):
            if tokens[stack_pointer] == ')':
                list_depth -= 1
            elif tokens[stack_pointer] == '(':
                list_depth += 1
            if list_depth == 0:
                break
            stack_pointer += 1
    elif tokens[stack_pointer] == ')':
        list_depth -= 1
    elif tokens[stack_pointer] == '@':
        mode = "call"
        return
    elif tokens[stack_pointer] == '$':
        mode = "define"
        return
    
    if list_depth != 0:
        mode = "error"
        paren = "Extra '(' found" if list_depth > 0 else "Extra ')' found"
        location = start if start != -1 else stack_pointer
        location = str(location - len(stack))
        error_message = "Error! " + paren + " at/after token " + location

    stack_pointer += 1        
    return

def call():
    return

'''
((input names) function name
  (match -> outA)
  (-> outB)) $ 
'''

def define(tokens):
    global stack_pointer
    global sub_pointer
    global mode
    global error_message

    var_names = []
    function_name = ""
    match_lists = []
    
    sp_cursor = sub_pointer + 1
    token = tokens[sp_cursor]
    if tokens[stack_pointer - 1] != ')':
        mode = "error"
        error_message = "Error! Invalid definition structure."
        return []
    elif tokens[sp_cursor] != '(':
        mode = "error"
        error_message = "Error! Invalid definition structure."
        return []
    
    sp_cursor += 1
    while tokens[sp_cursor] != ')':
        token = tokens[sp_cursor]
        if token == '@' or token == '$':
            mode = "error"
            error_message = "Error! Found " + token + " in VAR LIST."
            return []
        var_names.append(token)
        
    sp_cursor += 1
    token = tokens[sp_cursor]
    if token in ['(',')','@','$']:
        mode = "error"
        error_message = "Error! Found " + token + " in FUNCTION NAME SPACE"
        return []
    function_name = token

    sp_cursor += 1
    token = tokens[sp_cursor]
    if token != '(':
        mode = "error"
        error_message = "Error! Invalid definition structure."
        return []

    sp_cursor += 1
    depth = 0
    while tokens[sp_cursor] != ')':
        token = tokens[sp_cursor]
        if token in ['@','$']:
            mode = "error"
            error_message = "Error! Found " + token + " in MATCH SPACE"
            return []
        elif token == ')' and depth = 0:
            mode = "error"
            error_message = "Error! Expected MATCH value or '->'. Got ')'"
            return []
        
    if token in ['@','$']:
        mode = "error"
        error_message = "Error! Found " + token + " in MATCH SPACE"
        return []
    elif token == "->":
        match_lists
        
    
    mode = "stack"
    return

def error():
    global mode
    global error_message
    print(error_message)
    mode = "repl"
    return

def repl():
    global mode
    while True:
        program = input(">>> ")
        tokens = tokenize(program)
        
        mode = "stack"
        while mode != "repl":
            if mode == "stack": stacker(tokens)
            elif mode == "call": call()
            elif mode == "define": define(tokens)
            elif mode == "error": error()
