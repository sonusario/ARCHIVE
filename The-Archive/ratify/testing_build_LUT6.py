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

def lstr(v, p, LUT,spFlag=False):
    if spFlag:
        lstName([v],p,LUT)
    else:
        lstName(v,p,LUT)
    if v == []:
        blank(p,LUT)
    elif type(v[0]) != type([]):
        blank(p,LUT)
    else:
        val = v[0]
        LV = len(val)
        LP = len(p)
        if LP == 1:
            if type(p[0]) == type([]):
                lstr(val,p[0],LUT,True)
            else:
                LUT[p[0]] = [val]
        elif LP == 2:
            if type(p[0]) == type([]):
                lstr(val[:1],p[0],LUT)
            else:
                LUT[p[0]] = val[:1]
            if type(p[1]) == type([]):
                lstr(val[1:],p[1],LUT,True)
            else:
                LUT[p[1]] = [val[1:]]
        else:
            cnt = 0
            while cnt < LV and cnt < LP:
                if cnt == LP-2:
                    if type(p[cnt]) == type([]):
                        lstr(val[cnt:-1],p[cnt],LUT,True)
                    else:
                        LUT[p[cnt]] = [val[cnt:-1]]
                elif cnt == LP-1:
                    if type(p[cnt]) == type([]):
                        lstr(val[-1:],p[cnt],LUT)
                    else:
                        LUT[p[cnt]] = val[-1:]
                else:
                    if type(p[cnt]) == type([]):
                        lstr(val[cnt:cnt+1],p[cnt],LUT)
                    else:
                        LUT[p[cnt]] = val[cnt:cnt+1]
                cnt += 1
    
def build_LUT(values, params, LUT):
    v = copy(values)
    p = copy(params)
    for i in range(len(p)):
        if type(p[i]) == type([]):
            lstr(v[i:i+1],p[i],LUT)
        else:
            LUT[p[i]] = v[i:i+1]
