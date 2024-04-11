'''
=======
Implemented
---
@ $ -> ( ) # % ratify
=======
'''

class tode:
    def __init__(self, typ, S_data, L_data, prev=None):
        self.typ = typ
        self.S_data = S_data
        self.L_data = L_data
        self.prev = prev

def evaluate():
    return

def read():
    content = ""
    while True:
        try:
            line = input()
        except EOFError:
            break
        content += line + "\n"
    return content

def repl():
    g_stack = []
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
