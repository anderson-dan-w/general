#!/usr/bin/python3
from time import time
import math

def isPrime(x, ls):
    for p in ls:
        if x % p == 0:
            return False
    return True


def primesUnder(x):
    plist = []
    ceil = x//6 + 1
    for i in range(1, ceil):
        if isPrime(6*i - 1, plist):
            plist.append(6*i - 1)
        if isPrime(6*i + 1, plist):
            plist.append(6*i + 1)
    plist.insert(0, 3)
    plist.insert(0, 2)
    return plist


def factor(bignum):
    st = time()
    factors = []
    while bignum % 2 == 0:
        bignum /= 2
        factors.append(2)
    while bignum % 3 == 0:
        bignum /= 3
        factors.append(3)
    start = 1
    while bignum > 1:
        for num in range(start, int(bignum//6 + 6)):
            less = num*6 - 1
            more = num*6 + 1
            if bignum % less == 0:
                bignum /= less
                start = num
                factors.append(less)
                break
            if bignum % more == 0:
                bignum /= more
                start = num
                factors.append(more)
                break
    el = time() - st
    return factors, el
