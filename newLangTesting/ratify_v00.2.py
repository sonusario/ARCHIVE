import re

def tokenize(chars: str):
    paren = chars.replace('(', ' ( ').replace(')', ' ) ')
    brack = paren.replace('[', ' [ ').replace(']', ' ] ')
    curly = brack.replace('{', ' { ').replace('}', ' } ')
    escap = curly.replace('\\', ' \\ ')
    escly = re.sub(r'\\\s+{', r'\{', escap)
    return escly.split()

def printTree(tree):
    for branch in tree:
        if type(branch.val) == list:
            print('( ', end="")
            printTree(branch.val)
            print(') ', end="")
        else:
            print(branch.val, end=" ")
    

class node:
    def __init__(self, literal, kind):
        self.val = literal
        self.obj_type = kind

def makeListNode(tokens: list):
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(makeListNode(tokens))
            if L[-1] == '/@':
                try: eat,val = spliceCall(L[:-2],L[-2])
                except: raise IndexError("Can't eat")
                L = L[:eat]
                L.append(val)
        tokens.pop(0)
        return node(L, 'list')
    elif token == ')':
        raise SyntaxError('unexpected ")"')
    else:
        return node(token, 'word')

def transcribe(tokens: list):
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    strand = []
    while len(tokens) != 0:
        if tokens[0] == '(':
            strand.append(makeListNode(tokens))
    return strand
                    
            
