#!/usr/bin/python3
def uppercase(str):
    for count in str:
        temp = chr(ord(count) - 32)
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(count) - 32)
            print("{}".format(temp), end='')
        print()
