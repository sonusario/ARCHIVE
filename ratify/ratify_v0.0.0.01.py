def tokenize(chars: str):
    return chars.split()

def read_from_tokens(tokens: list, recFlag: bool):
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

def parse(program: str):
    return read_from_tokens(tokenize(program), False)    

program = "a b c ( ( x y z ) F -> ( x ) ) $"
print(parse(program))
