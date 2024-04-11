# words, numbers, strings, definitions, calls, specifiers
import operator as op
import math
import re

def tokenize(chars: str) -> list:
    paren = chars.replace('(', ' ( ').replace(')', ' ) ')
    brack = paren.replace('[', ' [ ').replace(']', ' ] ')
    curly = brack.replace('{', ' { ').replace('}', ' } ')
    escap = curly.replace('\\', ' \\ ')
    escly = re.sub(r'\\\s+{', r'\{', escap)
    return escly.split()

def word(token: str) -> Word:
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)

def read_from_tokens(tokens: list, defFlag=False) -> Exp:
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    nestOpenDict = {'(':')', '[':']'}
    nestClosDict = {')':'(', ']':'['}
    token = tokens.pop(0)
    if token in nestDict:
        L = []
        if token == '[' and not defFlag:
            L.append('define')
        elif token == '[':
            raise SyntaxError('unexpexted', token + '.', 'already in "define" space')
        while tokens[0] != nestDict[token]:
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif token in nestClosDict:
        raise SyntaxError('unexpected', token)
    else:
        return word(token)

def parse(program: str) -> Exp:
    return read_from_tokens(tokenize(program))
