#!/usr/bin/python3

def uniq_add(my_list=[]):
    q = set(my_list)
    r = 0
    for i in q:
        r += i
    return r
