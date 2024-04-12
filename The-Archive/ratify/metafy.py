from copy import deepcopy as copy

stack = []
defined = {"@":call}
core = []

def build_LUT(values, params, LUT, recFlag=False): # under construction
    v = copy(values)
    p = copy(params)
    while len(v) < len(p):
        v.append('')
    if len(p) == 1:
        vel = 
        if type(p[0]) == type([]):
            build_LUT(
        return
    elif len(p) == 2:
        first
        body = p[1:-1]
        return
    elif len(p) > 2:
        return
    else:
        return
        

def call(tokens, fname):
    global core, defined
    if type(fname) == type([]):
        return [read_from_tokens(fname)]
    elif fname == '$':
        if len(tokens) == 0:
            raise SyntaxError("Ratify> Expected definition structured " +
                              "LIST. Found NOTHING.")
        func = tokens.pop(-1)
        if type(func) != type([]):
            raise SyntaxError("Ratify> Expected definition structured LIST.")
        elif len(func) < 3:
            raise SyntaxError("Ratify> Expecting definition LIST of length 3.")
        elif type(func[0]) != type([]):
            raise SyntaxError("Ratify> Expected PARAMETER LIST. Found '" +
                              func[0] + "'.")
        elif type(func[1]) == type([]) or func[1] in core:
            raise SyntaxError("Ratify> Invalid FUNCTION NAME.")
        else:
            for item in func[2:]:
                if type(item) != type([]):
                    raise SyntaxError("Ratify> Expected CONDOUT LISTs. " +
                                      "Found '" + item "'.")
                elif '->' not in item:
                    raise SyntaxError("Ratify> '->' not found in a " +
                                      + "CONDOUT LIST.")
        defined[func[1]] = func[:1] + func[2:]
        return []
    elif fname not in defined:
        return [fname]

    function = defined[fname]
    par_count = len(function[0])
    values = []
    counter = 0
    while len(tokens) > 0 and counter < par_count:
        values.insert(0,tokens.pop(-1))
        counter += 1
    val_count = len(values)

    val_LUT = {}
    build_LUT(values, function[0], val_LUT = {}
    return

'''
def test():
	print(x)
x = {"test":test}
x['test']()
'''
