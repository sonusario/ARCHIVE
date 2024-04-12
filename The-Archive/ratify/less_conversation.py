from copy import deepcopy as copy

'''
@ $ -> ( )
'''

stack = []
mode = "repl"

def tokenize(program):
    global stack
    t0 = program.replace('(', ' ( ').replace(')', ' ) ').replace('@', ' @ ')
    t1 = t0.replace('$',' $ ').replace('->', ' -> ')
    tokens = stack + t1.split()

def read_from_tokens(tokens, recFlag=False, dCheck=0):
    STAK = []
    TYPE = []
    META = []
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token == '(':
            if dCheck >= 0: dCheck += 1
            s = read_from_tokens(tokens, True, dCheck)
            STACK.append(s)
        elif token == ')':
            if recFlag:
                return LST
            else:
                raise SyntaxError("unexpected ')'")
        else:
            LST.append(token)

def parse(program):
    return read_from_tokens(tokenize(program))
