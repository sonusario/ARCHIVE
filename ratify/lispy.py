import operator as op
import math

Symbol = str
Number = (int, float)
Atom   = (Symbol, Number)
List   = list
Exp    = (Atom, List)
Env    = dict

def tokenize(chars: str) -> List:
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def atom(token: str) -> Atom:
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)

def read_from_tokens(tokens: list) -> Exp:
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError('unexpected ")"')
    else:
        return atom(token)

def parse(program: str) -> Exp:
    return read_from_tokens(tokenize(program))

def standard_env() -> Env:
    env = Env()
    env.update(vars(math))
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv,
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq,
        'abs':      abs,
        'append':   op.add,
        'apply':    lambda proc, args: proc(*args),
        'begin':    lambda *x: x[-1],
        'car':      lambda x: x[0],
        'cdr':      lambda x: x[1:],
        'cons':     lambda x,y: [x] + y,
        'eq?':      op.is_,
        'expt':     pow,
        'equal':    op.eq,
        'length':   len,
        'list':     lambda *x: list(x),
        'list?':    lambda x: isinstance(x, List),
        'map':      map,
        'max':      max,
        'min':      min,
        'not':      op.not_,
        'null?':    lambda x: x == [],
        'number?':  lambda x: isinstance(x, Number),
        'print':    print,
        'procedure?': callable,
        'round':    round,
        'symbol?':  lambda x: isinstance(x, Symbol),
    })
    return env

global_env = standard_env()

def Eval(x: Exp, env=global_env) -> Exp:
    if isinstance(x, Symbol):
        return env[x]
    elif not isinstance(x, Number):
        return x
    elif x[0] == 'if':
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':
        (_, symbol, exp) = x
        env[symbol] = eval(exp, env)
    else:
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)

