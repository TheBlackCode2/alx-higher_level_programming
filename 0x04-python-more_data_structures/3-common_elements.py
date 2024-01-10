#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_3 = set()
    for elm in set_1:
        if elm in set_2:
            set_3.add(elm)
    return set_3
