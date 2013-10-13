#!/usr/bin/python3
from time import time
def CollatzUnder(x):
    st = time()
    dc = {}
    dc[1] = 1
    for i in range(2, x):
        temp = []
        y=i
        temp.append(int(y))
        while y != 1:
            if y %2 == 0:
                y/= 2
            else:
                y = y*3 + 1
            y = int(y)
            temp.append(y)
            if y in dc:
                preval = y
                for t in range(len(temp)-1):
                    val = temp[-t-2]
                    dc[val] = dc[preval] + 1
                    preval = val
                break
    return (dc, time()-st)
