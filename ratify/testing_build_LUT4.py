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
            blank(p, LUT)
        else:
            LUT[p] = []

def assoc(v, p, LUT, recFlag=False):
    LV = len(v)
    LP = len(p)
    if LP == 1:
        if type(p[0]) == type([]):
            cName = concat_name(p[0])
            LUT[cName] = v
            assoc(v,p[0],LUT)
        else:
            LUT[p[0]] = v
    elif LP == 2:
        if type(p[0]) == type([]):
            cName = concat_name(p[0])
            LUT[cName] = v[0]
            bPlate(v,0,p,LUT)
        else:
            LUT[p[0]] = [v[0]]
        if type(p[1]) == type([]):
            cName = concat_name(p[1])
            LUT[cName] = v[1:]
            assoc(v[1:],p[1],LUT)
        else:
            LUT[p[1]] = v[1:]
    else:
        if type(p[0]) == type([]):
            cName = concat_name(p[0])
            LUT[cName] = v[0]
            bPlate(v,0,p,LUT)
        else:
            LUT[p[0]] = [v[0]]
        cnt = 1
        while cnt < LV-1 and cnt < LP-1:
            val = [] if v[cnt] == '' else [v[cnt]]
            if cnt == LP-2:
                if type(p[cnt]) == type([]):
                    cName = concat_name(p[cnt])
                    LUT[cName] = v[cnt:-1]
                    assoc(v[cnt:-1],p[cnt],LUT)
                else:
                    LUT[p[cnt]] = v[cnt:-1]
            else:
                if type(p[cnt]) == type([]):
                    cName = concat_name(p[cnt])
                    LUT[cName] = v[cnt]
                    bPlate(v,cnt,p,LUT)
                else:
                    LUT[p[cnt]] = val
            cnt += 1
        if cnt != LP:
            blank(p[cnt:],LUT)
        if type(p[-1]) == type([]):
            cName = concat_name(p[-1])
            LUT[cName] = v[-1]
            bPlate(v,-1,p,LUT)
        else:
            LUT[p[-1]] = [v[-1]]

def bPlate(v,i,p,LUT):
    if type(v[i]) == type([]):
        if v[i] == []:
            blank(p[i],LUT)
        else:
            assoc(v[i],p[i],LUT)
    else:
        blank(p[i],LUT)

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    LP = len(p)
    while len(v) < LP:
        v.append('')
    for i in range(LP):
        val = [] if v[i] == '' else [v[i]]
        if type(p[i]) == type([]):
            cName = concat_name(p[i])
            LUT[cName] = val
            bPlate(v,i,p,LUT)
        else:
            LUT[p[i]] = val
'''

'''
def nest_LUT(v, p, LUT):
    LV = len(v)
    LP = len(p)
    if LP == 1:
        data_compare(v,p[0],LUT,True)
    elif LP == 2:
        data_compare(v[0] if len(v) > 0 else '',p[0],LUT)
        data_compare(v[1:],p[1],LUT,True)
    else:
        data_compare(v[0] if len(v) > 0 else '',p[0],LUT)

        cnt = 1
        while cnt < LV-1 and cnt < LP-1:
            if cnt == LP-2:
                data_compare(v[cnt:-1],p[cnt],LUT,True)
            else:
                data_compare(v[cnt],p[cnt],LUT)
            cnt += 1
        
        data_compare(v[-1] if len(v) > 0 else '',p[-1],LUT)
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
