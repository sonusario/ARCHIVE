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
