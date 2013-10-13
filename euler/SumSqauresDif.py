#!/usr/bin/python3
def sumSquareDif(x):
    sums = 0
    squares = 0
    for i in range(x+1):
        sums += i
        squares += i*i
    sums *= sums
    print(abs(sums-squares))
