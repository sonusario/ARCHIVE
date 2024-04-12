from random import randrange
import time

typeInt = type(int())
typeFloat = type(float())
typeComplex = type(complex())

typeStr = type(str())
typeBytes = type(bytes())
typeTuple = type(tuple())
typeFrozenset = type(frozenset())
typeBool = type(bool())


typeBytearry = type(bytearray())
typeList = type(list())
typeSet = type(set())
typeDict = type(dict())

def is_int(var):
    return type(var) == typeInt

def is_float(var):
    return type(var) == typeFloat

def is_complex(var):
    return type(var) == typeComplex

def is_str(var):
    return type(var) == typeStr

def is_bytes(var):
    return type(var) == typeBytes

def is_tuple(var):
    return type(var) == typeTuple

def is_frozenset(var):
    return type(var) == typeFrozenset

def is_bool(var):
    return type(var) == typeBool

def is_bytearray(var):
    return type(var) == typeBytearray

def is_list(var):
    return type(var) == typeList

def is_set(var):
    return type(var) == typeSet

def is_dict(var):
    return type(var) == typeDict

def gProg(arrI, arrO):
    dex = {}
    for i in range(len(arrI)):
        dex[arrI[i]] = arrO[i]
    dex = str(dex)
    def f(x):
        dx = '000'
        exec('global dx')
        exec('dx = ' + dex)
        ndx = dx
        return ndx[x]
    return f


#gProg(['10'],['[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]'])
