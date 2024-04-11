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
            assoc(v[0],p[0],LUT)
        else:
            LUT[p[0]] = v[0]
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
            assoc(v[0],p[0],LUT)
        else:
            LUT[p[0]] = v[0]
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
                    assoc(v[cnt],p[cnt],LUT)
                else:
                    LUT[p[cnt]] = v[cnt]
            cnt += 1
        if cnt != LP:
            blank(p[cnt:],LUT)
        if type(p[-1]) == type([]):
            cName = concat_name(p[-1])
            LUT[cName] = v[-1]
            assoc(v[-1],p[-1],LUT)
        else:
            LUT[p[-1]] = v[-1]

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
            if type(v[i]) == type([]):
                if v[i] == []:
                    blank(p[i],LUT)
                else:
                    assoc(v[i],p[i],LUT)
            else:
                blank(p[i],LUT)
        else:
            LUT[p[i]] = val
