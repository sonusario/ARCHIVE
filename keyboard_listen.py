from pynput.keyboard import Key, Listener

stack = ""

def on_press(key):
    global stack
    if key == Key.backspace:
        '''
        if stack[-2:] == r"\\":
            stack
        '''
        stack = stack[:-1]
    elif key == Key.enter:
        stack += "\n"
    elif key == Key.tab:
        stack += "\t"
    elif key == Key.space:
        stack += " "
    elif len(str(key)) > 3:
        return
    else:
        stack += str(key)[1:-1]
    if key == Key.backspace:
        print()
        print(stack, end='')
    else:
        print(stack[-1:], end='')

def on_release(key):
    global stack
    if key == Key.enter and stack[-3:] == "\n\n\n":
        print(stack[:-2])
        return False
            

def NAVI():
    global stack
    stack = ""
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

NAVI()
