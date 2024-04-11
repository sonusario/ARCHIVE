from copy import deepcopy as copy

def concat_name(lst, recFlag=False):
    cname = ""
    for n in lst:
        if type(n) == type([]):
            cname += concat_name(n, True)
        else:
            cname += n + "_"
    if recFlag:
        return cname
    return cname[:-1]

def blank(params, LUT):
    for p in params:
        if type(p) == type([]):
            blank(p, LUT)
        else:
            LUT[p] = []

def n_assoc(values, params, LUT):
    LP = len(params)
    for i in range(LP):
        if type(params[i] ==

def assoc(values, params, LUT, index):
    exec("cName = concat_name(params" + index + ")")
    exec("LUT[cName] = values" + index)
    exec(" () " +
         "if type(values" + index + ") == type([]) else " +
         " blank(params" + index + ", LUT)")

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    while len(v) < len(p):
        v.appen('')
    for i in range(len(p)):
        val = [] if value[i] == '' else [value[i]]
        if type(p[i]) == type([]):
            assoc(v,p,LUT,"[" + str(i) + "]")
        else:
            LUT[p[i]] = val
