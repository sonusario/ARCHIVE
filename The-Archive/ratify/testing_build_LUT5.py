from copy import deepcopy as copy

'''
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
            lstName([],p,LUT)
            blank(p, LUT)
        else:
            LUT[p] = []

def lstName(val, p, LUT):
    cName = concat_name(p)
    LUT[cName] = val

def rest(v):
    if len(v) > 1:
        return v, True
    elif len(v) > 0:
        return v[0], False
    return '',False

def nest_LUT(v, p, LUT):
    LV = len(v)
    LP = len(p)
    if LP == 1:
        data_compare(v,p[0],LUT,True)
    elif LP == 2:
        data_compare(v[0] if len(v) > 0 else '',p[0],LUT)
        val, flag = rest(v[1:])
        data_compare(val,p[1],LUT,flag)
    else:
        data_compare(v[0] if len(v) > 0 else '',p[0],LUT)

        cnt = 1
        while cnt < LV-1 and cnt < LP-1:
            if cnt == LP-2:
                val, flag = rest(v[cnt:-1])
                data_compare(val,p[cnt],LUT,flag)
            else:
                data_compare(v[cnt],p[cnt],LUT)
            cnt += 1
        if cnt != LP-1:
            blank(p[cnt:],LUT)
        
        data_compare(v[-1] if len(v) > 0 else '',p[-1],LUT)

def data_compare(v, p, LUT, nestFlag=False):
    vbool = True if type(v) == type([]) and not nestFlag else False
    pbool = True if type(p) == type([]) else False
    val = [] if v == '' else [v]
    if not vbool and not pbool:
        LUT[p] = val
    elif not vbool and pbool:
        lstName(val,p,LUT)
        blank(p,LUT)
    elif vbool and not pbool:
        LUT[p] = val
    elif vbool and pbool:
        lstName(val,p,LUT)
        nest_LUT(v,p,LUT)

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    LP = len(p)
    while len(v) < LP:
        v.append('')
    for i in range(LP):
        data_compare(v[i],p[i],LUT)
'''


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
            lstName([],p,LUT)
            blank(p, LUT)
        else:
            LUT[p] = []

def lstName(val, p, LUT):
    cName = concat_name(p)
    LUT[cName] = val

def rest(v):
    if len(v) > 1:
        return v, True
    elif len(v) > 0:
        return v[0], False
    return '',False

def data_compareB(v, p, LUT):
    pbool = True if type(p) == type([]) else False
    if not pbool:
        LUT[p] = v
    elif pbool:
        lstName([v],p,LUT)
        nest_LUT(v,p,LUT)
    
def nest_LUT(v, p, LUT):
    LV = len(v)
    LP = len(p)
    if LP == 1:
        data_compareB(v,p[0],LUT)
    elif LP == 2:
        data_compareA(v[0] if len(v) > 0 else '',p[0],LUT)
        data_compareB(v[1:],p[1],LUT)
    else:
        data_compareA(v[0] if len(v) > 0 else '',p[0],LUT)

        cnt = 1
        while cnt < LV-1 and cnt < LP-1:
            if cnt == LP-2:
                data_compareB(v[cnt:-1],p[cnt],LUT)
            else:
                data_compareA(v[cnt],p[cnt],LUT)
            cnt += 1
        if cnt != LP-1:
            blank(p[cnt:],LUT)
        
        data_compareA(v[-1] if len(v) > 0 else '',p[-1],LUT)

def data_compareA(v, p, LUT):
    vbool = True if type(v) == type([]) else False
    pbool = True if type(p) == type([]) else False
    val = [] if v == '' else [v]
    if not vbool and not pbool:
        LUT[p] = val
    elif not vbool and pbool:
        lstName(val,p,LUT)
        blank(p,LUT)
    elif vbool and not pbool:
        LUT[p] = val
    elif vbool and pbool:
        lstName(val,p,LUT)
        nest_LUT(v,p,LUT)

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    LP = len(p)
    while len(v) < LP:
        v.append('')
    for i in range(LP):
        data_compareA(v[i],p[i],LUT)

