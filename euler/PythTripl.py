#!/usr/bin/python3
from time import time
def pythTriple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False

def pyth100():
    st = time()
    for a in range(1, 500):
        for b in range(a, 500):
            for c in range(200, 600):
                if a+b+c == 1000:
                    if pythTriple(a, b, c):
                        el = time()-st
                        print("took ", el, a, b, c, a*b*c)
                        return (a, b, c)

