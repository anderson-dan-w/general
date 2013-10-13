#!/usr/bin/python3
from time import time
from math import *

def isPrime(numb, primes):
    for p in primes:
        if numb % p == 0:
            return False
    return True

def getPrimesUpTo(maxnum):
    primeList = []
    st = time()
    div = maxnum/6 + 2
    resets = []
    base=10
    limit = 10
    threes = 27
    while threes < maxnum:
        resets.append(threes)
        threes *= 3
    for i in range(1, int(div)):
        p = i*6 -1
        if p-2 in resets:
            newbase = int(sqrt(p*3))
            if newbase %2 == 0:
                newbase += 1
            while base <= newbase-10:
                if newbase in primeList:
                    print(p, " at p, base now is ", newbase)
                    base = newbase
                    limit = primeList.index(base)
                newbase+=2
        if isPrime(p, primeList[:limit]):
            primeList.append(p)
        if isPrime(p+2, primeList[:limit]):
            primeList.append(p+2)
    primeList.insert(0, 3)
    primeList.insert(0, 2)
    el = time()-st
    print("took ", el)
    return primeList
