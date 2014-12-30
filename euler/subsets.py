#!/usr/bin/python3

denoms = [1, 2, 5, 10, 20, 50, 100, 200]

def combos(total, max_denom):
    #print("called with total:{}; max_denom:{}".format(total, max_denom))
    if total == 0:
#        print("total 0")
        return 1
    if max_denom == 0:
#        print("max denom 0")
        return 0
    count = 0
    biggest = max([d for d in denoms if d <= max_denom])
    for i in range(total//biggest, -1, -1): ## include 0!
        amount = biggest * i
        count += combos(total - amount, biggest - 1)
    #print("\ttotal:{} max_denom:{}".format(total, max_denom))
    return count
