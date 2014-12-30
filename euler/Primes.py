#!/usr/bin/python
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

def getFactors(num, primes):
    factors = []
    pindex = 0
    while num != 1:
        if num % primes[pindex]:
            pindex += 1
            if pindex == len(primes):
                print("incomplete!")
                break
        else:
            factors.append(primes[pindex])
            num /= primes[pindex]
    return factors

import collections
def areSameLenDistinct(first, second, length):
    if length != len(first) or len(first) != len(second):
        return False
    for k, v in first.items():
        if k in second and v == second[k]:
            return False
    return True

def findConsecutive(start, stop, primes, length):
    previous = collections.Counter()
    consecutive = 1
    for i in range(start, stop):
        current = getFactors(i, primes)
        current = collections.Counter(current)
        if areSameLenDistinct(previous, current, length):
            consecutive += 1
            print("consec: {} and {}".format(consecutive, i-1, i))
            if consecutive == length:
                print("DONE!\n\n")
        else:
            consecutive = 1
        previous = current

