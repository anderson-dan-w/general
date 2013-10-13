#!/usr/bin/python3
from math import *
from time import time

def triList(x):
    ls = []
    start = 1
    for i in range(2, x+1):
        ls.append(start)
        start += i
    return ls


def getDivisors(x):
    ls = [1, x]
    lim = int(sqrt(x))
    for i in range(2, lim+1):
        if x % i == 0:
            ls.append(i)
            ls.append(x/i)
    if lim in ls:
        ls.remove(lim)
    return ls

def maxDivUnderTri(y, m=0):
    st = time()
    tris = triList(y)
    maxdiv = 0
    maxval = 0
    for tri in tris[m:]:
        divs = getDivisors(tri)
        if len(divs) > maxdiv:
            maxdiv = len(divs)
            maxval = tri
            #print(maxdiv, " divisors for ", maxval)
        if maxdiv > 500:
            return (maxdiv, maxval, time()-st)
    return (maxdiv, maxval, time()-st)



            



    
