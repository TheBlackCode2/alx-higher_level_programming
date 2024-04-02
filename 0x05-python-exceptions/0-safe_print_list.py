#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x): 
            print(str(my_list[i]), end="")
        print("\n")
        return i + 1
    except:
        print("\n")
        return i
