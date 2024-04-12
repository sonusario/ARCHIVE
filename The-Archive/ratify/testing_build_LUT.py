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
'''
def build_rLUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    build_LUT(v[0:1], p[0:1],LUT)
    pMid = p[1:-1]
    vMid = v[1:-1]
    while len(vMid) < len(pMid):
        vMid.append('')
    for i in range(len(pMid)):
        if type(pMid[i]) == type([]):
            if type(vMid[i]) != type([]):
                build_rLUT([], pMid[i],LUT)
            else:
                build_rLUT(vMid[i],pMid[i],LUT)
    build_LUT(v[1:-1],p[1:-1],LUT)
    build_LUT(v[-1:],p[-1:],LUT)
    return
'''
'''
def build_rLUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    build_LUT(v[0:1], p[0:1],LUT)
    if len(p[1:-1]) == 1:
        if type(p[1:-1][0]) != type([]):
            LUT[p[1:-1][0]] = v[1:-1]
        else:
            build_LUT(v[1:-1],p[1:-1],LUT)
    else:
        build_LUT(v[1:-1],p[1:-1],LUT)
    build_LUT(v[-1:],p[-1:],LUT)
    return
'''
'''
def build_rLUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    LP = len(p)
    if LP == 1:
        build_LUT(v[:],p[:],LUT)
    elif LP == 2:
        build_LUT(v[0:1], p[0:1],LUT)
        build_LUT(v[1:], p[1:],LUT)
    elif LP > 2:
        build_LUT(v[0:1], p[0:1],LUT)
        build_LUT(v[1:-1], p[1:-1],LUT)
        build_LUT(v[-1:],p[-1:],LUT)
    return

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    while len(v) < len(p):
        v.append('')
    for i in range(len(p)):
        if type(p[i]) == type([]):
            if type(v[i]) != type([]):
                build_rLUT([], p[i], LUT)
            else:
                build_rLUT(v[i], p[i], LUT)
            cName = concat_name(p[i])
            if len(p[i]) == 1:
                LUT[cName] = v
            else:
                LUT[cName] = [v[i]]
        else:
            if v[i] == '':
                LUT[p[i]] = []
            else:
                LUT[p[i]] = [v[i]]
    return

'''
'''
def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    while len(v) < len(p):
        v.append('')
    for i in range(len(p)):
        if type(p[i]) == type([]):
            if type(v[i]) != type([]):
                build_rLUT([], p[i], LUT)
            else:
                build_rLUT(v[i], p[i], LUT)
            cName = concat_name(p[i])
            LUT[cName] = [v[i]]
        else:
            if v[i] == '':
                LUT[p[i]] = []
            else:
                LUT[p[i]] = [v[i]]
    return
'''
'''
def n_assoc(values, params, LUT):
    for i in range(len(params)):
        val = []
        if i < len(values):
            if values[i] != '':
                val = [values[i]]
        if type(params[i]) == type([]):
            cName = concat_name(params[i])
            LUT[cName] = val

def n_assoc(values, params, LUT):
    for i in range(len(params)):
        if i < len(values):
            assoc(values[i],params[i],LUT)
'''

def first(lst):
    if type(lst) == type([]):
        if len(lst) > 0:
            return lst[0]
    return ''

def body(lst):
    if type(lst) == type([]):
        return lst[1:-1]
    return ''

def rest(lst):
    if type(lst) == type([]):
        return lst[1:]
    return ''

def last(lst):
    if type(lst) == type([]):
        if len(lst) > 0:
            return lst[-1]
    return ''

def n_assoc(values, params, LUT):
    LP = len(params)
    if LP == 1:
        assoc(values,first(params),LUT)
    elif LP == 2:
        assoc(first(values),first(params),LUT)
        assoc(rest(values),rest(params),LUT)
    else:
        assoc(first(values),first(params),LUT)
        assoc(body(values),body(params),LUT)
        assoc(last(values),last(params),LUT)

def assoc(value, param, LUT, nFlag=False):
    if param == '': return
    val = [] if value == '' else [value]
    if type(param) == type([]):
        cName = concat_name(param)
        LUT[cName] = val
        if type(value) == type([]):
            n_assoc(value,param,LUT)
        else:
            for p in param: assoc('',p,LUT)
    else:
        LUT[param] = val

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    while len(v) < len(p):
        v.append('')
    for i in range(len(v)):
        assoc(v[i],p[i],LUT)








'''
def n_assoc(values, params, LUT):
    if values == []:
        for param in params: assoc('',param,LUT)
    frst = values[:1][0]
    body = values[1:-1]
    last = values[-1:][0]

    rFlag = False
    LFLAG = False
    if len(values) > 1:
        rFlag = True
    if rFlag:
        if type(values[1]) != type([]):
            LFLAG = True
    
    LP = len(params)
    if LP == 1:
        assoc(values,params[0],LUT,True)
    elif LP == 2:
        assoc(frst,params[0],LUT,False)
        assoc(values[1:],params[1],LUT,True)
    else:
        assoc(values[:1],params[0],LUT,True)
        assoc(values[1:-1],params[1:-1],LUT,False)
        assoc(values[-1:],params[-1],LUT,True)

def n_assoc(values, params, LUT):
    if values == []:
        for param in params: assoc('',param,LUT)
    frst = values[:1][0]
    body = values[1:-1]
    last = values[-1:][0]

def assoc(value, param, LUT, nFlag=False):
    if nFlag:
        val = value
    else:
        val = [] if value == '' else [value]
    if type(param) == type([]):
        cName = concat_name(param)
        LUT[cName] = val
        n_assoc(value if type(value) == type([]) else [], param, LUT)
    else:
        LUT[param] = val

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    while len(v) < len(p):
        v.append('')
    for i in range(len(v)):
        assoc(v[i],p[i],LUT)

'''
