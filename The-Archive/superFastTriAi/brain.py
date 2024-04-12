from random import randrange as rand
from copy import deepcopy as cpy

key = [[[0,1,2],[3,4,5],[6,7,8]],[[9,10,11],[12,13,14],[15,16,17]],[[18,19,20],[21,22,23],[24,25,26]]]

C = [0,1,-1]
def clock(n):
    return C[n+1]

def snMux(gfList, sel):
    return gfList[key[sel[0][0]+1][sel[1][0]+1][sel[2][0]+1]][0]

#pass refferences to nodes to get outputs
