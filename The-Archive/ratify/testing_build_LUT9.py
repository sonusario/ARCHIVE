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

def ALL(lst,cnt):
    return lst

def FIRST(lst,cnt):
    if len(lst) > 0:
        return lst[0]
    return ''

def REST(lst,cnt):
    return lst[cnt:]

def BODY(lst,cnt):
    return lst[cnt:-1]

def LAST(lst,cnt):
    if len(lst) > 0:
        return lst[-1]
    return ''

def nest_assoc(v, p, LUT):
    LV = len(v)
    LP = len(p)
    phr_pt = LP - (2 if LP > 2 else 1)
    fs_choice = 2 if LP > 2 else LP-1
    f_cnt = 0
    f_set = [[ALL], [FIRST,REST], [FIRST,BODY,LAST]][fs_choice]
    s_typ = [['<phr>'], ['<cmp>','<phr>'], ['<cmp>','<phr>','<cmp>']][fs_choice]
    cnt = 0
    while cnt < LP:
        print("Data compare",f_set,f_cnt,v,cnt,p,s_typ,f_cnt)
        #data_compare(f_set[f_cnt](v,cnt),p[cnt],LUT,s_typ[f_cnt])
        if cnt == phr_pt-1:
            f_cnt += 1
        elif cnt == phr_pt:
            f_cnt + 1
        cnt += 1

def data_compare(v, p, LUT, sType):
    val = [] if v == '' else [v]
    if type(p) == type([]):
        lstName(val,p,LUT)
        if sType=='<cmp>' and type(v) == type([]) and v != []:
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
        data_compare(v[i],p[i],LUT,'<cmp>')
