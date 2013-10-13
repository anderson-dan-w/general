#!/usr/bin/python3
def fact(x):
    total = 1
    for y in range(2,x+1):
        total *= y
    return total


def SumDigits(num):
    st = str(num)
    s = 0
    for let in st:
        s += int(let)
    return s

def calcSumFactDigit(x):
    bignum = fact(x)
    s = SumDigits(bignum)
    return s
