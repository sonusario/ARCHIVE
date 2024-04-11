'''
@ $ -> ( )
'''

stack = []
rulers = []

def tokenize(program):
    global stack
    t0 = program.replace('(', ' ( ').replace(')', ' ) ').replace('@', ' @ ')
    t1 = t0.replace('$',' $ ').replace('->', ' -> ')
    tokens = stack + t1.split()
    return tokens

def judge(tokens):
    stack = []
    
    state = "add_token"
    while len(tokens) > 0:
        token = tokens.pop(0)
        
