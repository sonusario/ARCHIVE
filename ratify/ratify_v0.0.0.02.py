Word = str
List = list

################ Parsing: tokenize, read_from_tokens, and parse

def tokenize(s):
    return s.split()

def read_from_tokens(tokens, recFlag=False):
    L = []
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token == '(':
            L.append(read_from_tokens(tokens, True))
        elif token == ')':
            if recFlag:
                return L
            else:
                raise SyntaxError('unexpected ")"')
        else:
            L.append(token)

    if recFlag:
        raise SyntaxError('unexpected EOF')

    return L

def parse(program):
    return read_from_tokens(tokenize(program))

################ Default Dicionary

global_scope = {}

################ Evaluate Expression

def call_handler(lst_pntr, lst):
    global global_scope
    del_cnt = 1
    called = lst[lst_pntr-1]
    if type(called) == type([]):
        return del_cnt, called
    elif called not in global_scope:
        return del_cnt, [called]
    del_cnt, output = global_scope[called](lst[:lst_pntr-1])
    return

def forward_call_handler(stk_indx, stack):
    lst = stack[stk_indx]
    lst_pntr = 0
    while lst_pntr < len(lst):
        if type(lst[lst_pntr]) == type([]):
            sub = forward_call_handler(lst_pntr, lst)
            lst = lst[:lst_pntr] + sub + lst[lst_pntr+1:]
        elif lst[lst_pntr] == '/@' and lst_pntr != 0:
            del_cnt, sub = call_handler(lst_pntr, lst)
            lst = lst[:lst_pntr-del_cnt] + sub + lst[lst_pntr+1:]
            lst_pntr = lst_pntr - del_cnt
    return [lst]

def eval_expr(expr):
    global global_stack
    global_stack = expr
    pgrm_pntr = 0
    while prgm_pntr < len(global_stack):
        if type(global_stack[pgrm_pntr]) == type([]):
            sub = forward_call_handler(pgrm_pntr, global_stack)
            global_stack = global_stack[:pgrm_pntr] + sub + global_stack[pgrm_pntr+1:]
        elif global_stack[pgrm_pntr] in ['@','/@'] and prgm_pntr != 0:
            del_cnt, sub = call_handler(pgrm_pntr, global_stack)
            global_stack = global_stack[:pgrm_pntr-del_cnt] + sub + global_stack[pgrm_pntr+1:]
            pgrm_pntr = pgrm_pntr - del_cnt
    return
    
#program = "a b c ( ( x y z ) F -> ( x ) ) $"
#print(parse(program))

################ Interaction: A REPL

def repl(prompt="ratify> "):
    while True:
        val = eval_expr(parse(input(prompt)))
        if val is not None:
            print(ratify_str(val))

def ratify_str(exp):
    if isinstance(exp, List):
        return '( ' + ' '.join(map(ratify_str, exp)) + ' )'
    else:
        return str(exp)
