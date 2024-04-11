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

def nest_assoc(v, p, LUT):
    LV = len(v)
    LP = len(p)
    lst_pt = LP - (2 if LP > 2 else 1)
    cnt = 0
    while cnt < LP:
        if cnt == lst_pt:
            val = [] if cnt >= LV-1 else v[cnt:-1]
            data_compare(val,p[cnt],LUT)
        elif cnt != LP-1:
            val = [] if cnt >= LV-1 and not (LV==1 and cnt==0) else v[cnt]
            data_compare(val,p[cnt],LUT)
        elif cnt not in [0,1]:
            data_compare(v[-1:][0],p[cnt],LUT)
        cnt += 1

def data_compare(v, p, LUT):
    val = [] if v == '' else [v]
    if type(p) == type([]):
        lstName(val,p,LUT)
        if type(v) == type([]):
            if v == []:
                blank(p,LUT)
            else:
                nest_assoc(v,p,LUT)
        else:
            blank(p,LUT)
    else:
        LUT[p] = val

def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    LP = len(p)
    while len(v) < LP:
        v.append('')
    for i in range(LP):
        data_compare(v[i],p[i],LUT)
