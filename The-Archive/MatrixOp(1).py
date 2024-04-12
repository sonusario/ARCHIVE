# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 05:54:34 2017

@author: stert
"""

from copy import deepcopy as dcpy

def vTOm(v):
    return [v]

def mTOv(M):
    return M[0]

def T(A):
    AT = []
    aLen = len(A)
    iLen = len(A[0])
    for j in range(iLen):
        ATi = []
        for i in range(aLen):
            ATi.append(A[i][j])
        AT.append(ATi)
    return AT

def dotProd(v1, v2):
    pSum = 0
    for i in range(len(v1)):
        pSum += v1[i] * v2[i]
    return pSum

def sMatProd(A, B):
    C = []
    BT = T(B)
    for Ai in A:
        Ci = []
        for Bj in BT:
            Ci.append(dotProd(Ai,Bj))
        C.append(Ci)
    return C

def matAdSu(A, B, adsu):
    C = []
    aLen = len(A)
    azLen = len(A[0])
    for i in range(aLen):
        Ci = []
        for j in range(azLen):
            Ci.append(A[i][j] + (adsu * B[i][j]))
        C.append(Ci)
    return C

def matSum(A, B):
    return matAdSu(A,B,1)

def matSub(A, B):
    return matAdSu(A,B,-1)

def matScalAdd(A, s):
    C = []
    aLen = len(A)
    azLen = len(A[0])
    for i in range(aLen):
        Ci = []
        for j in range(azLen):
            Ci.append(A[i][j] + s)
        C.append(Ci)
    return C

def matScalProd(A, s):
    C = []
    aLen = len(A)
    azLen = len(A[0])
    for i in range(aLen):
        Ci = []
        for j in range(azLen):
            Ci.append(s * A[i][j])
        C.append(Ci)
    return C

def matVectAdd(A, v):
    C = []
    aLen = len(A)
    azLen = len(A[0])
    for i in range(aLen):
        Ci = []
        for j in range(azLen):
            Ci.append(A[i][j] + v[j])
        C.append(Ci)
    return C

def matProd(A, B):
    C = []
    for i in range(len(A)):
        Ci = []
        for j in range(len(B[0])):
            kSum = 0
            for k in range(len(A[0])):
                kSum += A[i][k] * B[k][j]
            Ci.append(kSum)
        C.append(Ci)
    return C
