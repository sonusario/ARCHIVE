from copy import deepcopy as copy

def concat_name(lst, recFlag=False):
    cname = "" if recFlag else "_"
    for n in lst:
        if type(n) == type([]):
            cname += concat_name(n, True)
        else:
            cname += n + "_"
    return cname

def lstName(val, p, LUT):
    cName = concat_name(p)
    LUT[cName] = val

def blank(params, LUT):
    for p in params:
        if type(p) == type([]):
            lstName([],p,LUT)
            blank(p, LUT)
        else:
            LUT[p] = []

def typeHandler(v, p, LUT):
    vtype = "LIST" if type(v) == type([]) else "WORD"
    ptype = "LIST" if type(p) == type([]) else "WORD"
    if vtype != ptype:
        raise SyntaxError("Ratify> Argument '" + v + "' passed " +
                          "to function was of type " + vtype + ". " +
                          "Expected type " + ptype + ".")
    elif vtype == "LIST":
        nest_LUT(v,p,LUT)
    else:
        LUT[p] = [] if v == '' else [v]

def oneParam(v,par,LUT):
    p = par[0]
    if type(p) == type([]):
        nest_LUT(v,p,LUT)
    else:
        LUT[p] = [v]

def twoParams(v,p,LUT):
    typeHandler(v[0],p[0],LUT)
    if type(p[1]) == type([]):
        nest_LUT(v[1:],p,LUT)
    else:
        LUT[p[1]] = [v]

def triParams(v,p,LUT):
    LV = len(v)
    LP = len(p)

    typeHandler(v[0],p[0],LUT)
    typeHandler(v[-1],p[-1],LUT)
    
    cnt = 1
    while cnt < LV-1 and cnt < LP-1:
        if cnt == LP-2:
            if type(p[cnt]) == type([]):
                nest_LUT(v[cnt:],p[cnt],LUT)

def nest_LUT(v, p, LUT):
    lstName([v],p,LUT)
    if v == []:
        blank(p,LUT)
    LP = len(p)
    if LP == 1:
        oneParam(v,p,LUT)
    elif LP == 2:
        twoParams(v,p,LUT)
    else:
        triParams(v,p,LUT)

def build_LUT(values, params, LUT, fname):
    v = copy(values)
    p = copy(params)
    LP = len(p)
    cnt = len(v)
    while cnt < LP:
        v.append([] if type(p[cnt]) == type([]) else '')
        cnt += 1
    for i in range(LP):
        typeHandler(v[i],p[i],LUT)
