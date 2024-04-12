from copy import deepcopy as copy


'''
@ $ -> ( )
'''


global_stack = []
para_pntrs = {}

def tokenize(line, glb_stack):
    return copy(glb_stack) + line.replace('(', ' ( ').replace(')', ' ) ').split()

def define_stuff(nxt_glb, nxt_para):
    pntr = len(nxt_glb) - 1
    if nxt_glb[pntr] != ')':
        return [],{},True
    

def procPy(tokens, glb_stack, para_pntrs):
    next_glb_stack = copy(glb_stack)
    next_para_pntrs = copy(para_pntrs)
    broken = False
    err_msg = ''
    i = 0
    p_cnt = 0
    while i < len(tokens):
        if tokens[i] == '@':
            call_stuff()
        elif tokens[i] == '$':
            next_glb_stack,next_para_pntrs,def_flag = define_stuff(next_glb_stack, next_para_pntrs)
            if def_flag:
                broken = True
                err_msg = "Incorrect DEFINITION structure"
        elif tokens[i] == '(':
            start = i
            next_glb_stack.append(tokens[i])
            p_cnt += 1
            while p_cnt > 0:
                i += 1
                if i >= len(tokens):
                    broken = True
                    err_msg = "Missing closing parens!"
                    break
                next_glb_stack.append(tokens[i])
                if tokens[i] == '(': p_cnt += 1
                elif tokens[i] == ')': p_cnt -= 1
            end = i
            next_para_pntrs[start] = end
            next_para_pntrs[end] = start
        elif tokens[i] == ')':
            broken = True
            err_msg = "Missing opening parens!"
        else:
            next_glb_stack.append(tokens[i])
        if broken:
            break
        i += 1
    return err_msg if broken else next_glb_stack
