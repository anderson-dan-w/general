#!/usr/bin/python3
def isPalin(numb):
    l = len(numb)
    for k in range(int(l/2)):
        if numb[k] != numb[l-k-1]:
            return False
    return True


def findPalProduct(mx, mn=0):
    from time import time
    st = time()
    pals = [0]
    for i in range(mn,mx):
        for j in range(i, mx):
            numb = i*j
            if numb > pals[-1] and isPalin(str(numb)):
                pals.append(numb)
    pals.sort()
    el = time()-st
    print(pals[-1], "\ntook ", el)

