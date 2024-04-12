from copy import deepcopy as copy
from inspect import signature

g_stack = []
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

def call(tokens, fname):
    global defined

    if type(fname) == type([]):
        return [evaluate([], fname)]
    elif fname == '$':
        define(tokens.pop(-1))
    elif fname == '->':
        function

def evaluate(stack, tokens):
    if len(tokens) == 0:
        return stack
    if tokens[0] == '@':
        prepend_tokens = call(stack, stack.pop(-1))
        while len(prepend_tokens) > 0:
            tokens.insert(0, prepend_tokens.pop(-1))
    else:
        stack.append(token)
    return stack
        

def read():
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)
    return listify(tokenize(' '.join(content)))

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
    global g_stack
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
