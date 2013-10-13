#!/usr/bin/python3

import Divisors as div

def divSum(x):
    ls = div.getDivisors(x)
    add = sum(ls)-x
    return add

def paired(x):
    sumX = divSum(x)
    if sumX < x:
        sumY = divSum(sumX)
        if sumY == x:
            return [x, int(sumX)]
    return []

def allPairsUnder(x, m=2):
    pairs = []
    for num in range(m, x):
        pairs += paired(num)
    return pairs
