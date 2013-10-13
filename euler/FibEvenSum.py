#!/usr/bin/python3
from time import time


def evenFibSum(num):
    st = time()
    x = 2
    y = 8
    tot = 2
    while y <= num:
        tot += y
        (x, y) = (y, 4*y + x)
    el = time() - st
    return tot, el
