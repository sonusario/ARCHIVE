def matchMaker(fn_spec):
    return fn_spec[1], fn_spec[0] + ['->'] + fn_spec[2:]

def dictMaker(env , newDictionary={}):
    if env == []: return newDictionary
    else:
        fn, fn_spec matchMaker(env.pop(0))
        newDictionary[fn] = fn_spec
        dictMaker(env, newDictionary)

def prependDict(raw, env, processed, func)

def rattatat(exprs, env, processed):
    global dictionary
    if exprs[0] == '@':
        reprocess(exprs[1:], env, processed[:-1], dictionary[processed[-1]])
    elif exprs[0:2] == ['$','@']:
        rattatat(prependDict(exprs[2:], env, processed))
    elif exprs = []: return processed
    else:
        rattatat(exprs[1:], env, processed + [exprs[0]])

def ratify(exprs, env):
    global dictionary
    dictionary = dictMaker(env)
    rattatat(exprs, env, [])
