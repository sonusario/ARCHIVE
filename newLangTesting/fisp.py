def run(funcs, stack, called):
    if called in funcs:
        print(called, " was called.")
    return (funcs, stack)

def addFunc(funcs, arr, itr):
    argCount = 0
    while arr[itr] != ')':
        if arr[itr] != ')' and arr[itr][0] != '#':
            raise Exception("Expected '#', '#<str>', or ')', found", arr[itr])
        elif arr[irt]
    return (funcs, itr)

def fisp(pgrm):
    functions = {}
    stack = []
    arr = pgrm.split(' ')

    itr = 0
    while itr < len(arr):
        item = arr[itr]
        if item == "@":
            functions,stack = run(functions , stack, stack.pop)
        elif item == "(":
            functions,itr = addFunc(functions, arr, itr)
        else:
            stack.append(item)

        itr += 1

    return (functions, stack)
