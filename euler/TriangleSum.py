#!/usr/bin/python3
def TriList(x):
    ls = [0]
    y = 0
    for i in range(1, x+1):
        y += i
        ls.append(y)
    return ls
