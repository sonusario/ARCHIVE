tape = [0]
t_pointer = 0
output = ""

ascii_limit = 256 #1114111

def interwfstr(fstr,string):
    return fstr + fstr.join(list(''.join(map(str,string.split())))) + fstr

def inc():
    tape[t_pointer] = (tape[t_pointer] + 1) % ascii_limit

def dec():
    tape[t_pointer] = (tape[t_pointer] - 1) % ascii_limit

def right():
    global t_pointer
    t_pointer += 1
    if t_pointer == len(tape):
        tape.append(0)

def left():
    global t_pointer
    t_pointer -= 1
    if t_pointer < 0:
        t_pointer = len(tape) - 1

def prnt():
    c = chr(tape[t_pointer])
    global output
    output += c
    print(c)

def n_put():
    prompt = "Awaiting input char: "
    tape[t_pointer] = ord(input(prompt))

def b_Loop(exp,bc):
    c = 0
    while tape[t_pointer] != 0:
        c = evaluate(exp)
    return c + bc

command = {'+':inc, '-':dec,
           '>':right, '<':left,
           '.':prnt, ',':n_put}

def print_state():
    global tape
    global t_pointer
    global output
    ascii_tape = list(map(chr,tape))
    spaces_t = ' '*len(str(tape[:t_pointer])) if t_pointer != 0 else ''
    spaces_a = ' '*len(str(ascii_tape[:t_pointer])) if t_pointer != 0 else ''

    print('='*77)
    print(tape, "TAPE")
    print(spaces_t, '^')
    print(spaces_t[6:] + "index: " + str(t_pointer))
    print(spaces_t[6:] + "cell : " + str(t_pointer + 1))
    print('-'*64)
    print(ascii_tape, "ASCII TAPE")
    print(spaces_a, ' ^')
    print("Has printed:", ascii(output))
    print('='*77)

def reset():
    global tape
    global t_pointer
    global output
    
    tape = [0]
    t_pointer = 0
    output = ""

def evaluate(exp):
    c = 0
    while c < len(exp):
        if exp[c] == '[':
            c = b_Loop(exp[c+1:],c+1)
        elif exp[c] == ']':
            return c
        elif exp[c] in command:
            command[exp[c]]()
        if "tape" in exp[c:c+4]:
            print(tape)
        elif "pntr" in exp[c:c+4]:
            print(t_pointer)
        elif "out" in exp[c:c+3]:
            print(ascii(output))
        elif "state" in exp[c:c+5]:
            print_state()
        elif "reset" in exp[c:c+5]:
            reset()
        c += 1

def repl(prompt="bf.py> "):
    while True:
        evaluate(input(prompt))
    return

repl()

'''
resetstate+state+state+state+state+state+state+state+state+state+state[state>state+state+state+state+state+state+state+state>state+state+state+state+state+state+state+state+state+state+state>state+state+state+state>state+state<state<state<state<state-state]state>state+state+state.state>state+state.state+state+state+state+state+state+state+state.state.state+state+state+state.state>state+state+state.state<state<state+state+state+state+state+state+state+state+state+state+state+state+state+state+state+state.state>state.state+state+state+state.state-state-state-state-state-state-state.state-state-state-state-state-state-state-state-state.state>state+state.state>state.
'''
