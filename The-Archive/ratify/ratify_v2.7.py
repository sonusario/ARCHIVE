from copy import deepcopy as copy

'''
=======
Implemented
---
( ) -> ~ { } $ @ \ # % ratify
=======
'''

def repl():
    g_stack = []
    defined = {}
    while True:
        print("-------<<<INPUT>>>-------",
              " "*15, "(Write code, press Enter, then Ctrl-d)")
        program = read()
        g_stack = evaluate(copy(g_stack), program, defined)
        print("-------<<<STACK>>>-------")
        print(format_stack(g_stack))
        print("\n\n\n")
    return

repl()
