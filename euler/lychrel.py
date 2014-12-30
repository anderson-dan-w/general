#!/usr/bin/python3

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_lychrel(n, count=0, maximum=50):
#    print("n={}, count={}, max={}".format(n, count, maximum))
    if count == maximum:
#        print("\treturning none")
        return None
    rev_n = int(str(n)[::-1])
    new_n = n + rev_n
    if is_palindrome(new_n):
#        print("\tfound palindrome")
        return 1
#    print("\tcalling new_n:{}".format(new_n))
    new_lychrel = get_lychrel(new_n, count+1, maximum=maximum)
    if new_lychrel is None:
        return None
    return 1 + new_lychrel
