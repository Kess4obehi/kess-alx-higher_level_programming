#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = 0
    for i in set(my_list):
        uniq_list += i
    return uniq_list
