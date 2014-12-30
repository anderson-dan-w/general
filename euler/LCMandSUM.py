#!/usr/bin/python3
from time import time
st = time()

def LCM(x, y):
    tempList = [x]
    for i in range(2, y+1):
        tempList.append(x*i)5
    for i in range(x+1):
        if i*y in tempList:
            return i*y
    return x*y

def Triangle(x, m):
    ceil = m//x
    return int(x*(ceil*(ceil+1)/2))

def SumTo(m, x=1, y=None):
    if y is not None:
        lcm = LCM(x, y)
    else:
        y = x
        lcm = x
    return Triangle(x, m) + Triangle(y, m) - Triangle(lcm, m)
    
