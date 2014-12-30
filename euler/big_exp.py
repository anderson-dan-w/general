#!/usr/local/bin/python3
import math

def readPairs(fname):
    ls = []
    with open(fname) as fh:
        lines = fh.readlines()
        for line in lines:
            base, exp = line.split(",")
            base, exp = int(base), int(exp)
            ls.append((base, exp))
    return ls

def getMaxPair(pair_list):
    return max(pair_list, key=lambda x:math.log(x[0]) * x[1])

def getLargestIndexFromFile(fname):
    pairs = readPairs(fname)
    maxpair = getMaxPair(pairs)
    return pairs.index(maxpair)
