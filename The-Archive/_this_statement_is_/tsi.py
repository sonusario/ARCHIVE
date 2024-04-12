def A(ftv):#A is false
    if ftv == True or ftv == False:
        return int(not ftv)
    return int((not ftv(0)) and (not ftv(1)))

def C(ftv):#C is paradox
    if ftv == True or ftv == False:
        return int(ftv and (not ftv))
    return int(ftv(0) and (not ftv(1)))

def D(ftv):#D is indeterminate
    if ftv == True or ftv == False:
        return int(ftv or (not ftv))
    return int((not ftv(0)) and ftv(1))

def B(ftv):#B is true
    if ftv == True or ftv == False:
        return int(ftv)
    return int(ftv(0) and ftv(1))
